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
