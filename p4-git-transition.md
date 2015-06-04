# Action Items

- merge notes on proteus back through main to gather my notes together
- merge notes from Dropbox

- delete p4 home clients
    - jwm-home-MAIN-capella
    - jwm-home-MAIN-proteus
    - jwm-home-capella


- remove proteus clients:
    - jwm-www-proteus
    - jwm-proj-books-proteus
    - jwm-notes-proteus
    - jwm-notes-MAIN-proteus
    - jwm-localnotes-proteus


- clean up jwm-www
    - rm bikes/ktm520

- mv jwm-www to Dropbox
    - remove from proteus
    - rm from capella
    - p4 delete those clients

- transition /j/sw licenses into 1password

- Tear down p4tunnel

## Group by project
- home directory
- notes
- 1 per client
- 1 per coursera course

# Transition projects to git

## Existing p4 clients:
`p4 clients | perl -ne 'print $1, "\n" if m{\AClient\s([\w-]+)}'`

- jwm-capella-home-proteus
- jwm-coursera-ml-capella
- jwm-coursera-stats-one-capella
- jwm-notes-MAIN-capella
- jwm-notes-capella
- jwm-notes-public-capella
- jwm-proj-blackbeltfactory-capella
- jwm-proj-blueprint-css-work-capella
- jwm-proj-books-capella
- jwm-restful-dogs-capella
- jwm-software-capella
- jwm-www-capella
- jwm-www-ng-capella



## Existing p4 projects:

### proteus

#### /j

- /j/home-capella/.p4config
- /j/home-MAIN/.p4config
- /j/lnotes/.p4config
- /j/MAIN-notes/.p4config
- /j/notes/.p4config
- /j/proj/books/.p4config
- /j/proj/ml-cs229/.p4config
- /j/www/.p4config

#### home

- /Users/jmccarre/.p4config

### capella

#### /j ####

* /j/MAIN-notes/.p4config
* /j/notes/.p4config
* /j/pdata/.p4config
* /j/proj/bbf/.p4config
* /j/proj/blueprint-css-work/.p4config
* /j/proj/books/.p4config
* /j/proj/coursera/machine-learning/.p4config
* /j/proj/coursera/stats-one/.p4config
* /j/proj/jwm-home-MAIN/.p4config
* /j/proj/restful-dogs/.p4config
* /j/public-notes/.p4config
* /j/sw/.p4config
* /j/www/.p4config
* /j/www-ng/.p4config

#### home ####

* /Users/jwm/.p4config

# Completed Items

## Reduce surface area stored in my p4 instance

- DELETED jwm-qidtrace-capella

- DELETED jwm-discern-capella
- DELETED jwm-proj-ezdriving-capella


### delete all invino and jolata clients

- DELETED jwm-invino-dev-capella
- DELETED jwm-invino-import-capella
View:
	//jwm-depot/clients/invino/src/import/... //jwm-invino-import-capella/...
- DELETED jwm-invino-main-capella
- DELETED jwm-invino-notes-capella
Root:	/c/invino/notes
View:
	//jwm-depot/clients/invino/notes/... //jwm-invino-notes-capella/...

- DELETED jwm-jolata-notes-capella
- DELETED jwm-home-jolata-capella
- DELETED jwm-home-jolata-dev

### tear down unneeded clients

- DELETED jwm-home-dev2-invino
	//jwm-depot/homes/dev2-invino/... //jwm-home-dev2-invino/...

- DELETED jwm-restful-dogs-dev2

- DELETED jwm-snapgear-negheb
	//jwm-depot/snapgear/... //jwm-snapgear-negheb/...

- DELETED jwm-software-leda

- DELETED jwm-software-negheb
	//jwm-depot/software/... //jwm-software-negheb/...


### DONE tear down jolata host clients

- DONE jwm-home-buster-dev
- DONE jwm-home-romo
- DONE jwm-home-romo-dev


## Other Done

- DONE I need a way to move PII that is only available on proteus to capella.
    - A: Dropbox or usb stick
- DONE verify arq is backing up contents of ~/Dropbox

## YES DONE Use bitbucket
- Use [bitbucket.org](https:bitbucket.org): git repo manangement, in the cloud.  Free unlimited private repos.
- Do I have an account?
    - A: yes, and I have provisioned my ssh key there.
- How are backups of the git repos done?  Ie, how do I control/own the data.  What happens
  if bitbucket goes away?  How do I backup all of my bitbucket hosted repos?
    - A: https://confluence.atlassian.com/pages/viewpage.action?pageId=288658413
    - A2: read this again and consider the ramifications
- Today I backup (well, I don't actually) my p4 repo as a unit; everthing I have there
  is managed by me.


- NO USE bitbucket.  Figure out how people use git to sync between machines without a github-like server
    - git immersion had the server lesson
    - try that technique on /j/proj/books
        - between proteus and capella
    - git on sneaker net
        - make a .git repot on a usb stick
        - sync to that stick
        - sync the next client?
- NO Check out Kiln as another choice to consider vs. bitbucket.
    - A: No, kiln is $25/user/month, so I prefer a free 5-user bitbucket account.

# Goal
- reduce hassle merging changes between similiar files I keep many places
    - environment: emacs, bash, src
    - *.cpt files
- remove PII from exposure to the public internet as clear text
- reduce the risk / cost of losing my mcc.org server


# Things to take care of
- Eliminate complex merging of /j/notes, home
- Figure out how good git is at handling binary (encrypted) files

- Does every "project" I work on have its own git repository?  I.e. Is the namespace flat?
  `jmccarrell/flat-namespace-here?`
    - Essentially, yes.  There are git submodules, but Jack warned me off of them.
      Bite the bullet and choose a naming scheme that works with a flat namespace.
