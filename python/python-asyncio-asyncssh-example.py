#!/usr/bin/env python3

"""Report the deployed SHA for named sets of hosts"""

import argparse
import asyncssh
import asyncio
import logging
import socket
import sys
import warnings

from dataclasses import dataclass
from constants import ENVS
from utils import get_hosts

API3_ROLES = ['api3', 'api3-se']
CLASSIFIER_ROLES = ['classifier-batch', 'classifier-batch-event', 'classifier-rpc']
CRITICAL_LOG_LEVEL = 50  # see: https://docs.python.org/3/library/logging.html#logging-levels


@dataclass
class HostSha:
    '''pair for hostname and the sha it is running'''
    host: str
    sha: str


def check_hosts(hosts):
    for host in hosts:
        try:
            socket.gethostbyname(host)
        except Exception:
            logging.warning('Could not find ip for {}'.format(host))
            hosts.remove(host)
    return hosts


def get_command(role):
    if role == 'api':
        role = 'api_server'
    elif role in API3_ROLES:
        role = 'api3_server'
    elif role == 'classifier' or role in CLASSIFIER_ROLES:
        role = 'classifier_server'
    elif role.startswith('ato-judgy'):
        role = 'ato-judgy'
    elif role.startswith('judgy'):
        role = 'judgy'
    return 'cat /opt/sift/{}/current/REVISION'.format(role)


async def get_service_sha(host: str, sha_command: str) -> HostSha:
    try:
        async with asyncssh.connect(host=host, known_hosts=None) as conn:
            ssh_result = await conn.run(sha_command)
            sha = ssh_result.stdout.strip() if ssh_result.exit_status == 0 else ssh_result.stderr.strip()
    except Exception as e:
        sha = str(e)

    return HostSha(host, sha)


async def run_all_hosts(hosts: set, command: str = None, timeout: int = 30):
    tasks = (get_service_sha(h, sha_command=command) for h in hosts)
    num_timed_out = 0
    for t in asyncio.as_completed(list(tasks), timeout=timeout):
        try:
            result = await t
        except (asyncio.TimeoutError) as e:
            num_timed_out += 1
            logging.error("timed out connecting to a host")
        except (Exception) as e:
            logging.debug(f"uncaught exception: {e}")
        else:
            print(f"{result.sha} {result.host}")

    if num_timed_out > 0:
        print(f"timed out on {num_timed_out} hosts", file=sys.stderr)


def main(role: str, env: str, timeout: int = 30):
    hosts = []
    if role == 'api3':
        for api3_role in API3_ROLES:
            hosts += get_hosts(env, api3_role)
    elif role == 'classifier':
        for classifier_role in CLASSIFIER_ROLES:
            hosts += get_hosts(env, classifier_role)
    else:
        hosts = get_hosts(env, role)

    hosts = list(hosts)
    checked_hosts = check_hosts(hosts)
    command = get_command(role)
    asyncio.run(run_all_hosts(checked_hosts, command, timeout=timeout))


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    parser = argparse.ArgumentParser(description='Verify the git SHA of all instances of a role in a given env')
    parser.add_argument('-d', '--debug', default=0, action='count', help='increase debugging; -dddd == DEBUG')
    parser.add_argument('-t', '--timeout', type=int, default=30, help='seconds to wait for all ssh connections to complete')
    parser.add_argument('env', type=str, help='The environment to use', choices=ENVS.keys())
    parser.add_argument('role', type=str, help='The role to verify')
    options = parser.parse_args()
    log_level = CRITICAL_LOG_LEVEL - (options.debug * 10)
    log_level = 10 if log_level < 10 else log_level
    logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s", level=log_level, stream=sys.stderr)
    main(options.role, options.env, timeout=options.timeout)
