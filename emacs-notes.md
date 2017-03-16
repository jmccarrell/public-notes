## registers ##

registers in emacs:

- `C-x r <SPC> R`
  - Save position of point in register R (point-to-register).

- `C-x r j R`
  - Jump to the position saved in register R (jump-to-register).

- `C-x r s R`
  - Copy region into register R (copy-to-register).

- `C-x r i R`
  - Insert text from register R (insert-register).

- `M-x append-to-register <RET> R`
  - Append region to text in register R.

- `M-x prepend-to-register <RET> R`
  - Prepend region to text in register R.

- `C-x r r R`
  - Copy the region-rectangle into register R
   (copy-rectangle-to-register).  With numeric argument, delete it
   as well.

- `C-x r i R`
  - Insert the rectangle stored in register R (if it contains a
   rectangle) (insert-register).

jwm: follow this reference when you have a minute:

> See also the command sort-columns, which you can think of as sorting a rectangle.  *Note Sorting::.

read about bookmarks

columns of numbers

----

## directory-local-variables ##

- I found an interesting [reference to directory-local-variables](http://atomized.org/2009/05/emacs-23-easier-directory-local-variables/)
  - it could be a solution to my per-directory formatting needs.

## php-mode ##

set up php-mode (and any other local vars desired) in php files:

    // Local Variables:
    // mode: php;
    // tab-width: 4;
    // End:

this is documented in the emacs manual under the heading: 'Local Variables in Files'

Here is more context on Local Variables:

> There are two ways to specify file local variable values: in the first line, or with a
  local variables list.  Here's how to specify them in the first line:

     -*- mode: MODENAME; VAR: VALUE; ... -*-

> You can specify any number of variable/value pairs in this way, each pair with a colon
  and semicolon as shown above.  The special variable/value pair `mode: MODENAME;', if
  present, specifies a major or minor mode; if you use this to specify a major mode, it
  should come first in the line.  The VALUEs are used literally, and not evaluated.

> You can use the command `add-file-local-variable-prop-line' instead of adding entries
  by hand.  It prompts for a variable and value, and adds them to the first line in the
  appropriate way.  The command `delete-file-local-variable-prop-line' deletes a variable
  from the line.  The command `copy-dir-locals-to-file-locals-prop-line' copies
  directory-local variables (*note Directory Variables::) to the first line.

> Here is an example first line that specifies Lisp mode and sets two variables with
  numeric values:

     ;; -*- mode: Lisp; fill-column: 75; comment-column: 50; -*-

----

## recursive edit ##

when in recursive edit, with the [[ ]] on the mode line,

    C-[   abort-recursive-edit

will get out of it.

----

## mysql in emacs ##

use

    sql-help

to read about sql mode.

Start a connection to mysql with:

    sql-mysql

In another buffer, run

    sql-mode

Then useful commands can be found in the SQL menu, like:

    C-c C-c     Send-paragraph
    C-c C-r     Send-region

----

## outline mode ##

outline-minor-mode is typically what I would use for txt files with a file local variable:

    mode: outline-minor

View an outline in 2 or more different views:

You can display two views of a single outline at the same time, in
different windows.  To do this, you must create an indirect buffer using
`M-x make-indirect-buffer'.  The first argument of this command is the
existing outline buffer name, and its second argument is the name to
use for the new indirect buffer.


In outline-minor mode, all outline commands are on prefix: C-c @,
so every command below is at, e.g.,  'C-c @ C-n' instead of 'C-c C-n'

Outline Motion Commands:

- `C-c C-n`
  - Move point to the next visible heading line

- `C-c C-p`
  - Move point to the previous visible heading line

- ``C-c C-f``
  - Move point to the next visible heading line at the same level as
    the one point is on.

- ``C-c C-b``
  - Move point to the previous visible heading line at the same level.

- ``C-c C-u``
  - Move point up to a lower-level (more inclusive) visible heading line.

### outline visibility commands ###

- ``C-c C-c``
  - Make the current heading line's body invisible.

- ``C-c C-e``
  - Make the current heading line's body visible.

- ``C-c C-d``
  - Make everything under the current heading invisible, not including
   the heading itself.

- ``C-c C-s``
  - Make everything under the current heading visible, including body,
    subheadings, and their bodies.

- ``C-c C-l``
  - Make the body of the current heading line, and of all its
    subheadings, invisible.

- ``C-c C-k``
  - Make all subheadings of the current heading line, at all levels,
    visible.

- ``C-c C-i``
  - Make immediate subheadings (one level down) of the current heading
    line visible.

- ``C-c C-t``
  - Make all body lines in the buffer invisible.

- ``C-c C-a``
  - Make all lines in the buffer visible.

- ``C-c C-q``
  - Hide everything except the top N levels of heading lines.

- ``C-c C-o``
  - Hide everything except for the heading or body that point is in,
    plus the headings leading up from there to the top level of the
    outline.

How does searching work in the context of hidden outline elements?
From the emacs manual:

> When incremental search finds text that is hidden by Outline mode, it makes that part of the buffer visible.  If you exit the search at that position, the text remains visible.  You can also automatically

----

File local variables can be specified at the top of a file one 1 line:

     -*- mode: MODENAME; VAR: VALUE; ... -*-

or at the bottom with 3,000 chars of EOF in the form:
Any prefix/suffix is allowed around 'Local Variables:';
emacs strips those from the rest of the section

     /* Local Variables: */
     /* mode:c           */
     /* comment-column:0 */
     /* End:             */

----

## font size increase/decrease ##

The functions

        text-scale-increase             C-x  C-+
                   decrease             C-x  C--
                   set

can be used to change the font size of the current buffer.
Very useful.

----

## comint mode ##

emacs notes to drill down on:

        from lisp/progmodes/sql.el

        ;; For documentation on the functionality provided by comint mode, and
        ;; the hooks available for customizing it, see the file `comint.el`.

        ;; Hint for newbies: take a look at `dabbrev-expand`, `abbrev-mode`, and
        ;; `imenu-add-menubar-index`.

----

## solarized emacs ##

- many variants; standardize on bbatsov:

- [solarized theme](https://github.com/bbatsov/solarized-emacs) available as a package loaded by a package manager
  - works from emacs 24 on.
  - some support for emacs 23.
  - recommends [MELPA](http://melpa.org/) emacs package manager

### no, older prefer bbatsov ###

- [code and instructions](https://github.com/sellout/emacs-color-theme-solarized) from github

### precursor ##

- I want my emacs library files brought along in my environment so I can have a
  consistent env.  These files:
  - c-m-supl.el
  - jc_ctags.el
  - jc_misc.el
  - p4.el
  - ps-ccrypt.el
  - yaml-mode.el

- so the first question is: can I use  `$HOME/.emacs.d` provisioned under jwm-dotfiles
  for this purpose?

----

## Other packages I want ##

- editorconfig
  - there is an editorconfig package available in MELPA.

- yaml-mode
  - yes, available on MELPA

----

- discover the idiomatic usage of multiple emacs packages
  - how does this work?
  - gnu ELPA vs MELPA vs Marmalade
- could I write a ansible playbook to update my emacs environment on a given machine?
  - what would that look like?

----

**Fri Jun 26 16:04:40 PDT 2015**


- Jack Repenning doesn't use any of the package managers.

- I guess the next thing to do is to explore the mechanisms:

  - will ~/.emacs.d/elisp
    be searched and autoloaded?

  - try installing and using yaml-mode via melpa.  What does it look like?

## √ el-get ##

- looks like [el-get](http://www.emacswiki.org/emacs/el-get) is the equivalent
  to apt-get for emacs packages

- the [lazy installer](https://github.com/dimitri/el-get#the-lazy-installer)

- Ok, then I did

        M-x el-get-install solarized-emacs

so I guess it is there now.  How to turn [solarized-emacs](https://github.com/bbatsov/solarized-emacs) on or off?

        M-x load-theme <solarized-{dark,light}>

- where does el-get put the packages it downloads?
  - A: `~/.emacs.d/el-get/<package-name>`

- el-get [recommends](https://github.com/dimitri/el-get#package-setup) customizing a given package by putting the customization code into
  `init-<package-name>.el` in the directory named by `el-get-user-package-directory`,
  which has to be given a value.

## √ solarized ##

- I like solarized-dark

### next steps ##

- leave .emacs.d to emacs for transitory things.
- put Jeffs emacs stuff into .emacs-jwm.d
  - version control this in jwm-dotfiles
  - put my customizations to packages in there
  - convert my font and color settings in .emacs to a theme
  - .emacs-jwm.d/themes
  - follow [the conventions](https://github.com/bbatsov/solarized-emacs#stand-alone-manual-installation)

----

- Investigate auto-highlight-mode as a productivity enhancer:
  - c.f.: [rainbow identifiers solarized issue](https://github.com/bbatsov/solarized-emacs/issues/133) about comment 5 or so

  - emacswiki [Highlight Symbol](http://www.emacswiki.org/emacs/HighlightSymbol)
  - how do I get el-get to tell me if it knows how to install HighlightSymbol?

  highlight-symbol      available  Quickly highlight a symbol throughout the buffer and cycle through its locations.


----

## elisp references ##

- Steve Yegge has written his [emergency elisp](http://steve-yegge.blogspot.com/2008/01/emergency-elisp.html) blog entry
  - it is written for programmers who don't know elisp.  good stuff.  Coverge includes:
  - lexical stuff
  - operators
  - statements
  - classes
  - with some nice elisp / java side by side comparisons

----

## use solarized foreground and background colors ##

- NO SEE BELOW change references from ~ to $HOME so I can use the
  - HOME=/j/proj/jwm-dotfiles emacs -i $HOME/.emacs
  - convention to ease testing of color changes
  - yes, but that has the effect of creating a whole new
    - /j//proj/jwm-dotfiles/.emacs.d
  - populated by el-get
  - which I do not want ever revision controlled.
  - so abandon this idea.
- √ drop support for emacs-21 and 22 in my customization functions
- √ merge solarized foreground and background colors into my standard frame definition.

----

## better find-files ##

- [Emacs: find files anywhere, updated for 2016](http://amitp.blogspot.com/2016/07/emacs-find-files-anywhere.html)

## utf 8 / unicode ##

- one of the main pages for international characters is in the emacs manual: [22 International Character Support](http://www.gnu.org/software/emacs/manual/html_node/emacs/International.html#International)


It looks like C-x 8 is bound to a number of interesting unicode characters, as part of of iso-international mode, but it also appears to be very Latin-1 specific.

There is an input-method called rfc1345, which follows the RFC.  [RFC 1345](https://tools.ietf.org/pdf/rfc1345.pdf) defines `RT` to produce the square root symbol that I am using for my check mark.

So one officially sanctioned way to get a square root symbol into any buffer are the 4 characters:

C-\ &RT

then another C-\ to get back out of the rfc 1345 input method.

another interesting character is infinity: 00.  So

C-\ &00

creates ∞

I can also do this with the insert-character function.

But the final answer I arrived at was to disable option as a meta character in my .emacs

(when (and window-system (eq 'ns window-system))
  (set-variable (quote mac-option-modifier) 'none))

Then option-v produces my desired square root character.

----

I want to prefer utf-8 in all cases so add to my init file:

;; prefer utf-8 encoding in all cases.
(prefer-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)

----

**Thu Nov 10 13:02:11 PST 2016**

## emacs package managers again ##

- I started with [el-get](http://www.emacswiki.org/emacs/el-get)
- but I had problems install magit via el-get.
- so throw out el-get, and fall back to MELPA.
- what is the model post-installation to keep packages up to date?
- A: manually:

> After running package-list-packages, type U (mark Upgradable packages) and then x (eXecute the installs and deletions). When it’s done installing all the packages it will ask if you want to delete the obsolete packages and so you can hit y (Yes).

## magit ##

- support for magit added.

## xterm-color ##

- move to the MELPA packaged version of xterm-color from my private version.

```
M-x package-list-packages
<search> xterm-color
i
x
```

- √ then nuke xterm-color from my repo

**Fri Nov 11 11:08:24 PST 2016**

## path inside emacs ##

- as I frequently change virtual envs, the PATH of the shell changes
- but emacs retains the PATH from when it was started.
- to see the current path, eval:

```lisp
(getenv "PATH")
"/c/davo/tmp/venvs/auto_filer/bin:/Users/jeff/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin:/opt/homebrew-cask/Caskroom/emacs/24.5-1/Emacs.app/Contents/MacOS/bin-x86_64-10_9:/opt/homebrew-cask/Caskroom/emacs/24.5-1/Emacs.app/Contents/MacOS/libexec-x86_64-10_9"
```

- looks like there is a package [exec-path-from-shell](https://github.com/purcell/exec-path-from-shell) to help with this specific issue.
- so try it.
- load it from melpa

- but that has the opposite effect, as when it evals the shell, the shell doesn't know about the virtualenv, so it resets the emacs path like so:

```lisp
(when (memq window-system '(mac ns))
  (exec-path-from-shell-initialize))
(("MANPATH" . "/usr/local/opt/coreutils/libexec/gnuman:/usr/share/man:/usr/local/share/man:/Library/TeX/Distributions/.DefaultTeX/Contents/Man:/usr/local/opt/coreutils/libexec/gnuman") ("PATH" . "/Users/jeff/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin"))
```

- so keep looking
- found [pyvenv](https://github.com/jorgenschaefer/pyvenv), available via melpa
- seems to do just what I want, via `pyvenv-activate`

- M-x pyvenv-activate /c/davo/tmp/venvs/autofiler

```lisp
(getenv "PATH")
"/c/davo/tmp/venvs/auto_filer/bin:/Users/jeff/bin/:/usr/local/bin/:/usr/bin/:/bin/:/usr/sbin/:/sbin/:/opt/X11/bin/:/Library/TeX/texbin/:/opt/homebrew-cask/Caskroom/emacs/24.5-1/Emacs.app/Contents/MacOS/libexec/"
```

- does the right thing.  Problem solved.

**Thu Feb  9 07:54:09 PST 2017**

- I need to update my emacs env quite a bit.
  - make a list of common markdown mode key bindings I am likely to need:
    - [follow link](http://www.example.com/)
  - configure a markdown previewer from
    - OSX: Marked2
    - ubuntu: Multimarkdown?
  - re-read this notes file; I have trod some of this ground before
  - consider enabling diff3 mode by default for git
    - to enable smerge in emacs
    - drill into this more.
  - LARGELY DONE yasnippet
  - IN PROGESS markdown-mode or github flavored markdown gfm-mode
  - IN PROGRESS I need a minor shell mode that works with my colorization
  - improve the dynamism of setting the font-size
    - certainly read about setting the font size interactively
    - and having that propogate to new frames
  - bind keys to anticipate coming esc key moving to the whatever bar on mac laptops
  - make bindings to insert common unicode chars I use:
    - √
    - λ
  - insert a date stamp in markdown format on a key binding
    - when in markdown-mode or gfm-mode, make it bold?

## yasnippet ##

- remaining: evaluate existing snippet packages
  - for python
- decide how to patition my snippets among the supported packages
  - or if this is even easily supported

- IN PROGRESS set up yasnippet for quoting haskell in markdown
  - √ so yasnippet is turned on by default
  - sync through to orion
  - worry about shared snippets later
- √ devolve to: identify a markdown mode
  - choose markdown-mode, along with gfm-mode for github flavored markdown

## xterm-color ##

- I need to configure this.
- it would be great to get emacs to treat /j/proj/jwm-dotfiles as HOME for the purpose of evaluating new emacs configs.

jeff at vega in /j/proj/jwm-dotfiles on jwm-dotfiles
$ HOME=$(PWD) emacs -nw

fails trying to load magit

- Ok, initally seems to work for some things
- push yasnippet through bitbucket
- push through bitbucket to orion
- see if I get the (B in the bash prompt over there without the iterm2 specializations
  - yes, I do see the (B on orion
- based on the xterm color tests (perl tests/xterm-colortest && perl tests/256colors2.pl)
  - it looks like the (B issue is with my prompt, not with the xterm color package.
  - although it is curious why bash on both linux and os x don't have the issue while emacs does.

- interesting that in bash:

```
$ echo $PS1
\[\033]0;\W\007\]\[\]\[\]\u\[\] at \[\]\h\[\] in \[\]\w$(prompt_git "\[\] on \[\]" "\[\]")\n\[\]$ \[\]
```

- while in shell-mode:

```
$ (Becho $PS1
\[\033]0;\W\007\]\[\]\[\]\u\[\] at \[\]\h\[\] in \[\]\w$(prompt_git "\[\] on \[\]" "\[\]")\n\[\]$ \[(B\]
```

- so there is the (B at the end

----

**Wed Feb 22 11:48:09 PST 2017**

- I tried to use `(exec-path-from-shell-initialize)` on ubuntu LTS.
  - did it work?  A: No, it did not.

**Fri Feb 24 19:09:23 PST 2017**

## helm ##

- turn on helm mode.
- for find files:
  - C-x c C-x C-f
- likewise for list buffers:
  - C-x c C-x C-b
- explore helm-locate
  - C-x c l
  - which requires locate to be working on the mac
  - explored in mac-os-notes
  - locate is building the db now.
- so I have the basics.

- √ consider fixing the face choices used by helm; not so good with solarized.

## solarized ##

- which led me to an investigation of how to simply use the 2 variants of solarized:
- which led me to [this advice to](http://stackoverflow.com/questions/9840558/why-cant-emacs-24-find-a-custom-theme-i-added) auto load any installed themes into the emacs `custom-theme-load-path`
  - which refers to in ~/emacs.d/init.el
  - so check that out.
    - it doesn't exist in my config.
    - so add the snippet to ~/.emacs
- looks like this is working pretty ok.

## todo ##

- investigate my-packages
  - I saw a defvar in someones init.el to describe the packages they use
- investigate use-package
  - author talk on youtube: [Emacs package highlight: use-package](https://www.youtube.com/watch?v=2TSKxxYEbII)
- explore `C-x $` set-selective display
  - super useful for code narrowing; start using this immediately

## search for better emacs patterns ##

- notes from listening to youtube: [Editor of a lifetime](https://www.youtube.com/watch?v=VADudzQGvU8)
  - none; this was not a useful talk to me; just about why emacs overview, not details of how to use it well.

### emacculate ###

- I like these guys; they explain how they have leveraged emacs pretty well.

## `use-package` ##

- 30 minute talk by the author:
  - [Emacs package highlight: use-package](https://www.youtube.com/watch?v=2TSKxxYEbII)
  - part of youtube channel by Sacha Chua
- source [github](https://github.com/jwiegley/use-package)
- Author John Wiegley

### Philosophy ###

- `use-package` philosophy
  - be targeted and specific
  - have a declaration that is going to work
  - or, essentially do nothing on every machine where you use it
    - could be: report a useful error and continue

### Notes ###

- the author really likes a package to expand and show macros, which is what use-package largely is.
  - macrostep
- which he uses like this:

```elisp
(use-package macrostep
  :load-path "site-lisp/macrostep"
  :bind ("C-c e m" . macrostep-expand))
```

- the author also really likes `ggtags`
  - which is an interface to the [gnu global](https://www.gnu.org/software/global/) next gen etags system

----

- `:disabled t` looks particularly useful to me to try things out

### ensure ###

- the author does not use ensure, nor package managers
- he prefers to manually install every package so he can manage his emacs startup time
- he stated he has his personal emacs load time down to < 1/3 second

### describe-personal-keybindings ###

- for users of the use-package system, there is a key board command referenced in this talk about 16:08 in
- that shows the current key bindings *and* what you may have overriddenn; what is now hidden.
  - it looks super useful to me as I refine my emacs usage.
  - `describe-personal-keybindings`
- so this is specific to `use-package`

- about 17:00 in is where we can see John's personal key bindings, which could be useful to compare.
  - eg, he binds C-z to delete-other-windows, like C-x 0
  - no more suspend-emacs

- explore the `bind:` capabilities of `use-package`

### init vs config ###

- init happens before the require
- config happens after the require
- preface will happen when the use-pacakge macro is evaluated, and when it is byte compiled.

----

## silver searcher ##

- [the_silver_searcher](https://github.com/ggreer/the_silver_searcher)
- an ack replacement that knows about about .gitignore
  - and .ignore
    - it specifically mentions .min.js
- runs much faster as well
- there is ag.el
  - and helm ag
  - and John Wiegleys startup file shows how to configure them with use-package
    - about 21:58 into the use-package video
- looks like a winner to me.

## erc ##

- emacs IRC internet relay chat client

# upate emacs env #

## scoping ##

**Sat Feb 25 16:48:18 PST 2017**

- consider changing emacs env to improve productivity
  - goals
    - leverage helm-ag to search file repositories more effectively
    - get to using org-mode instead of markdown for authoring my notes and especially for executing code.

- which one is more important?  A: helm-ag

- model my target env after John Wiegleys

- look into [ibuffer save filter groups](https://github.com/jwiegley/dot-emacs/blob/master/settings.el#L703)
  - [ibuffer mode](https://github.com/jwiegley/dot-emacs/blob/master/init.el#L2558)
- look into [recentf](https://github.com/jwiegley/dot-emacs/blob/master/settings.el#L886)
- look into [smart compile alist](https://github.com/jwiegley/dot-emacs/blob/master/settings.el#L987)
- look into helm swoop youtube
- look into [hippie / dabbrev](https://github.com/jwiegley/dot-emacs/blob/master/init.el#L2323)

- use settings.el for custom settings:

 '(custom-file "~/.emacs.d/settings.el")
 '(fill-column 78)
 '(global-font-lock-mode t nil (font-lock))

 '(indent-tabs-mode nil)
;;; needs to be my user name
 '(inhibit-startup-echo-area-message "johnw")
 '(inhibit-startup-screen t)
 '(initial-major-mode (quote fundamental-mode))

 '(kill-do-not-save-duplicates t)
 '(kill-whole-line t)
 '(large-file-warning-threshold nil)

 '(markdown-command "pandoc -f markdown_mmd -S")
 '(markdown-command-needs-filename t)
 '(markdown-enable-math t)
 '(markdown-open-command "open-markdown")

 '(menu-bar-mode nil)

 '(package-archives
(quote
 (("gnu" . "https://elpa.gnu.org/packages/")
  ("MELPA" . "https://melpa.org/packages/")
  ("Marmalade" . "https://marmalade-repo.org/packages/"))))

 '(regex-tool-backend (quote perl))

 '(user-full-name "John Wiegley")
 '(user-initials "jww")
 '(user-mail-address "johnw@newartisans.com")

 '(whitespace-auto-cleanup t t)
 '(whitespace-line-column 110)
 '(whitespace-rescan-timer-time nil t)
 '(whitespace-silent t t)
 '(whitespace-style (quote (face trailing lines space-before-tab empty)))

- [just one space](https://github.com/jwiegley/dot-emacs/blob/master/init.el#L420)
- [hack font](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=font+Hack-normal-normal-normal-*-14-*-*-*-m-0-iso10646-1&*)
- how John deals with [variable size frames](https://github.com/jwiegley/dot-emacs/blob/master/init.el#L487)

- an [example of binding his own keymap](https://github.com/jwiegley/dot-emacs/blob/master/init.el#L462)
- explore ffap: find-file-at-point
  - johns binding: (bind-key "C-c v" #'ffap)

- packages to consider
  - compile
  - css
  - csv
  - diff-mode
  - diff-view
  - diminish
  - docker
    - dockerfile-mode
  - dr-racket-like-unicode
  - ediff
  - etags
  - flyspell
  - graphviz-dot-mode
  - grep
  - helm-config
  - helm-grep
  - helm-make
  - helm-swoop
  - hi-lock
  - hilit-chg
  - iedit
  - iflipb
  - isearch
  - json-mode
  - lusty-explorer
  - macrostep
  - magit
  - markdown-mode
  - mule
    - configure utf8 stuff here?
  - multiterm
    - maybe; jww uses screen, not tmux
  - nxml-mode
    - example of calling tidy on the buffer here
  - outline
  - pabbrev
  - paredit
    - minor mode for parens
    - check this out.
  - mic-paren or paren
  - projectile
    - maybe: check this one out
  - python-mode
  - recentf?
  - regex-tool
  - restclient
  - rubymode
  - selected
  - session
    - sounds useful, but last updated in 2012?
  - sh-{script,toggle} ?
    - I can't find these in melpa
  - smart compile
    - disabled by jww
  - smart-tabs-mode
  - smerge-mode?
  - sort-words
  - swiper-helm
  - tiny?  maybe
    - Quickly generate linear ranges in Emacs
  - tramp-sh
    - including integration with docker containers
  - transpose-mark?
    - seems pretty specialized
  - vdiff
    - another diff mode akin to ediff
  - visual regexp
  - vkill
  - whitespace
  - winner
  - workgroups?
    - or maybe workgroups2
    - not clear what this provides
  - wrap-region
  - yaml-mode
  - yasnippet
  - zencoding-mode?
    - maybe; low priority
  - ztree-diff

## implementation ##

### questions to answer ###

- what is in ~/.emacs.d now?
  - A: just emacs side effects dirs and files
- where will my elisp go?
  - now in `~/.emacs.jwm.d/elisp/`
  - move to `~/.emacs.d/jwm-elisp`
- will I create a separate repo just for emacs?
  - A: yes.  stored on github
- keep el-get?
  - probably not; do whatever jww is doing here
- how will I manage the transition?
  - create a new repo in parallel to jwm-dotfiles
  - then I can push with jwm-dotfiles to re-create my old config
    - or rm the old emacs config with a shell script?

### todo ###

- √ I have to untangle my .emacs-jwm.d
- I want C-x C-e to only run compile in certain modes; not globally
  - C-x C-e to evaluate an sexpr in lisp mode is particularly useful.

### exploration ###

- the first thing I need to know is: will use-package require a compile step?
  - are the .elc files checked into jww's git repo?  A: no.
  - My guess is no: the simplest invocation is: `(use-package foo)`
- read the docs: [use-package](https://github.com/jwiegley/use-package)

- the emacculate guys have a template to get started with.
  - [the template](https://github.com/durantschoon/.emacs.d/tree/boilerplate-sane-defaults_v1.0)
- switch from .emacs to emacs.d/init.el

### transition plan ###

- I need a way to move back and forth between old style and new style

#### move to new style ####

- presume there is a repo in bitbucket: jmccarrell/.emacs.d
- start from the template

```
if [ ! -e ~/tmp/emacs.d ] ; then
  mv ~/.emacs.d ~/tmp/emacs.d
fi
if [ ! -f ~/tmp/dot-emacs ] ; then
  mv ~/.emacs ~/tmp/dot-emacs
fi

git clone path-to-repo ~/.emacs.d
```

#### move back to old style ####

- check to make sure there are no unsaved changes in ~/.emacs.d
- rm -rf ~/.emacs.d
- mv ~/tmp/emacs.d ~/.emacs.d
- mv ~/tmp/dot-emacs ~/.emacs

## start conversion ##

- decide what to call the repo
  - .emacs.d
  - √ dot-emacs

- so can they coexist?
- what if I just mv aside .emacs, so .emacs.d/init.el takes over?
- worth a try

```
$ if [ ! -f ~/tmp/dot-emacs ] ; then
→   mv ~/.emacs ~/tmp/dot-emacs
→ fi
jeff at vega in ~
$ cp -pv /j/proj/dot-emacs/*.* ~/.emacs.d
/j/proj/dot-emacs/config.el -> /Users/jeff/.emacs.d/config.el
/j/proj/dot-emacs/config.org -> /Users/jeff/.emacs.d/config.org
/j/proj/dot-emacs/custom.el -> /Users/jeff/.emacs.d/custom.el
/j/proj/dot-emacs/init.el -> /Users/jeff/.emacs.d/init.el
```

- so that appears to have worked.
- so that means: no more dot-emacs project
  - do it in jwm-dotfiles
  - √ on a branch: refactor-emacs-init

- set up the initial set of files.
- on that branch, I can git rm .emacs
  - will that propogate through ./bootstrap.sh?  A: no, so I need a postprocessing step to rm ~/.emacs at times.

- √ so this should be the trick to get going:

```
cd /j/proj/jwm-dotfiles && ./bootstrap.sh -f && mv ~/.emacs ~/tmp/dot-emacs
```

## pull the best from other configs ##

- john wiegley
  - $ git clone git@github.com:jwiegley/dot-emacs.git ~/tmp/jwiegley-dotemacs
- daniel mai:
  - $ git clone git@github.com:danielmai/.emacs.d.git ~/tmp/danielmai-dotemacs

## bring back Jeffs stuff ##

- √ username
- √ jwm emacs dir

- solarized
- jeffs colors

- so how did Daniel do color theme?

## new functionality ##

**Mon Feb 27 18:37:47 PST 2017**

- strive for feature parity in the new scheme.
- what is left to map over?
- √ magit
- √ helm
  - helm-ag
    - installed, but I don't know how to use it yet.
- √ yasnippet
  - configure my qh haskell yasnippet
- DEFER xterm-color
  - and eshell
- √ intero
- ALREADY THERE figure out how to add recentf into helm, if it is not already there.
- √ nxhtml
  - I used jwiegley's nxml mode config instead.
- ccrypt and bcrypt support
  - transition to gpg2?

- mode hooks
  - C mode
  - python mode
- yaml-mode

- frame defaults
  - orange cursor in emacs
- font size / font setting on both platforms

- discard terminal face settings

- os x keybindings
  - adopt Daniel Mais

**Thu Mar  2 16:10:50 PST 2017**

- X figure out how to do a git pull from inside magit
  - shown on the top level magit page.
  - fetch: f u
  - pull: F u
- figure out how to create a branch inside magit

## Magit cheat sheet ##

- `z Z` to stash
- TAB will expand/contract visibility in a status buffer
- C-TAB will cycle visibility
  - a short cut for my often used 'd d'; switch to buffer approach

**Thu Mar  2 17:08:47 PST 2017**

## status ##

- so am I ready to move my emacs env over to orion?  A: no.
- what is the key functionality that is missing?
  - helm / ag searcher
  - which is not configured on vega.
  - xterm-color?
  - frame defaults
    - orange cursor in emacs
  - font size / font setting on both platforms

## issues noted ##

- comment-face is not italic
  - switch to custom-var style to make it so


## next steps ##

- so next steps in emacs move over:

- √ use settings.el for customization as jwiegley does
  - drop custom.el
- os x keybindings
  - adopt Daniel Mais
  - cant test this except under Frame
- where am I working?  jwm-dotfiles:refactor-emacs-init

**Sun Mar 12 10:23:49 PDT 2017**

## emacs ##

- √ install emacs 25 for GUI os x
  - https://emacsformacosx.com/
  - upgrade from 24.5.1
  - this can be had (and kept updated by brew) with the emacs cask:

``` sh
$ brew cask info emacs
emacs: 25.1-1
https://emacsformacosx.com/
```

### √ brew cask migration ###

- Ok, it turns out that the brew cask location has changed:

``` sh
$ brew cask list
Warning: The default Caskroom location has moved to /usr/local/Caskroom.

Please migrate your Casks to the new location and delete /opt/homebrew-cask/Caskroom,
or if you would like to keep your Caskroom at /opt/homebrew-cask/Caskroom, add the
following to your HOMEBREW_CASK_OPTS:

  --caskroom=/opt/homebrew-cask/Caskroom

For more details on each of those options, see https://github.com/caskroom/homebrew-cask/issues/21913.
emacs                     java                      rstudio                   vagrant                   virtualbox                wkhtmltopdf
```
- so I cleaned all of that up.
- then installed emacs fresh from homebrew cask.

``` sh
$ brew cask install emacs
==> Creating Caskroom at /usr/local/Caskroom
==> We'll set permissions properly so we won't need sudo in the future
==> Downloading https://emacsformacosx.com/emacs-builds/Emacs-25.1-1-universal.dmg
######################################################################## 100.0%
==> Verifying checksum for Cask emacs
==> Moving App 'Emacs.app' to '/Applications/Emacs.app'
==> Symlinking Binary 'emacsclient' to '/usr/local/bin/emacsclient'
==> Symlinking Binary 'ctags' to '/usr/local/bin/ctags'
==> Symlinking Binary 'ebrowse' to '/usr/local/bin/ebrowse'
==> Symlinking Binary 'etags' to '/usr/local/bin/etags'
🍺  emacs was successfully installed!
```

### √ improve cursor in terminal defaults so I can find it in emacs ###

- √ in iterm2, the cursor is an underline char now; make it an orange box so I can see it better.
  - alternatively, use <Alt/cookie> / iterm2 command to show the cursor.

- convert init.el to use the exact same solarized that .emacs does.
- make it so C-k at bol kills the whole line in init.el emacs.

### IN PROGRESS ag silver searcher ###

- IN PROGRESS get silver searcher working in emacs
  - at least understand what it can do for me
  - ag is a drop-in? replacement for ack

## ag ##

- it respect the contents of .gitignore and .hgignore
- and .ignore

### useful commands ###

- (helm-ag-project-root)
- search from the root of the project
  - using the heuristic of .git

- what is the difference between (helm-ag-project-root) and (helm-do-ag-project-root)

- (helm-do-ag-project-root)
  - seems like an interactive search

- C-u helm-ag
  - to search from a given directory

- what bindings to ag does eg, the emacs guy use?
  - work on it by searching
    - jwiegley
    - danielmai


### danielmai ag config ###

``` lisp
#+BEGIN_SRC emacs-lisp
(use-package ag
  :commands ag
  :ensure t)
#+END_SRC
```
### danielmai helm config ###

``` lisp
#+begin_src emacs-lisp
(use-package helm
  :ensure t
  :diminish helm-mode
  :init (progn
          (require 'helm-config)
          (use-package helm-projectile
            :ensure t
            :commands helm-projectile
            :bind ("C-c p h" . helm-projectile))
          (use-package helm-ag :defer 10  :ensure t)
          (setq helm-locate-command "mdfind -interpret -name %s %s"
                helm-ff-newfile-prompt-p nil
                helm-M-x-fuzzy-match t)
          (helm-mode)
          (use-package helm-swoop
            :ensure t
            :bind ("H-w" . helm-swoop)))
  :bind (("C-c h" . helm-command-prefix)
         ("C-x b" . helm-mini)
         ("C-`" . helm-resume)
         ("M-x" . helm-M-x)
         ("C-x C-f" . helm-find-files)))
#+end_src
```

### explore ag / helm configs ###

- Ok, I definitely want ag in my emacs config.  So add it to both variants.

- what does `:commands` do here?

```lisp
(use-package ag
  :commands ag
```

- A: from the docs:

:commands      Define autoloads for commands that will be defined by the
               package.  This is useful if the package is being lazily loaded,
               and you wish to conditionally call functions in your `:init'
               block that are defined in the package.

- how do I use `ag`?
- A: [ag usage](http://agel.readthedocs.io/en/latest/usage.html)

- it recommends installing wgrep
  - do jwiegley or danielmai have wgrep?
  - A: unanswered just yet.

**Sat Mar 11 13:22:47 PST 2017**

- √ Davo work
- write Peter K linkedin reference
- write Peter Malutta tax prep email
- √ update emacs env enough to be productive on vega
  - accomplised by reverting back to my former setup.
- install VM with windows 8 in prep for excel
  - next signal is Wed.
- reply to Speck

## emacs work ##

- kill to end of line when at beginning of line

## consider moving to refactor-emacs-init approach to emacs ##

### current issues ###

#### mac os x specific ####

- resolve the alt-vs option key issue on the mac keyboard.
- what I have now is not working.
  - the key labeled "alt" or clover is bound to: super
    - <Alt> d => s-d runs: s-d runs the command isearch-repeat-backward
  - the key labeled "option" or windows is bound to: meta
    - <Option> d => M-d runs the command kill-word
  - consider mapping the key labeled caps lock to Meta
    - it is big and then I could use my pinkie to shift into Meta

- shell-command-on-region issues:

bash: cannot set terminal process group (-1): Inappropriate ioctl for device
bash: no job control in this shell
(B[mSat Mar 11 13:30:48 PST 2017

#### common issues ####

- √ for window system:
  - menubar display for window system
  - √ doesn't kill the startup screen on startup

### transition plan ###

- make a branch to stash current emacs config: preserve-emacs-config-before-init-upgrade
- then merge refactor-emacs-init branch in
  - will destroy .emacs altogether

### test it out on ubuntu ###

- can I get emacs 25 on ubuntu?  I must be able to.
- move both branches over there; try things out.

**Sun Mar 12 22:47:22 PDT 2017**

## solarized blue background on terminal ##

- attempt to resolve the blue background in emacs -nw
  - there is no problem in emacs with window system

- consider the two solarized packages:
  - bbatsov: solarized-theme
    - which I started with
  - sellout: color-theme-solarized

- which one does danielmai use?  A: bbatsov, same as me.
