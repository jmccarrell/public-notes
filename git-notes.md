git is a distributed version control system

good docs:
  http://gitref.org/index.html

git immersion guide:
  http://www.gitimmersion.com


meaning there is no central repository.
Every 'clone' carries its own copy of the revision history.

git clone will copy the entire history of the project and will give you
a working directory of the main branch.

so the process of publishing changes is necessarily in 2 stages:

commit locally, typically with git add
then 'push' and 'pull' changes shared with others to remote repositories.

often to submit local changes to existing files, one uses
git add -p
which starts up in patch mode, showing each patch made, and presenting the option
to commit it locally.

use
git add <filenames>
to add new files to the project.

This is analogous to putting it in the changelist of p4.

commit changes eg:

git commit -m 'commit message'

Or, tell git to find all changes at commit time:

git commit -a ...

Or tell git to commit changes to named files:

git commit -a <filenames>

The changes that are staged with git add are in a buffer;
further changes to the underlying file are not in the buffer until explicitly put there.

Both git status and diff show uncommitted changes in the tree.

----------------------------------------------------------------

customizing git appropriately:

# tell git who I am:
git config --global user.name  "Jeff McCarrell"
git config --global user.email "jeff@mccarrell.org"

# and I like colorized output:
git config --global color.ui "auto"

# ignore mac os file system turdlets
#  cf: http://stackoverflow.com/questions/18393498/gitignore-all-the-ds-store-files-in-every-folder-and-subfolder
echo .DS_Store > ~/.git_ignore_global
git config --global core.excludesfile ~/.git_ignore_global

# set up my github access
git config --global github.user 'jmccarrell'
git config --global github.token '38cc87efff6d6cee3252480094848397'

----------------

pretty print git history of all branches:

git config --global alias.graph "log --all --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%ci)%C(bold blue)<%an>%Creset'"

----

show where current branches and remotes are in the commit history

git log --oneline --decorate

----

other aliases I like

git config --global alias.co checkout
git config --global alias.st status

----------------

git diff
with no arguments, shows changes between staging and working tree.
I.e. it will not show changes that are already staged.

add --cached to see just the differences between staged and repository,
not including any changes in the local working tree.

use
git diff HEAD
to see all changes between working tree, staging and repository.

HEAD refers to the most recent commit to the branch you are working in.

To see the diffs between 2 commits, name them:
       git diff [--options] <commit> <commit> [--] [<path>...]
           This is to view the changes between two arbitrary <commit>.



----------------

rename files with git mv
git mv index.html hello.html

wildcards can be ignored by git by naming them in .gitignore
or .git/info/exclude
  which is likely a better way to handle this case.
  .gitignore is not ignored by git by default...

----------------

Branching

The * shows which branch is currently checked out, ie., which branch to work against:

  proteus-> git branch new
  proteus-> git branch
  * master
    new

NB that master is still the checked out branch

  proteus-> git checkout new
  Switched to branch 'new'

One can create and checkout in 1 step with the -b to checkout:

  proteus-> git checkout -b alternate master
  Switched to a new branch 'alternate'
  proteus-> git branch
  * alternate
    master
    new


After adding an about.html file to alternate branch, I can merge it master.
First I have to have the target branch in view:

  proteus-> git checkout master
  Switched to branch 'master'
  Your branch is ahead of 'origin/master' by 2 commits.

then merge the 2 branches:

  proteus-> git merge alternate
  Updating 6bb34c7..925ae22
  Fast-forward
   about.html |   10 ++++++++++
   1 files changed, 10 insertions(+), 0 deletions(-)
   create mode 100644 about.html

Squashed commits are a common way to batch changes in a branch into a single commit
in an upstream branch.

Having made 2 changes in my 'contact' branch, I can squash commit them to master with:

  proteus-> git checkout master
  Switched to branch 'master'
  Your branch is ahead of 'origin/master' by 3 commits.

  proteus-> git merge --squash contact
  Updating 925ae22..e69b104
  Fast-forward
  Squash commit -- not updating HEAD
   contact.html |   10 ++++++++++
   1 files changed, 10 insertions(+), 0 deletions(-)
   create mode 100644 contact.html

Unlike a straight merge, a squash merge does not commit; the changes are staged,
as git status will show.

