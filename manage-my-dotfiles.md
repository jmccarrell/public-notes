# dotfile manager

- (large) [reference to many different ways to do dotfiles](https://dotfiles.github.io), and bash themes
- choose [rcm](https://github.com/thoughtbot/rcm) as my dotfile mgr of choice, because of its wide support on common
  linux-en I use

## jeff's policy decisions

- my dotfiles will be stored in a private gitlab repo
- no ssh keys will be stored in gitlab ever


## [install](https://github.com/thoughtbot/rcm#installation)

- osx


## rcm notes

- the [intro](http://thoughtbot.github.io/rcm/rcm.7.html)
    - section "quick start for empty dotfiles directories

- the recipe:

1. Add your rc files to a dotfiles directory with mkrc(1).

        mkrc .zshrc .gitconfig .tigrc

1. Synchronize your home directory with rcup(1)

        rcup -v

## my dotfiles to sync

        NO   -r--------   1 jeff  staff      7 Oct 17  2014 .CFUserTextEncoding
        NO   -rw-r--r--@  1 jeff  staff  24580 Jun  3 16:01 .DS_Store
        NO   drwxr-xr-x   3 jeff  staff    102 Mar 26 17:54 .PyCharm40
        NO  drwx------   2 jeff  staff     68 Jun  3 13:52 .Trash
        √  -rw-r--r--   1 jeff  staff    271 Sep  9  2011 .ackrc
        NO   -rw-------   1 jeff  staff  13992 Jun  3 08:26 .bash_history
        √   -rw-r--r--   1 jeff  staff   1976 May  9 16:08 .bash_profile
        √   -rw-r--r--   1 jeff  staff   1100 May  2 11:19 .bashrc
        NO   drwxr-xr-x   3 jeff  staff    102 Apr 14  2012 .bazaar
        √  drwxr-xr-x   3 jeff  staff    102 Feb 24 16:54 .config
        NO  drwx------   3 jeff  staff    102 Mar 27  2014 .cups
        √  -rw-r--r--   1 jeff  staff     40 May 29  2008 .cvsrc
        NO  drwxr-xr-x   3 root  staff    102 Apr 16  2014 .distlib
        NO  drwx------  11 jeff  staff    374 May 30 14:53 .dropbox
        √  -rw-r--r--   1 jeff  staff   9163 Sep 11  2014 .emacs
        √  -r--r--r--   1 jeff  staff      0 Jul 11  2008 .emacs-custom-21.el
        √  -rw-r--r--   1 jeff  staff    343 Sep 11  2014 .emacs-custom-22.el
        √  -rw-r--r--   1 jeff  staff    723 Sep 11  2014 .emacs-custom-23.el
        √  -rw-r--r--   1 jeff  staff    723 Sep 11  2014 .emacs-custom-24.el
        √  -r--r--r--   1 jeff  staff      0 Jul 11  2008 .emacs-custom-future.el
        NO  drwx------   2 jeff  staff     68 Mar 24  2014 .emacs.d
        √  -rw-r--r--   1 jeff  staff     10 May 27  2014 .git_ignore_global
        √  -rw-r--r--   1 jeff  staff   1245 Jun  1 17:12 .gitconfig
        √  -rw-r--r--   1 jeff  staff     13 Mar 19  2013 .gitignore_global
        NO  -rw-r--r--   1 jeff  staff     27 Mar 19  2013 .hgignore_global
        NO  -rw-------   1 jeff  staff    631 Jun  3 18:11 .lesshst
        NO  -rw-r--r--   1 jeff  staff     25 Feb 28 18:04 .my.cnf
        NO  -rw-r--r--   1 jeff  staff    298 Mar 18  2013 .my.invino.cnf
        NO  -rw-------   1 jeff  staff    280 Feb 28 18:31 .mylogin.cnf
        NO  -rw-------   1 jeff  staff   2024 May 30 14:47 .mysql_history
        NO  drwxr-xr-x   3 jeff  staff    102 Apr 16  2014 .pip
        NO  -rw-------   1 jeff  staff      0 May  5 18:08 .python_history
        NO  drwx------  16 jeff  staff    544 May 30 17:37 .ssh
        √  -rw-rw-r--   1 jeff  staff    209 Jun  2 17:39 .tmux.conf
        NO  -rw-------   1 jeff  staff    700 May 18  2014 .viminfo
        NO  drwxr-xr-x  16 jeff  staff    544 May  9 16:08 .virtualenvs

so that means

    .ackrc
    .bash_profile
    .bashrc
    .config
    .cvsrc
    .emacs
    .emacs-custom-21.el
    .emacs-custom-22.el
    .emacs-custom-23.el
    .emacs-custom-24.el
    .emacs-custom-future.el
    .git_ignore_global
    .gitconfig
    .gitignore_global
    .tmux.conf

.ackrc .bash_profile .bashrc .config .cvsrc .emacs .emacs-custom-21.el .emacs-custom-22.el .emacs-custom-23.el .emacs-custom-24.el .emacs-custom-future.el .git_ignore_global .gitconfig .gitignore_global .tmux.conf

        vega-> mkrc .ackrc .bash_profile .bashrc .config .cvsrc .emacs .emacs-custom-21.el .emacs-custom-22.el .emacs-custom-23.el .emacs-custom-24.el .emacs-custom-future.el .git_ignore_global .gitconfig .gitignore_global .tmux.conf
        Moving...
        Linking...
          ...

        vega-> rcup -v
        identical /Users/jeff/.ackrc
          ...

## share with gitlab

        vega-> git init
        Initialized empty Git repository in /Users/jeff/.dotfiles/.git/
        vega-> git st
        On branch master

        Initial commit

        Untracked files:
          (use "git add <file>..." to include in what will be committed)

                ackrc
                bash_profile
                bashrc
                config/
                cvsrc
                emacs
                emacs-custom-21.el
                emacs-custom-22.el
                emacs-custom-23.el
                emacs-custom-24.el
                emacs-custom-future.el
                git_ignore_global
                gitconfig
                gitignore_global
                tmux.conf

        nothing added to commit but untracked files present (use "git add" to track)
        vega-> git add *
        vega-> git commit -m 'inital set of dotfiles.'
        [master (root-commit) 5a657e7] inital set of dotfiles.
         16 files changed, 585 insertions(+)
         create mode 100644 ackrc
         create mode 100644 bash_profile
         create mode 100644 bashrc
         create mode 100644 config/git/gitk
         create mode 100644 config/git/ignore
         create mode 100644 cvsrc
         create mode 100644 emacs
         create mode 100644 emacs-custom-21.el
         create mode 100644 emacs-custom-22.el
         create mode 100644 emacs-custom-23.el
         create mode 100644 emacs-custom-24.el
         create mode 100644 emacs-custom-future.el
         create mode 100644 git_ignore_global
         create mode 100644 gitconfig
         create mode 100644 gitignore_global
         create mode 100644 tmux.conf
        vega-> git remote add origin git@gitlab.com:jmccarrell/dotfiles.git
        vega-> git push -u origin master
        Counting objects: 17, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (13/13), done.
        Writing objects: 100% (17/17), 7.60 KiB | 0 bytes/s, done.
        Total 17 (delta 1), reused 0 (delta 0)
        To git@gitlab.com:jmccarrell/dotfiles.git
         * [new branch]      master -> master
        Branch master set up to track remote branch master from origin.

----

**Fri Jun  5 09:32:28 PDT 2015**

- Ok, using rcm is Ok, but I would like:
    1. distinguish architecture in .dot files so I don't invoke brew on linux boxes
    1. I would like some of my bin managed too

Here is a solution for brew (from Mathias)

# Add tab completion for many Bash commands
if which brew > /dev/null && [ -f "$(brew --prefix)/share/bash-completion/bash_completion" ]; then


- I had previously forked justone/dotfiles
    - I am less impresses with this now.  rcm is a better choice than justone's 300 lines of perl.
    - throw this out?

- inspect (clone and read) some power-user dotfiles setups:
    - [Mathias](https://github.com/mathiasbynens/dotfiles)
        - vega: `~/tmp/dotfiles/mathias/`


## Mathias

### aliases

Ok, there are some aliases in there I could use.  And some I don't want.

### bash_profile

I want the tab completion stuff in there, especially tab completion of ssh/config names.

### bash_prompt

I may not want all of this, but I can start with it, and pare it down as needed.

### editor config

I want this

- there are a couple of functions I want as well.

----

**Sun Jun  7 13:25:33 PDT 2015**

# move to new dotfiles

## todo

- √ install and start using spectable for window sizing/moving by keyboard shortcuts
    - NOT YET install the defaults in .osx for spectacle
- DEFERRED install and start using sizeup; move away from Moom
    - install the defaults in .osx for sizeup
- √ drill down into .path
    - is it supposed to be versioned?
        - A: I think not.
    - what does the README say?

            /usr/local/bin/ack --literal .path
            .bash_profile:5:# * ~/.path can be used to extend `$PATH`.

            README.md:39:If `~/.path` exists, it will be sourced along with the other files, before any feature testing (such as [detecting which version of `ls` is being used](https://github.com/mathiasbynens/dotfiles/blob/aff769fd75225d8f2e481185a71d5e05b76002dc/.aliases#L21-26)) takes place.
            README.md:41:Here’s an example `~/.path` file that adds `/usr/local/bin` to the `$PATH`:

- √ FAILS test my 'e' alias
- √ add my git credentials to ~/.extras
- √ figure out to leverage the iterm color profile installed by:

        # Install the Solarized Dark theme for iTerm
        open "${HOME}/init/Solarized Dark.itermcolors"

    - The color scheme was imported and added to presets. You can find it under Preferences>Profiles>Colors>Load Presets….

- √ remove all links to dotfiles

- √ .ackrc@ -> /Users/jeff/.dotfiles/ackrc
- √ RM .cvsrc@ -> /Users/jeff/.dotfiles/cvsrc
- √ .emacs@ -> /Users/jeff/.dotfiles/emacs
- √ .emacs-custom-21.el@ -> /Users/jeff/.dotfiles/emacs-custom-21.el
- √ .emacs-custom-22.el@ -> /Users/jeff/.dotfiles/emacs-custom-22.el
- √ .emacs-custom-23.el@ -> /Users/jeff/.dotfiles/emacs-custom-23.el
- √ .emacs-custom-24.el@ -> /Users/jeff/.dotfiles/emacs-custom-24.el
- √ .emacs-custom-future.el@ -> /Users/jeff/.dotfiles/emacs-custom-future.el
- √ NO .emacs.d/
- √ RM .git_ignore_global@ -> /Users/jeff/.dotfiles/git_ignore_global
- √ RM .gitignore_global@ -> /Users/jeff/.dotfiles/gitignore_global
- √ .tmux.conf@ -> /Users/jeff/.dotfiles/tmux.conf

- √ add a package to emacs to take advantage of editorconfig
- √ drill into ssh-copy-id
- √ fix up the selection-color green of .osx
- √ set up the javascript REPL
    - use `jsc`
    - defined in aliases
- IN PROGRESS drill into [iterm2 tmux](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration)
- find an use someone elses tmux config files

- figure out how to leverage the hot corners set up in .osx
## backup existing dotfiles and bin

- Ok, I want to move to Mathias' dotfiles scheme.
- should I spend any time building a recovery scheme?
    - A: yes: ~/tmp/backup-dotfiles
    - vega-> tar cvf ~/tmp/backup-dotfiles/dotfiles.tar .??*
    - vega-> tar -cvf ~/tmp/backup-dotfiles/bin.tar bin

## describe current dotfiles

- they are in ~/.dotfiles, as configured by rcm

        Initialized empty Git repository in /Users/jeff/.dotfiles/.git/

- will Mathias' config conflict with that?
    - does Mathias' approach symlink?
    - No, it rsyncs from the git repo into the home directory
    - so the overwrite symlink question comes down to the behavior of rsync on symlinks
    - in any case, rcup should be able to recreate the dotfiles that I have currently.

- where will I store my dotfiles?
    - √ /j/proj/jwm-dotfiles
    - /j/proj/dotfiles
    - ~/jwm-dotfiles

- the Mathias rsync will not delete any dotfiles that I remove from the repo in my home dir.
    - so it would be important for me to delete the dot files I don't want

- √ Nuke my previous justone dotfiles
- √ fork and clone Mathias repo
- √ make jwm-dotfiles branch

- make my initial review to Mathias' repo

## aliases, bash_profile

## bash prompt

- start with Mathias' version; revise it downward over time

## gitconfig

I need to merge my git configuration into git config

## hushlogin

I deleted this; I want to see the login messages from the system.

## bin

- √ add sample, commify

Ok, I have made the initial pass through the dotfiles.

Now, run subsets of .osx to build the base system the aliases assume.

IN PROGRESS

it is not clear this worked:
# Menu bar: hide the Time Machine, Volume, and User icons
for domain in ~/Library/Preferences/ByHost/com.apple.systemuiserver.*; do
	defaults write "${domain}" dontAutoLoad -array \
		"/System/Library/CoreServices/Menu Extras/TimeMachine.menu" \
		"/System/Library/CoreServices/Menu Extras/Volume.menu" \
		"/System/Library/CoreServices/Menu Extras/User.menu"
done
defaults write com.apple.systemuiserver menuExtras -array \
	"/System/Library/CoreServices/Menu Extras/Bluetooth.menu" \
	"/System/Library/CoreServices/Menu Extras/AirPort.menu" \
	"/System/Library/CoreServices/Menu Extras/Battery.menu" \
	"/System/Library/CoreServices/Menu Extras/Clock.menu"

√ try rebooting:

IN PROGRESS

the next step would be:

# Display ASCII control characters using caret notation in standard text views
# Try e.g. `cd /tmp; unidecode "\x{0000}" > cc.txt; open -e cc.txt`
defaults write NSGlobalDomain NSTextShowsControlCharacters -bool true

IN PROGRESS

- reboot
- start again at Mail

COMPLETED.

## homebrew setup

### √ coreutils

- √ dotfiles brew.sh says:

        # Install GNU core utilities (those that come with OS X are outdated).
        # Don’t forget to add `$(brew --prefix coreutils)/libexec/gnubin` to `$PATH`.


- the output from brew install

        All commands have been installed with the prefix 'g'.

        If you really need to use these commands with their normal names, you
        can add a "gnubin" directory to your PATH from your bashrc like:

            PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

        Additionally, you can access their man pages with normal names if you add
        the "gnuman" directory to your MANPATH from your bashrc as well:

            MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"


$ git commit -m 'intermediate checkpoint while customizing dotfiles'
[jwm-dotfiles a5a1a68] intermediate checkpoint while customizing dotfiles
 Committer: Jeff McCarrell <jeff@vega.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 3 files changed, 73 insertions(+), 46 deletions(-)

- √ set my git identity; follow the git pattern Mathias recommends

### √ bash

# Install Bash 4.
# Note: don’t forget to add `/usr/local/bin/bash` to `/etc/shells` before
# running `chsh`.
brew install bash
brew tap homebrew/versions
brew install bash-completion2


brew output

        $ brew tap homebrew/versions
        ==> Tapping Homebrew/versions
        Cloning into '/usr/local/Library/Taps/homebrew/homebrew-versions'...
          ...
        Tapped 224 formulae (248 files, 1.4M)
        It looks like you tapped a private repository. To avoid entering your
        credentials each time you update, you can use git HTTP credential
        caching or issue the following command:

          cd /usr/local/Library/Taps/homebrew/homebrew-versions
          git remote set-url origin git@github.com:Homebrew/homebrew-versions.git

brew output

        $ brew install bash-completion2
          ...
        ==> Caveats
        Add the following to your ~/.bash_profile:
          if [ -f $(brew --prefix)/share/bash-completion/bash_completion ]; then
            . $(brew --prefix)/share/bash-completion/bash_completion
          fi

          Homebrew's own bash completion script has been linked into
            /usr/local/share/bash-completion/completions
          bash-completion will automatically source it when you invoke `brew`.

          Any completion scripts in /usr/local/etc/bash_completion.d
          will continue to be sourced as well.

### gnu grep

    ==> Installing homebrew/dupes/grep
    ==> Downloading http://ftpmirror.gnu.org/grep/grep-2.21.tar.xz
    ######################################################################## 100.0%
    ==> ./configure --disable-nls --prefix=/usr/local/Cellar/grep/2.21 --infodir=/usr/local/Cellar/grep
    ==> make
    ==> make install
    ==> Caveats
    The command has been installed with the prefix "g".
    If you do not want the prefix, install using the "with-default-names"
    option.
    ==> Summary
    🍺  /usr/local/Cellar/grep/2.21: 14 files, 760K, built in 46 seconds



### php

    $ brew install homebrew/php/php55 --with-gmp
    ==> Tapping Homebrew/php
    Cloning into '/usr/local/Library/Taps/homebrew/homebrew-php'...
    remote: Counting objects: 485, done.
    remote: Compressing objects: 100% (172/172), done.
    remote: Total 485 (delta 372), reused 354 (delta 312), pack-reused 0
    Receiving objects: 100% (485/485), 135.87 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (372/372), done.
    Checking connectivity... done.
    Tapped 469 formulae (502 files, 2.2M)
    It looks like you tapped a private repository. To avoid entering your
    credentials each time you update, you can use git HTTP credential
    caching or issue the following command:

      cd /usr/local/Library/Taps/homebrew/homebrew-php
      git remote set-url origin git@github.com:Homebrew/homebrew-php.git
    ==> Installing php55 from homebrew/homebrew-php
    ==> Installing dependencies for homebrew/php/php55: libpng, freetype, homebrew/dupes/zlib, i
    ==> Installing homebrew/php/php55 dependency: libpng
    ==> Downloading https://homebrew.bintray.com/bottles/libpng-1.6.17.yosemite.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring libpng-1.6.17.yosemite.bottle.tar.gz
    🍺  /usr/local/Cellar/libpng/1.6.17: 17 files, 1.2M
    ==> Installing homebrew/php/php55 dependency: freetype
    ==> Downloading https://homebrew.bintray.com/bottles/freetype-2.5.5.yosemite.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring freetype-2.5.5.yosemite.bottle.tar.gz
    🍺  /usr/local/Cellar/freetype/2.5.5: 60 files, 2.6M
    ==> Installing homebrew/php/php55 dependency: homebrew/dupes/zlib
    ==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/dupes/zlib-1.2.8.yosemite.bott
    ######################################################################## 100.0%
    ==> Pouring zlib-1.2.8.yosemite.bottle.tar.gz
    ==> Caveats
    This formula is keg-only, which means it was not symlinked into /usr/local.

    Mac OS X already provides this software and installing another version in
    parallel can cause all kinds of trouble.

    Generally there are no consequences of this for you. If you build your
    own software and it requires this formula, you'll need to add to your
    build variables:

        LDFLAGS:  -L/usr/local/opt/zlib/lib
        CPPFLAGS: -I/usr/local/opt/zlib/include

    ==> Summary
    🍺  /usr/local/Cellar/zlib/1.2.8: 9 files, 392K
    ==> Installing homebrew/php/php55 dependency: icu4c
    ==> Downloading https://homebrew.bintray.com/bottles/icu4c-55.1.yosemite.bottle.tar.gz
    ######################################################################## 100.0%
    ==> Pouring icu4c-55.1.yosemite.bottle.tar.gz
    ==> Caveats
    This formula is keg-only, which means it was not symlinked into /usr/local.

    Mac OS X already provides this software and installing another version in
    parallel can cause all kinds of trouble.

    OS X provides libicucore.dylib (but nothing else).

    Generally there are no consequences of this for you. If you build your
    own software and it requires this formula, you'll need to add to your
    build variables:

        LDFLAGS:  -L/usr/local/opt/icu4c/lib
        CPPFLAGS: -I/usr/local/opt/icu4c/include

    ==> Summary
    🍺  /usr/local/Cellar/icu4c/55.1: 244 files, 66M
    ==> Installing homebrew/php/php55 dependency: jpeg
    ==> Downloading https://homebrew.bintray.com/bottles/jpeg-8d.yosemite.bottle.2.tar.gz
    ######################################################################## 100.0%
    ==> Pouring jpeg-8d.yosemite.bottle.2.tar.gz
    🍺  /usr/local/Cellar/jpeg/8d: 18 files, 776K
    ==> Installing homebrew/php/php55 dependency: unixodbc
    ==> Downloading https://homebrew.bintray.com/bottles/unixodbc-2.3.2_1.yosemite.bottle.1.tar.gz
    ######################################################################## 100.0%
    ==> Pouring unixodbc-2.3.2_1.yosemite.bottle.1.tar.gz
    🍺  /usr/local/Cellar/unixodbc/2.3.2_1: 31 files, 1.0M
    ==> Installing homebrew/php/php55
    ==> Downloading https://www.php.net/get/php-5.5.25.tar.bz2/from/this/mirror
    ######################################################################## 100.0%
    ==> ./configure --prefix=/usr/local/Cellar/php55/5.5.25 --localstatedir=/usr/local/var --sysconfdir
    ==> make
    ==> make install
    ==> /usr/local/Cellar/php55/5.5.25/bin/pear config-set php_ini /usr/local/etc/php/5.5/php.ini syste
    ==> Caveats
    To enable PHP in Apache add the following to httpd.conf and restart Apache:
        LoadModule php5_module    /usr/local/opt/php55/libexec/apache2/libphp5.so

    The php.ini file can be found in:
        /usr/local/etc/php/5.5/php.ini

    ✩✩✩✩ PEAR ✩✩✩✩

    If PEAR complains about permissions, 'fix' the default PEAR permissions and config:
        chmod -R ug+w /usr/local/Cellar/php55/5.5.25/lib/php
        pear config-set php_ini /usr/local/etc/php/5.5/php.ini system

    ✩✩✩✩ Extensions ✩✩✩✩

    If you are having issues with custom extension compiling, ensure that
    you are using the brew version, by placing /usr/local/bin before /usr/sbin in your PATH:

          PATH="/usr/local/bin:$PATH"

    PHP55 Extensions will always be compiled against this PHP. Please install them
    using --without-homebrew-php to enable compiling against system PHP.

    ✩✩✩✩ PHP CLI ✩✩✩✩

    If you wish to swap the PHP you use on the command line, you should add the following to ~/.bashrc,
    ~/.zshrc, ~/.profile or your shell's equivalent configuration file:

          export PATH="$(brew --prefix homebrew/php/php55)/bin:$PATH"

    ✩✩✩✩ FPM ✩✩✩✩

    To launch php-fpm on startup:
        mkdir -p ~/Library/LaunchAgents
        cp /usr/local/opt/php55/homebrew.mxcl.php55.plist ~/Library/LaunchAgents/
        launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.php55.plist

    The control script is located at /usr/local/opt/php55/sbin/php55-fpm

    OS X 10.8 and newer come with php-fpm pre-installed, to ensure you are using the brew version you need to make sure /usr/local/sbin is before /usr/sbin in your PATH:

      PATH="/usr/local/sbin:$PATH"

    You may also need to edit the plist to use the correct "UserName".

    Please note that the plist was called 'homebrew-php.josegonzalez.php55.plist' in old versions
    of this formula.

    To have launchd start homebrew/php/php55 at login:
        ln -sfv /usr/local/opt/php55/*.plist ~/Library/LaunchAgents
    Then to load homebrew/php/php55 now:
        launchctl load ~/Library/LaunchAgents/homebrew.mxcl.php55.plist
    ==> Summary
    🍺  /usr/local/Cellar/php55/5.5.25: 497 files, 50M, built in 2.4 minutes


### √ font tools

    It looks like you tapped a private repository. To avoid entering your
    credentials each time you update, you can use git HTTP credential
    caching or issue the following command:

      cd /usr/local/Library/Taps/bramstein/homebrew-webfonttools
      git remote set-url origin git@github.com:bramstein/homebrew-webfonttools.git

- √ brew install completed.

----

**Sun Jun  7 23:41:36 PDT 2015**

- Ok, basic dotfiles install is completed on vega.
- Next up, an emacs package manager.
- editorconfig support.

## emacs package manager

- get editorconfig via brew

        $ brew install editorconfig
        ==> Installing editorconfig dependency: cmake
        ==> Downloading https://homebrew.bintray.com/bottles/cmake-3.2.2.yosemite.bottle.5.tar.gz
        ######################################################################## 100.0%
        ==> Pouring cmake-3.2.2.yosemite.bottle.5.tar.gz
        ==> Caveats
        Bash completion has been installed to:
          /usr/local/etc/bash_completion.d
        ==> Summary
        🍺  /usr/local/Cellar/cmake/3.2.2: 1850 files, 32M
        ==> Installing editorconfig
        ==> Downloading https://downloads.sourceforge.net/project/editorconfig/EditorConfig-C-Core/0.12.0/s
        ######################################################################## 100.0%
        ==> cmake . -DCMAKE_INSTALL_PREFIX:PATH=/usr/local/Cellar/editorconfig/0.12.0
        ==> make install
        🍺  /usr/local/Cellar/editorconfig/0.12.0: 8 files, 120K, built in 6 seconds

        $ ls -l /usr/local/lib/libeditorconfig
        libeditorconfig.0.12.0.dylib@ libeditorconfig.dylib@
        libeditorconfig.0.dylib@      libeditorconfig_static.a

- then I have to put the editorconfig.el somewhere
    - /usr/local/share/emacs/site-lisp

            $ cp -pv editorconfig.el  /usr/local/share/emacs/site-lisp/

- so brew installs emacs in ~/Applications
    - nuke the copy I have in /Applications

            $ brew install emacs
            ==> Downloading https://homebrew.bintray.com/bottles/emacs-24.5.yosemite.bottle.tar.gz
            ######################################################################## 100.0%
            ==> Pouring emacs-24.5.yosemite.bottle.tar.gz
            ==> Caveats
            To have launchd start emacs at login:
                ln -sfv /usr/local/opt/emacs/*.plist ~/Library/LaunchAgents
            Then to load emacs now:
                launchctl load ~/Library/LaunchAgents/homebrew.mxcl.emacs.plist

- √ so startup emacs at login

### emacs package managers

- [ELPA Emacs Lisp Package Archive](launchctl load ~/Library/LaunchAgents/homebrew.mxcl.emacs.plist)

### tmux work

            Example configurations have been installed to:
              /usr/local/Cellar/tmux/2.0/share/tmux/examples


              /usr/local/Cellar/tmux/2.0/share/tmux/examples:
              -rw-r--r--   1 jeff  admin   913 Apr 29 10:42 h-boetes.conf
              -rw-r--r--   1 jeff  admin  2338 Apr 29 10:42 n-marriott.conf
              -rw-r--r--   1 jeff  admin  1805 Apr 29 10:42 screen-keys.conf
              -rw-r--r--   1 jeff  admin  2789 Apr 29 10:42 t-williams.conf
              -rw-r--r--   1 jeff  admin  5456 Apr 29 10:42 tmux.vim
              -rw-r--r--   1 jeff  admin  2513 Apr 29 10:42 tmux_backup.sh
              -rw-r--r--   1 jeff  admin  1088 Apr 29 10:42 vim-keys.conf
              -rw-r--r--   1 jeff  admin  1291 Apr 29 10:42 xterm-keys.vim

- [iterm2 tmux](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration)
- √ read the tmux man page

- recommends tmux -CC which is "control mode".

----

## √ test dotfiles on new ubuntu host

- my dotfiles are in the branch jwm-dotfiles.
- so push that:

        $ git push origin jwm-dotfiles
          ...
        To git@github.com:jmccarrell/dotfiles.git
         * [new branch]      jwm-dotfiles -> jwm-dotfiles

- and stand up a new digital ocean box and test.
- √ it works
