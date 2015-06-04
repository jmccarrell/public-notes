# Collaborating with Git

## TOC

### Videos

- √ Welcome and setup
- √ Getting started with hosted git repositories
- √ Downloading a remote repository
- √ Configuring git
- √ Getting started as a team of one
- √ Connecting to remote repositories
    - √ connecting
    - √ copying
    - √ converting
    - √ adding another
- √ Working with branches
    - √ working
    - √ listing all branches
    - √ using a different branch
    - √ establishing your branch strategy
    - √ creating a topic branch
    - √ uploading changes with git push
    - √ accepting and merging new work
    - √ dealing with merge conflicts
- √ Working with tags
    - √ working with tags
    - √ add, delete, list
    - √ check out tags
    - √ recovering from detached HEAD
    - √ sharing tags
- √ Finding and fixing bugs
    - find and fix
    - find relative history
    - find last working state with bisect
    - find author with blame
    - using stash
- √ Rollbacks, resets and undoing your work
    - √ using branches to experiment
    - √ amending a commit
    - √ removing changes to the working directory
    - √ removing commits with reset
    - √ promoting a previous commit with revert
- Rewiring history with rebase
    - bringing your work up to date with rebase
    - using rebase to combine several commits
    - using rebase to truncate a branch before merging
    - combining your changes into another branch with rebase
    - changing previous commits with interactive reabase
- Collaborating on github
- Collaborating on bitbucket


## remotes

    (pldev6)vega-> git remote show origin

shows useful info about the relationship with the remote, including what branches are
tracked.

## branches

- to start working locally on a remote branch:
    - git fetch: to get an up-to-date view
    - git branch -r: to see the remote branches available
        - say upstream/feature/tilesearch
    - then checkout that branch
    - git co --track upstream/feature/tilesearch

## checkout

- supports the --track / -t option to specify tracking of a remote at branch creation time.
    - see also `branch.autosetupmerge` config variable

- git commit --amend
    - lets you edit the message in the last commit made.
    - only really works for commits made locally; don't want to edit state in the shared space

- how to see if a local branch vs a remote branch are in sync:
    - git diff master..origin/master
    - git diff origin/master..master


## git permission strategies overview

- 4 common ways of setting up permissions
    - centralized
    - patched
    - forking
    - branching

### centralized

- mimic subversion / p4

### patched

- used for working on linux kernel
- they (linux kernel team) send patch files around in email
- very few people are allowed to actually make changes to teh blessed canonical version of the project

## forking

- a fork is a copy of the entire repo
- return code to main via either a pull request, or merge

## branch

- feature branchs off of the main repo
- does not include a fork
- but of course one can combine these models: fork + branch

- here is how to show changes between branchs:

    git log master..develop --oneline

## amend

- git commit --amend
    - update a particular commit in the repo
    - often used to 'touch-up' a commit; fix an oops

## remove changes to a working directory

- git reflog
    - show very granular operation history

## rollbacks and resets

### undoing a commit with reset

- git reset <commit_id>
    - will "undo" a commit; moving back to a prior time.
    - however, the commit is still there; see the reflog

## rebase

### bring your branch up to date

- git config --global rerere.enabled true
    - do this once and forget about it

- git log ..master
    - show changes outside of the area we are currently working on to be integrated

- git rebase master
    - bring in those changes

### combine multiple commits into a single

- choose the commit-id before the one(s) we want to eliminate.  then:
- git rebase -i <commit_id>
    - pick: leave as is
    - squash: keep the commit message; merge the commit output

### truncate a branch before merging

- she recommends bringing changes back into the mainline with merge, specifically, merge --no-ff

### combining your changes into another branch with rebase