cherry picking pulls specific named changes:

  proteus-> git commit -m "add metoo link" -a
  [contact d23858a] add metoo link
   1 files changed, 1 insertions(+), 0 deletions(-)

  proteus-> git checkout master
  Switched to branch 'master'
  Your branch is ahead of 'origin/master' by 4 commits.

  proteus-> git cherry-pick d23858a
  Finished one cherry-pick.
  [master 40ef4f4] add metoo link
   1 files changed, 1 insertions(+), 0 deletions(-)

If there are > 1 change to cherry pick, add -n.
This tells git to do the 1 change, but not the commit.
Then you can merge other changes as needed and commit by hand.

  proteus-> git cherry-pick -n d23858a
  Finished one cherry-pick.
  proteus-> git status
  # On branch master
  # Your branch is ahead of 'origin/master' by 4 commits.
  #
  # Changes to be committed:
  #   (use "git reset HEAD <file>..." to unstage)
  #
  #	modified:   contact.html

N.B. The Xcode tools from apple include opendiff,
which can be used to do file merges.

git mergetool
will find opendiff on my OSX box for the graphical merge tool for conflicts.
Choose save after choosing each conflict on opendiff.

or use p4merge (hint from gitimmersion tutorial):

    git doesn’t provide any graphical merge tools, but it will gladly work with any third
    party merge tool you wish to use. See
    http://onestepback.org/index.cgi/Tech/Git/UsingP4MergeWithGit.red for a description of
    using the Perforce merge tool with git.

use
git branch -d <branchname>
to delete branches that are no longer needed.

  proteus-> git branch -d about2
  Deleted branch about2 (was 863c62f).

git will prevent deleting a branch whose changes are not yet merged:

  proteus-> git branch -d about
  error: The branch 'about' is not fully merged.
  If you are sure you want to delete it, run 'git branch -D about'.
----
When to Rebase, When to Merge?
(from gitimmersion tutorial)

    Don’t use rebase …

    If the branch is public and shared with others. Rewriting publicly shared branches
    will tend to screw up other members of the team.

    When the exact history of the commit branch is important (since rebase rewrites the
    commit history).

    Given the above guidelines, I tend to use rebase for short-lived, local branches and
    merge for branches in the public repository.

----------------

examining history

git log
shows revision history

use --pretty=oneline for a one line summary:

    capella-> git log --pretty=oneline
    190536b667fc952497cd2cda55941223ce8f4b77 add a comment
    a51ef64e6a81a237c91c70500e0f8272f4058a26 Add a default value
    6054f7f2d30404890225dbd41608e80c8affd36b Using ARGV
    2275eacbf54d155da575fc40ff11463f94037226 First Commit

how to see changes in the last 1 week; add --author="Jeff McCarrell" to see just my commits:
git log --all --pretty=format:"%h %cd %s (%an)" --since='7 days ago'

gitimmersion 'ultimate log format'
  - shows nested commit relationships
  - can take a while (10 secs or so) to run:
git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short

git log will show tags as well, ie:
git hist master --all

add -p to show diffs

add -<n> where <n> is an integer to limit output to that many commits.
So to see diffs of the last commit, use:
git log -p -1

Start the log viewing at a named commit by giving the commit
(recall you only need a unique prefix of the commmit name, typically 5 - 8 characters):

    git log -p -1 18f822eb10

there are the --since and --before params which take human parseable times/dates:

--since="5 hours"
--before="2010-09-01"

    proteus-> git log --since='2008-09-21' --pretty=oneline
    0bb3dfb752fa3c890ffc781fd6bd5dc5d34cd3be add link to twitter
    18f822eb1044761f59aebaf7739261042ae10392 add contact page
    217a88e9cdcb6c003e4b692fc620c7e545fc99f4 add the skeleton of an about page
    9a234643d3444ce456d2642584ca0919aa0f27b8 rename to more appropriate name
    6f1bf6ffd4bbf79d0b0f34c38c597b2d4ed89a70 Change biography link and add contact link
    4333289ecc18d9931bd420fc87bc1f43289170fb add in a bio link
    4b5377945aba872d5b991e9f067d5954cb6d6781 Add in a description element to the metadata
    a5dacabde5a622ce8ed1d1aa1ef165c46708502d add <head> and <title> to index

    proteus-> git log --since='2008-09-21' --pretty=format:"%h %s"
    0bb3dfb add link to twitter
    18f822e add contact page
    217a88e add the skeleton of an about page
    9a23464 rename to more appropriate name
    6f1bf6f Change biography link and add contact link
    4333289 add in a bio link
    4b53779 Add in a description element to the metadata
    a5dacab add <head> and <title> to index

