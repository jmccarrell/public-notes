# tmux notes

- the [tmux tutorial](https://danielmiessler.com/study/tmux/) I used

## session start / stop

- start a tmux session, with a name

        $ tmux new -s session-name

- suspend a session inside it

        C-b d

- list sessions inside tmux

        C-b s

- how to see what is running after ssh

        $ [buildbot@buildbot ~]$ tmux list-clients
        /dev/pts/2: 1 [101x48 xterm-256color] (utf8)

- list active sessions at command line

        [buildbot@buildbot ~]$ tmux list-sessions
        1: 1 windows (created Tue Jun  2 23:38:39 2015) [101x47] (attached)
        bb: 1 windows (created Tue Jun  2 23:46:49 2015) [101x47]

- reattach

        $ tmux a -t session-name

- kill a session


        $ tmux kill-session -t session-name

# tmux and ssh together notes

- [combining ssh and tmux](http://www.bsdnow.tv/tutorials/ssh-tmux)
    - no useful info here at all.

# other tmux configs to follow

- this [search: tmux ssh tutorial](https://www.google.com/search?client=safari&rls=en&q=tmux+ssh+tutorial&ie=UTF-8&oe=UTF-8) shows interesting things to follow

- [maximum-awesome](https://github.com/square/maximum-awesome)
    - looks like some useful tmux goodness there
- more [tmux hints here](https://github.com/adnichols/tmux-and-vim#tmux)
- advice on how to [autostart tmux](http://marklodato.github.io/2013/10/31/autostart-tmux-on-ssh.html)


# jeff key bindings

- remap C-b to C-o

- My initial tmux.conf file

        # use C-o, as the prefix
        set-option -g prefix C-o
        unbind-key C-o
        bind-key C-o send-prefix
        set -g base-index 1

        # Easy config reload
        bind-key R source-file ~/.tmux.conf \; display-message "tmux.conf reloaded."
