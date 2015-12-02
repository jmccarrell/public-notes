# tmux notes

- the [tmux tutorial](https://danielmiessler.com/study/tmux/) I used
    - the [shortcut key references](https://danielmiessler.com/study/tmux/#reference) there are useful

## Jeffs customizations

- I re-bind the default `C-b` to `C-q`, so everywhere I have my dotiles, it is `C-q`



## session management

- think of sessions as a top-level thing, like
    - leafcutter
    - api work

- from the server that you will be re-connecting to:
- start a tmux session, with a name

        $ tmux new -s session-name

- suspend a session inside it

        C-q d

- list sessions inside tmux

        C-q s

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

- remap C-b to C-q

- My initial tmux.conf file

        # use C-q, as the prefix
        set-option -g prefix C-q
        unbind-key C-q
        bind-key C-q send-prefix
        set -g base-index 1

        # Easy config reload
        bind-key R source-file ~/.tmux.conf \; display-message "tmux.conf reloaded."

## window work

### split windows

- split window horizontally:  `C-q "`
    - like `C-x 4 b` in emacs
    - bind-key          " split-window

- split window vertically:   `C-q %`
    - Split the current pane into two, left and right.
    - like `C-x 3 b` in emacs
    - bind-key          % split-window -h

### restore to a single pane

- break-pane  `C-q !`
    - Break the current pane out of the window.
    - sort of like `C-x 1` in emacs, but splits the pane out into a new window like `C-x 5`

- next layout:  `C-q space`
    - bind-key      Space next-layout
    - cycles through some interesting window layouts; seems useful

## windows and panes

- there are both windows and panes

... Each session has one or more windows linked into it.  Windows may be linked to multiple sessions and are made up of one or more panes, each of which contains a pseudo terminal.

... the current pane may be changed with the select-pane command and the rotate-window and swap-pane commands may be used to swap panes without changing their position.  Panes are numbered beginning from zero in the order they are created.

- How do I see the current window and pane in the status bar?
    - A: `C-q i`: display some info

           i           Display some information about the current window.

- how do I switch between windows?
    - A: prev / next windows:

           l           Move to the previously selected window.
           n           Change to the next window.
           p           Change to the previous window.

    - is l and p the same thing?  I guess not

- how do I switch between panes in a window?
    - A: `C-q o`

           o           Select the next pane in the current window.

- how do I make a new pane?
    - A: split an existing one, either:
        - into top and bottom (preferred): `C-q "`
        - into left and right: `C-q %`


## default bindings (tmux 2.1)


           C-b         Send the prefix key (C-b) through to the application.
           C-o         Rotate the panes in the current window forwards.
           C-z         Suspend the tmux client.
           !           Break the current pane out of the window.
           "           Split the current pane into two, top and bottom.
           #           List all paste buffers.
           $           Rename the current session.
           %           Split the current pane into two, left and right.
           &           Kill the current window.
           '           Prompt for a window index to select.
           (           Switch the attached client to the previous session.
           )           Switch the attached client to the next session.
           ,           Rename the current window.
           -           Delete the most recently copied buffer of text.
           .           Prompt for an index to move the current window.
           0 to 9      Select windows 0 to 9.
           :           Enter the tmux command prompt.
           ;           Move to the previously active pane.
           =           Choose which buffer to paste interactively from a list.
           ?           List all key bindings.
           D           Choose a client to detach.
           L           Switch the attached client back to the last session.
           [           Enter copy mode to copy text or view the history.
           ]           Paste the most recently copied buffer of text.
           c           Create a new window.
           d           Detach the current client.
           f           Prompt to search for text in open windows.
           i           Display some information about the current window.
           l           Move to the previously selected window.
           n           Change to the next window.
           o           Select the next pane in the current window.
           p           Change to the previous window.
           q           Briefly display pane indexes.
           r           Force redraw of the attached client.
           m           Mark the current pane (see select-pane -m).
           M           Clear the marked pane.
           s           Select a new session for the attached client interactively.
           t           Show the time.
           w           Choose the current window interactively.
           x           Kill the current pane.
           z           Toggle zoom state of the current pane.
           {           Swap the current pane with the previous pane.
           }           Swap the current pane with the next pane.
           ~           Show previous messages from tmux, if any.
           Page Up     Enter copy mode and scroll one page up.
           Up, Down
           Left, Right
                       Change to the pane above, below, to the left, or to the right of the current pane.
           M-1 to M-5  Arrange panes in one of the five preset layouts: even-horizontal, even-vertical, main-horizon-
                       tal, main-vertical, or tiled.
           Space       Arrange the current window in the next preset layout.
           M-n         Move to the next window with a bell or activity marker.
           M-o         Rotate the panes in the current window backwards.
           M-p         Move to the previous window with a bell or activity marker.
           C-Up, C-Down
           C-Left, C-Right
                       Resize the current pane in steps of one cell.
           M-Up, M-Down
           M-Left, M-Right
                       Resize the current pane in steps of five cells.

## key bindings for emacs-edit

    bind-key -t emacs-edit    C-a start-of-line
    bind-key -t emacs-edit    C-b cursor-left
    bind-key -t emacs-edit    C-c cancel
    bind-key -t emacs-edit    C-d delete
    bind-key -t emacs-edit    C-e end-of-line
    bind-key -t emacs-edit    C-f cursor-right
    bind-key -t emacs-edit    C-h backspace
    bind-key -t emacs-edit    Tab complete
    bind-key -t emacs-edit    C-j enter
    bind-key -t emacs-edit    C-k delete-end-of-line
    bind-key -t emacs-edit  Enter enter
    bind-key -t emacs-edit    C-n history-down
    bind-key -t emacs-edit    C-p history-up
    bind-key -t emacs-edit    C-t transpose-chars
    bind-key -t emacs-edit    C-u delete-line
    bind-key -t emacs-edit    C-w delete-word
    bind-key -t emacs-edit    C-y paste
    bind-key -t emacs-edit Escape cancel
    bind-key -t emacs-edit BSpace backspace
    bind-key -t emacs-edit     DC delete
    bind-key -t emacs-edit   Home start-of-line
    bind-key -t emacs-edit    End end-of-line
    bind-key -t emacs-edit     Up history-up
    bind-key -t emacs-edit   Down history-down
    bind-key -t emacs-edit   Left cursor-left
    bind-key -t emacs-edit  Right cursor-right
    bind-key -t emacs-edit    M-b previous-word
    bind-key -t emacs-edit    M-f next-word-end
    bind-key -t emacs-edit    M-m start-of-line

## key bindings for emacs-choice

    bind-key -t emacs-choice            C-c cancel
    bind-key -t emacs-choice            C-j choose
    bind-key -t emacs-choice          Enter choose
    bind-key -t emacs-choice            C-n down
    bind-key -t emacs-choice            C-p up
    bind-key -t emacs-choice            C-v page-down
    bind-key -t emacs-choice         Escape cancel
    bind-key -t emacs-choice          Space tree-toggle
    bind-key -t emacs-choice              q cancel
    bind-key -t emacs-choice MouseDown1Pane choose
    bind-key -t emacs-choice MouseDown3Pane tree-toggle
    bind-key -t emacs-choice    WheelUpPane up
    bind-key -t emacs-choice  WheelDownPane down
    bind-key -t emacs-choice         BSpace backspace
    bind-key -t emacs-choice           Home start-of-list
    bind-key -t emacs-choice            End end-of-list
    bind-key -t emacs-choice          NPage page-down
    bind-key -t emacs-choice          PPage page-up
    bind-key -t emacs-choice             Up up
    bind-key -t emacs-choice           Down down
    bind-key -t emacs-choice           Left tree-collapse
    bind-key -t emacs-choice          Right tree-expand
    bind-key -t emacs-choice            M-0 start-number-prefix
    bind-key -t emacs-choice            M-1 start-number-prefix
    bind-key -t emacs-choice            M-2 start-number-prefix
    bind-key -t emacs-choice            M-3 start-number-prefix
    bind-key -t emacs-choice            M-4 start-number-prefix
    bind-key -t emacs-choice            M-5 start-number-prefix
    bind-key -t emacs-choice            M-6 start-number-prefix
    bind-key -t emacs-choice            M-7 start-number-prefix
    bind-key -t emacs-choice            M-8 start-number-prefix
    bind-key -t emacs-choice            M-9 start-number-prefix
    bind-key -t emacs-choice            M-< start-of-list
    bind-key -t emacs-choice            M-> end-of-list
    bind-key -t emacs-choice            M-R top-line
    bind-key -t emacs-choice            M-v page-up
    bind-key -t emacs-choice           C-Up scroll-up
    bind-key -t emacs-choice         C-Down scroll-down
    bind-key -t emacs-choice         C-Left tree-collapse-all
    bind-key -t emacs-choice        C-Right tree-expand-all

## key bindings for emacs-copy

    bind-key -t emacs-copy        C-Space begin-selection
    bind-key -t emacs-copy            C-a start-of-line
    bind-key -t emacs-copy            C-b cursor-left
    bind-key -t emacs-copy            C-c cancel
    bind-key -t emacs-copy            C-e end-of-line
    bind-key -t emacs-copy            C-f cursor-right
    bind-key -t emacs-copy            C-g clear-selection
    bind-key -t emacs-copy            C-k copy-end-of-line
    bind-key -t emacs-copy            C-n cursor-down
    bind-key -t emacs-copy            C-p cursor-up
    bind-key -t emacs-copy            C-r search-backward
    bind-key -t emacs-copy            C-s search-forward
    bind-key -t emacs-copy            C-v page-down
    bind-key -t emacs-copy            C-w copy-selection
    bind-key -t emacs-copy         Escape cancel
    bind-key -t emacs-copy          Space page-down
    bind-key -t emacs-copy              , jump-reverse
    bind-key -t emacs-copy              ; jump-again
    bind-key -t emacs-copy              F jump-backward
    bind-key -t emacs-copy              N search-reverse
    bind-key -t emacs-copy              R rectangle-toggle
    bind-key -t emacs-copy              T jump-to-backward
    bind-key -t emacs-copy              f jump-forward
    bind-key -t emacs-copy              g goto-line
    bind-key -t emacs-copy              n search-again
    bind-key -t emacs-copy              q cancel
    bind-key -t emacs-copy              t jump-to-forward
    bind-key -t emacs-copy MouseDrag1Pane begin-selection
    bind-key -t emacs-copy    WheelUpPane scroll-up
    bind-key -t emacs-copy  WheelDownPane scroll-down
    bind-key -t emacs-copy          NPage page-down
    bind-key -t emacs-copy          PPage page-up
    bind-key -t emacs-copy             Up cursor-up
    bind-key -t emacs-copy           Down cursor-down
    bind-key -t emacs-copy           Left cursor-left
    bind-key -t emacs-copy          Right cursor-right
    bind-key -t emacs-copy            M-1 start-number-prefix
    bind-key -t emacs-copy            M-2 start-number-prefix
    bind-key -t emacs-copy            M-3 start-number-prefix
    bind-key -t emacs-copy            M-4 start-number-prefix
    bind-key -t emacs-copy            M-5 start-number-prefix
    bind-key -t emacs-copy            M-6 start-number-prefix
    bind-key -t emacs-copy            M-7 start-number-prefix
    bind-key -t emacs-copy            M-8 start-number-prefix
    bind-key -t emacs-copy            M-9 start-number-prefix
    bind-key -t emacs-copy            M-< history-top
    bind-key -t emacs-copy            M-> history-bottom
    bind-key -t emacs-copy            M-R top-line
    bind-key -t emacs-copy            M-b previous-word
    bind-key -t emacs-copy            M-f next-word-end
    bind-key -t emacs-copy            M-m back-to-indentation
    bind-key -t emacs-copy            M-r middle-line
    bind-key -t emacs-copy            M-v page-up
    bind-key -t emacs-copy            M-w copy-selection
    bind-key -t emacs-copy           M-Up halfpage-up
    bind-key -t emacs-copy         M-Down halfpage-down
    bind-key -t emacs-copy           C-Up scroll-up
    bind-key -t emacs-copy         C-Down scroll-down

- Do any of my tutorials listed about talk about the copy buffer and how to use it?