- One can also give ranges with ..
- Oldest on the left hand side of ..
- ranges can be given with tags.

So this

    git log 1.0..HEAD

would show the changes between the 1.0 release to current.

### Operators on revisions:

- ^ gives the revision minus 1
- abcdef^   gives the rev before abcdef
- abcdef^^  gives 2 before ...

- ~N        subtracts N revisions
- abcdef~10 is 10 revs back

git will produce summary stats about changes:

    proteus-> git diff --stat 1.0
     about.html   |   15 +++++++++++++++
     contact.html |   23 +++++++++++++++++++++++
     hello.html   |   13 +++++++++++++
     index.html   |    9 ---------
     4 files changed, 51 insertions(+), 9 deletions(-)

----

### unstaging a change that is staged.

Recall it is a 2-step process; use reset HEAD to unstage the change in git.
However, this leaves the changes in the directory.
To reset to the previous version, follow with a checkout <file_name or master>

----

### undoing a committed change retaining history

    git revert HEAD

where HEAD names the revision to roll back to.  Any hash value may be used there.

this operation will leave a record of the commit, and the reversion in the log.

----

### undoing a committed change while deleting history

the reset command will when given a commit reference (a hash, branch, or a tag name):

- Rewrite the current branch to point to the specified commit
- Optionally reset the staging area to match the specified commit
- Optionally reset the working directory to match the specified commit

The advice is to use reset --hard.  However, there are caveats:

- only on local changes; resets pushed to shared repositories will confuse others

The lesson here is at: gitimmersion/git_tutorial/html/lab_17.html


----

### Blame

    git blame -L 6,+2 hello.html

will show lines 6 and 7 of hello.html

-L will also take a (POSIX) regexp

----

### Following Content

- use -M to blame to see content copied in files
- use -C -C to see entire files that have been copied.

        proteus-> git blame -M original.txt
        daac83ab (Jeff McCarrell 2010-11-08 15:36:36 -0800 1) This is the first line.
        daac83ab (Jeff McCarrell 2010-11-08 15:36:36 -0800 2) This happens to be the second line.
        daac83ab (Jeff McCarrell 2010-11-08 15:36:36 -0800 3) And this, it is the third and final line.
        daac83ab (Jeff McCarrell 2010-11-08 15:36:36 -0800 4) This is the first line.
        daac83ab (Jeff McCarrell 2010-11-08 15:36:36 -0800 5) This happens to be the second line.
        daac83ab (Jeff McCarrell 2010-11-08 15:36:36 -0800 6) And this, it is the third and final line.

E.g. if original.txt got copies to copy.txt, git shows:

        proteus-> git blame -C -C copy.txt
        daac83ab original.txt (Jeff McCarrell 2010-11-08 15:36:36 -0800 1) This is the first line.
        daac83ab original.txt (Jeff McCarrell 2010-11-08 15:36:36 -0800 2) This happens to be the second lin
        daac83ab original.txt (Jeff McCarrell 2010-11-08 15:36:36 -0800 3) And this, it is the third and fin
        daac83ab original.txt (Jeff McCarrell 2010-11-08 15:36:36 -0800 4) This is the first line.
        daac83ab original.txt (Jeff McCarrell 2010-11-08 15:36:36 -0800 5) This happens to be the second lin
        daac83ab original.txt (Jeff McCarrell 2010-11-08 15:36:36 -0800 6) And this, it is the third and fin

NB that original.txt, commit daac... is shown as the source of these lines.

another way to see this info:

        proteus-> git log -C -C -p -1
        commit 13145b5abfd843f7cb5026c2a3d0837862fd4771
        Author: Jeff McCarrell <jwm@emptech.com>
        Date:   Mon Nov 8 15:40:59 2010 -0800

            commit copy.txt

        diff --git a/original.txt b/copy.txt
        similarity index 100%
        copy from original.txt
        copy to copy.txt

----

### remote repositories

adding -r to git branch shows remote branches:

