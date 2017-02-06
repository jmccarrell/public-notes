# [3 hours to Docker fundamentals](https://www.youtube.com/watch?v=ddhU3NMrhX4)

- video

python supervisor -n

to run supervisor in the foreground mode, which will then start up all of the
processes you want in that docker container.

- 'a hidden gem in the docker eco system': docker.py

- boot2docker: docker on a mac

- unicorn is a chef thing: it can sit in front of ruby on rails
    - seems like it is only applicable to RoR

- start at 7:30

- slide of scripts is about 1:29:00

- end at 1:40:00

----

**Fri Jan 20 21:15:00 PST 2017**

restarting docker investigation after wanting to run team city inside a docker container on my mac.

- I uninstalled the old VirtualBox-based Docker Toolbox
- I installed the MacOS native app Docker for Mac
- which runs the container inside Alpine Linux
    - running on top of a hypervisor layer written by docker
    - running on top of OS X hyperviser interface
- with Docker for Mac, you get only 1 VM, and you don't manage it.
- it is managed by the Docker for Mac application
    - which includes autoupdate for client and server versions.

## using docker

### basic commands

- docker info
- docker version
- docker images
- docker ps

### next

- I went through the [docker for mac](https://docs.docker.com/docker-for-mac/) page.
- it lists projects to pursue, trying out various ways to compose layers together.
- and then I could try the team city experiment as well.
