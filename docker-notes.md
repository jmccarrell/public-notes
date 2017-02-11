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

# [Docker for Web Developers](http://player.oreilly.com/videos/9781784390679)

- video

## digital ocean setup

- I set up docktest.mccarrell.org
- and I set up iterm login scripts: docktest

### tmux

- I am running a 4 window session, so name the tmux windows
    - w1 .. w4


## first docker container

- install the docker container based on ubuntu LTS:

        root@docktest:~# docker pull ubuntu:14.04
        Pulling repository ubuntu

- then run a shell

        root@docktest:~# docker run -it ubuntu:14.04 bash
        root@f8d092f87041:/#

## vnc viewer

- I have to decide if I am going to set up a VNC viewer.
- Apparently, there is a [good VNC like viewer built into OSX](http://www.davidtheexpert.com/post.php?id=5)
    - `/System/Library/CoreServices/Applications/Screen Sharing.app`
    - try this one.
    - you can put a vnc scheme into Safari, and it will launch screen sharing for you.

## Using Docker

### Working with Images

- list images

        $ docker images
        $ docker images
        REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
        ubuntu              14.04               6d4946999d4f        8 days ago          188.3 MB
        ubuntu              latest              6d4946999d4f        8 days ago          188.3 MB
        <none>              <none>              5efddeffbf5f        5 weeks ago         396 MB
        hello-world         latest              91c95931e552        9 weeks ago         910 B

- think of an image as a class in OO programming terms.  It can generate many instances.

- run the vnc server as a container:

        $ docker run -it imiell/win2048 bash -c '/root/start_vnc.sh && sleep infinity'

- recall that each container instance leaves a trace. See these with:

        $ docker ps -a
        CONTAINER ID        IMAGE                   COMMAND                CREATED             STATUS                       PORTS               NAMES
        9f824797b08c        imiell/win2048:latest   bash -c '/root/start   3 minutes ago       Exited (130) 4 seconds ago                       drunk_albattani
        cdf24a62b21d        imiell/win2048:latest   bash                   6 minutes ago       Exited (0) 3 minutes ago                         romantic_ardinghelli
        b06a741e5fc9        hello-world:latest      /hello                 34 minutes ago      Exited (0) 34 minutes ago                        nostalgic_mclean
        f8d092f87041        ubuntu:14.04            bash                   56 minutes ago      Exited (0) 53 minutes ago                        hungry_tesla

- and clean up a container

        $ docker rm b06a741e5fc9

- many folks confuse containers and image at first, so to separate them use:

        $ docker top <container name>
        $ docker logs <container name>

- docker container leakage -- too many old containers lying around -- is a real issue.
- to delete all old containers, a bit of shell magic:

        $ docker rm -f $(docker ps -aq)

## Sharing with Docker

- it is a good idea to pause a container before commiting it to avoid race conditions.

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
