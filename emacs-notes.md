## registers

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

## directory-local-variables

- I found an interesting [reference to directory-local-variables](http://atomized.org/2009/05/emacs-23-easier-directory-local-variables/)
    - it could be a solution to my per-directory formatting needs.

## php-mode

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

## recursive edit

when in recursive edit, with the [[ ]] on the mode line,

    C-[   abort-recursive-edit

will get out of it.

----

## mysql in emacs

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

## outline mode

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

### outline visibility commands

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

>    When incremental search finds text that is hidden by Outline mode, it makes that part
     of the buffer visible.  If you exit the search at that position, the text remains
     visible.  You can also automatically


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

## font size increase/decrease

The functions

        text-scale-increase             C-x  C-+
                   decrease             C-x  C--
                   set

can be used to change the font size of the current buffer.
Very useful.

----

## comint mode

emacs notes to drill down on:

        from lisp/progmodes/sql.el

        ;; For documentation on the functionality provided by comint mode, and
        ;; the hooks available for customizing it, see the file `comint.el`.

        ;; Hint for newbies: take a look at `dabbrev-expand`, `abbrev-mode`, and
        ;; `imenu-add-menubar-index`.

----

## solarized emacs

- [code and instructions](https://github.com/sellout/emacs-color-theme-solarized) from github

### precursor

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

Other data:

- [solarized theme](https://github.com/bbatsov/solarized-emacs) available as a package loaded by a package manager
    - works from emacs 24 on.
    - some support for emacs 23.
    - recommends [MELPA](http://melpa.org/) emacs package manager

----

## Other packages I want

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

## √ el-get

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

## √ solarized

- I like solarized-dark

### next steps

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

  highlight-symbol            available  Quickly highlight a symbol throughout the buffer and cycle through its locations.


----

## elisp references

- Steve Yegge has written his [emergency elisp](http://steve-yegge.blogspot.com/2008/01/emergency-elisp.html) blog entry
    - it is written for programmers who don't know elisp.  good stuff.  Coverge includes:
    - lexical stuff
    - operators
    - statements
    - classes
    - with some nice elisp / java side by side comparisons

----

## use solarized foreground and background colors

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

## better find-files

- emacs wiki [Locate Files Anywhere](http://www.emacswiki.org/emacs/LocateFilesAnywhere)
- precursor [Emacs: Helm for finding files](http://amitp.blogspot.com/2012/10/emacs-helm-for-finding-files.html)

## utf 8 / unicode

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