Here's the Dancer repository:

      proteus-> git branch -r
        origin/HEAD -> origin/master
        origin/after_filter
        origin/devel
        origin/feature/docs
        origin/feature/forward
        origin/headers
        origin/hooks
        origin/hot_fix_1.1901
        origin/hotfix/xml_test_fail
        origin/master
        origin/plack-middlewares
        origin/psgi-refactor
        origin/refactor/dtsimple-removal
        origin/refactoring/app

To sync changes from the remote repository into a local copy, use

    git pull <remote repository> <branch name without origin/>

Travis Swicegood uses the technique of pushing to his local private repositories
on multiple hosts to, eg, check cross platform code.
There is a blurb on pg 97 of the book.

The syntax to push is the same:

    git push <remote repo> <refspec>

In its simplest form, refspec is a tag, or a branch or a keyword like HEAD.
However, one can also name source:destination pairs like:

    git push origin mybranch:master

to push the changes from mybranch to the remote master.

The push moves to the repository, not to your working copy. So:

You have to run git checkout HEAD to pull all the latest changes from the repository to
your working tree.  This gives you an opportunity to handle any conflicts...

----

## Chap 8 Organizing Repositories

github notes:

after I requested a pull from Peter of my changes, the github instructions were:

Step 1: Check out a new branch to test the changes — run this from your project directory

    git checkout -b jmccarrell-master master

Step 2: Bring in jmccarrell's changes and test

    git pull https://jmccarrell@github.com/jmccarrell/upstream-gold.git master

Step 3: Merge the changes and update the server

    git checkout master
    git merge jmccarrell-master
    git push origin master

----

pull Peters changes in his master into my working tree:
What is peter's branch named?

guess:

    git pull git@github.com:Peterkools/upstream-gold.git master

which names the master of Peters repository.
This failed with a permissions error:

    capella-> git pull git@github.com:Peterkools/upstream-gold.git master
    ERROR: Permission to Peterkools/upstream-gold.git denied to jmccarrell/upstream-gold.
    fatal: The remote end hung up unexpectedly

However, using the http: access method succeeded:

    capella-> git pull https://jmccarrell@github.com/Peterkools/upstream-gold.git master
    Password:
    remote: Counting objects: 13, done.
    remote: Compressing objects: 100% (11/11), done.
    remote: Total 12 (delta 4), reused 0 (delta 0)
    Unpacking objects: 100% (12/12), done.
    From https://github.com/Peterkools/upstream-gold
     * branch            master     -> FETCH_HEAD
    Updating 8607e49..1629e4d
    Fast-forward
     schema/usell_taf.sql                  |  106 +++++++++++++++++++++++++++++++++
     schema/usell_temporary_dev_schema.sql |   90 ++++++++++++++++++++++++++++
     2 files changed, 196 insertions(+), 0 deletions(-)
     create mode 100644 schema/usell_taf.sql
     create mode 100644 schema/usell_temporary_dev_schema.sql

----

**Sun Feb 13 13:44:34 PST 2011**

gitref has a good section on remote access: http://gitref.org/remotes/

    git remote -v

lists the remote repositories one has cloned from:

    capella-> git remote -v
    origin	git@github.com:jmccarrell/upstream-gold.git (fetch)
    origin	git@github.com:jmccarrell/upstream-gold.git (push)

git fetch: sync with another repo:

> git fetch will synchronize you with another repo, pulling down any data that you do not have
    locally and giving you bookmarks to where each branch on that remote was when you
    synchronized. These are called "remote branches" and are identical to local branches
    except that Git will not allow you to check them out - however, you can merge from them,
    diff them to other branches, run history logs on them, etc. You do all of that stuff
    locally after you synchronize.

git pull == git fetch and get merge in 1 step.

the gitref author doesn't care for pull; he prefers explicit fetch and merge steps.

git push

    capella-> git push origin master
    Counting objects: 59, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (55/55), done.
    Writing objects: 100% (57/57), 172.50 KiB, done.
    Total 57 (delta 15), reused 0 (delta 0)
    To git@github.com:jmccarrell/upstream-gold.git
       8607e49..a1c00e6  master -> master

----

github key management help:  http://help.github.com/mac-key-setup/

----

So to add an entire tree of files  on capella and push them to an AWS instance, I did

on capella:

    git-add -A .
    git commit
    git push origin master

now the changes are in git-hub.

on ec2 instance:

    git fetch origin
    git merge origin

done.

my normal public key

jwm personal 2010/06/30

is already in use at github.

