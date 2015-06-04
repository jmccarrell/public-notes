# More git notes

## More useful git sites:

- [Rypress Git Tutorial](http://rypress.com/tutorials/git/index.html)

## Rypress notes

useful for seeing commit history

    git log --oneline


## git branch

- from the git book, [Branch Management](http://git-scm.com/book/en/v2/Git-Branching-Branch-Management)

    - git branch --merged
    - git branch --no-merged

- these aren't as helpful in my experience as I first thought.

### remote branches

- [this](http://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) covers creating and
  sharing branches with remotes effectively.

The summary:

- to push my local branch up to the origin

        $ git push origin serverfix
          ...
         * [new branch]      serverfix -> serverfix

- to setup a local branch based on a new remote branch that you see in a fetch:

        $ git checkout -b serverfix origin/serverfix
        Branch serverfix set up to track remote branch serverfix from origin.
        Switched to a new branch 'serverfix'

- this creates a local tracking branch.  Tracking branches have a direct relationship
  to a remote branch, so `git pull` knows what to do.

- this is a common enough idiom that there is a command line shortcut to setup other tracking branches:

        $ git checkout --track origin/serverfix
        Branch serverfix set up to track remote branch serverfix from origin.
        Switched to a new branch 'serverfix'

- to set or change the remote, use the `-u/--set-upstream` option:

        $ git branch -u origin/serverfix
        Branch serverfix set up to track remote branch serverfix from origin.

- see tracking branch information

        vega-> git branch -vv
        * develop 57c7b9c [origin/develop] Add doc_type to ProductLoader interface.  doc_type is now a required parameter.
          master  672e2fe [origin/master] Merge pull request #107 from witlee/develop

- n.b. that this information is from the local copy only; to sync up all remotes
  for the completely up to date picture, do something like:

        vega-> git fetch --all; git branch -vv
        Fetching origin
        Fetching upstream
          ...
        * develop 57c7b9c [origin/develop] Add doc_type to ProductLoader interface.  doc_type is now a required parameter.
          master  672e2fe [origin/master] Merge pull request #107 from witlee/develop

- deleting remote branchs
    - add the --delete option to git push

             $ git push origin --delete serverfix
             To https://github.com/schacon/simplegit
              - [deleted]         serverfix

    - this just deletes the branch pointer from the remote.  it will typically live
      until a garbage collection run, so it is often easy to recover if accidentally
      deleted.