So to make a public key available at github, I will need a new ssh key

Can I store ssh keys in 1password?
  at a minimum I could as file attachments

----

how to do the equivalent of p4 sync -f in git:

    git checkout filename

this will checkout from HEAD, destroying all of the changes you have made.

there is also:

- git reset --hard filename
- git revert HEAD
- git revert HEAD^

see for reference:

- http://norbauer.com/notebooks/code/notes/git-revert-reset-a-single-file
- http://book.git-scm.com/4_undoing_in_git_-_reset,_checkout_and_revert.html

----

**Sun May  8 13:40:38 PDT 2011**

create working area for ML Big Data group project

follow directions at:

http://help.github.com/fork-a-repo/

So after I forked

    https://github.com/hackerdojoml/mrbigdata.git

I got

    git@github.com:jmccarrell/mrbigdata.git

Then I followed the directions and created the upstream remote and updated from there:

    capella-> git remote add upstream https://github.com/hackerdojoml/mrbigdata.git
    capella-> git fetch upstream
    From https://github.com/hackerdojoml/mrbigdata
     * [new branch]      master     -> upstream/master

----

**Tue Jun 14 18:18:47 PDT 2011**

to create a branch of code with a patch to cherry pick, I followed these
[helpful notes from arkx](https://github.com/mxcl/homebrew/issues/5404)

which boil down to:

@jmccarrell I created an own branch for io in homebrew, added codykrieger as a remote,
fetched his stuff and cherry-picked that exact commit. This is a fairly common pattern for
testing changes others have made that haven't been pulled to master yet. Here's the gist
of it with git commands:

    cd /usr/local
    git checkout -b io
    git remote add codykrieger https://github.com/codykrieger/homebrew.git
    git fetch codykrieger
    git cherry-pick 5224aff54264963b57df


So
    git checkout -b io

gets the io project into my local file system as an orphaned copy.

who owns the io branch?  is it just a local name?

    man git-checkout

says that -b (aka --orphan) creates a new orphaned branch.
The first commit made on this branch will have no parents,
and it will be the root of a new history totally disconnected
from all the other branches and commits.
So I have created a singleton off to the side here.

how do I list branches in git command line?

    git branch -r

will list remote branches.

----

**Tue Apr 14 15:56:08 PDT 2015**

## github

A key difference, or concept, in the github world that is different in the stash
world, (and perhaps in the bitbucket world?) is the *fork* concept.

git has no native fork command; this is a github-created concept.

So it follows that using forks when working with github is likely a good idea.

And, in fact, the github help recommends exactly that: [fork a repo](https://help.github.com/articles/fork-a-repo/)

----

**Mon Jun 22 12:17:06 PDT 2015**

# Sharing git repos on github / bitbucket / gitlab

- A common pattern I have is to start a new git repo, then push it up to a shared repository.
- so I do:
  - git init
  - create the repo on github / bitbucket / gitlab
  - then push

- the instructions from bitbucket are helpful

        cd /path/to/my/repo
        git remote add origin git@bitbucket.org:jmccarrell/jwm-ansible.git
        git push -u origin --all # pushes up the repo and its refs for the first time
        git push -u origin --tags # pushes up any tags

----

**Sat Oct  8 13:19:54 PDT 2016**

# locally modified (config) files not revision controlled

- to resolve storing my own mysql DB password in revision controlled dev_settings.py, I want to try this recipe:
  - [how do I keep a local version of files](http://stackoverflow.com/questions/11979634/how-do-i-keep-my-local-version-of-files-without-using-gitignore)
  - which boils down to:
  - `git update-index --assume-unchanged [file names]`
- well, that didn't work at all like I wanted.

```shell
$ git st
  ...
        modified:   filing/autofile/ca.py
$ git update-index --assume-unchanged tech/dev_settings.py
$ mv ~/Downloads/dev_settings.py  tech
$ git st
  ...
        modified:   tech/dev_settings.py
        modified:   filing/autofile/ca.py
```

- Ok, it looks like if I invert the order of operations, it might work.
- Nope, same result:

```
$ git st
  ...
        modified:   filing/autofile/ca.py
$ mv /c/davo/tmp/dev_settings.py tech/dev_settings.py
$ git st
  ...
        modified:   tech/dev_settings.py
        modified:   filing/autofile/ca.py
$ git update-index --assume-unchanged tech/dev_settings.py
$ git st
  ...
        modified:   tech/dev_settings.py
        modified:   filing/autofile/ca.py
```

- so try `--skip-worktree`
- that worked:

```
$ git st
  ...
        modified:   filing/autofile/ca.py
$ cp -p ~/Downloads/dev_settings.py tech/
$ git st
  ...
        modified:   tech/dev_settings.py
        modified:   filing/autofile/ca.py
$ git update-index --skip-worktree tech/dev_settings.py
$ git st
  ...
        modified:   filing/autofile/ca.py
```

- it remains to be seen whether or not this change persists across:
  - branches
  - pull
- so far, so good.  I have made new branches, and merged in upstream changes.

----

- good reference for git remote branch handling: [Advanced Git concepts; the upstream tracking branch](https://felipec.wordpress.com/2013/09/01/advanced-git-concepts-the-upstream-tracking-branch/)


### rebasing

- read the pro git chapter on rebasing

----

## [ignore local changes](http://www.virtuouscode.com/2011/05/20/keep-local-modifications-in-git-tracked-files/)

`git update-index --skip-worktree FILENAME`

----

## creating and applying patchs

- a nice overview: [How to create and apply a patch with Git](https://ariejan.net/2009/10/26/how-to-create-and-apply-a-patch-with-git/)

- create the patch from a dev branch:

$ git format-patch develop --stdout > /c/davo/tmp/s3-key-names.patch

- create a branchn in the target to test applying that patch.

$ git co -b feature_#137359471

- check out / test the patch to see if it will apply cleanly

```
$ git apply --stat /c/davo/tmp/s3-key-names.patch
 filing/autofile/ca_efile.py |   43 +++++++++++++++++++++++--------------------
 1 file changed, 23 insertions(+), 20 deletions(-)
```

- it turns out I had already applied that change:

```
$ git apply --check /c/davo/tmp/s3-key-names.patch
error: patch failed: filing/autofile/ca_efile.py:184
error: filing/autofile/ca_efile.py: patch does not apply
```

**Sat Feb 25 16:28:28 PST 2017**

## git from the bottom up ##

- looks like a very well written guide to understanding git internals.
- looks well worth my time.

### TOC ###

- IN PROGRESS John Wiegley's [git-from-the-bottom-up](https://github.com/jwiegley/git-from-the-bottom-up/blob/master/index.md)
  - √ [1-Repository](https://github.com/jwiegley/git-from-the-bottom-up/tree/master/1-Repository)
  - [2-The-index](https://github.com/jwiegley/git-from-the-bottom-up/tree/master/2-The-Index)
  - [3-Reset](https://github.com/jwiegley/git-from-the-bottom-up/tree/master/3-Reset)
  - [4-Stashing-and-the-reflog](https://github.com/jwiegley/git-from-the-bottom-up/blob/master/4-Stashing-and-the-reflog.md)
  - [5-Conclusion](https://github.com/jwiegley/git-from-the-bottom-up/blob/master/5-Conclusion.md)
  - [6-Further-Reading](https://github.com/jwiegley/git-from-the-bottom-up/blob/master/6-Further-Reading.md)

- IN PROGRESS recommends reading the git-rebase man page
  - I have read down to "Merge Strategies"

**Thu Jun 15 15:57:29 PDT 2017**

Jason Rosendale observed:

To add an empty commit that will automatically create a link to your PR in asana:
```
git commit --allow-empty -m 'https://app.asana.com/0/6641...'
```
To do a force-push that will only go through if nobody else has done a push since your last pull:
```
git push origin some_branch_that_is_not_master --force-with-lease
```
To see all changes that have been made to a particular file, in chronological order:
```
git log -p ./app/.../whatever.rb
```

Alex Deeb added:

One command I like to use to see the names of all files changed in a particular commit: `git diff-tree --no-commit-id --name-only -r {commit_sha}`u

----

[git scm blog on reset](https://git-scm.com/blog/2011/07/11/reset.html)

nicely identifies the 3 git trees:

Tree Roles
The HEAD	last commit snapshot, next parent
The Index	proposed next commit snapshot
The Working Directory	sandbox

**Fri Jul  5 16:24:17 PDT 2019 **
To reset a branch, eg, staging to master, do something like this:

```
git checkout staging
git reset --hard master
git push origin -u staging --force
```
