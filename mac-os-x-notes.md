## users and groups:

To create groups and users, follow this example which creates an oracle user and dba group:

I use 4200 as GID and UID so checking if they are available (Updated on 19-Apr-09: Thanks Gleb!):

        macbook:~ gorby$ dscl . -list /groups gid | grep 4200
        macbook:~ gorby$ dscl . -list /users uid | grep 4200
        macbook:~ gorby$


        sudo dscl . -create /groups/dba
        sudo dscl . -append /groups/dba gid 4200
        sudo dscl . -append /groups/dba passwd "*"
        sudo dscl . -create /users/oracle
        sudo dscl . -append /users/oracle uid 4200
        sudo dscl . -append /users/oracle gid 4200
        sudo dscl . -append /users/oracle shell /bin/bash
        sudo dscl . -append /users/oracle home /Users/oracle
        sudo dscl . -append /users/oracle realname "Oracle software owner"
        sudo dscl . -append /Groups/dba GroupMembership oracle
        sudo mkdir /Users/oracle
        sudo chown oracle:dba /Users/oracle
        sudo defaults write /Library/Preferences/com.apple.loginwindow HiddenUsersList -array-add oracle
        sudo passwd oracle

## dns cache flush

To flush the dns cache, which can be helpful in VPN situations:

        dscacheutil -flushcache

## dns servers

To see the DNS servers for a given network service

        proteus-> networksetup -getdnsservers Wi-Fi
        There aren't any DNS Servers set on Wi-Fi.

to see all of the network services:

        proteus-> networksetup -listallnetworkservices
        An asterisk (*) denotes that a network service is disabled.
        Bluetooth DUN
        Ethernet
        USB Ethernet
        FireWire
        Wi-Fi

----

**Sun Jun 28 21:03:06 PDT 2015**

## mdfind

- does mdfind index my markdown documents?
    - A: no
    - [Mac OS: index source code](http://amitp.blogspot.com/2014/06/mac-os-index-source-code.html)
        - gives an overview of the problem and the solution
        - this creates an "app" that registers common programming file extensions
        - then mdfind will have them in the index to search against

- Ok, so set it up so .md files get indexed.
    - follow the recipe Amit layed out above

- duti (brew will install it) is a tool to manage the *d*efault UTI mapping
    - man duti
    - appears to be worth the read.
    - in particular, it looks like Xcode currently wants to manage .md files

            $ duti -x .md
            Xcode.app
            /Applications/Xcode.app
            com.apple.dt.Xcode

- here is how to see lots of mapping detail mac os x keeps:

        $ $(mdfind -name lsregister) -dump

- launch service register

- Ok, in finder, I opened file info on a .md file, then in that gui, chose marked2 as
  the app to handle it.

- but mdfind will still not index my .md files

        $ mdfind -onlyin /j/notes clone
        /j/notes/python-virtualenv-notes.txt
        /j/notes/restful-dogs-dev-notes.txt
        /j/notes/perl-threads.txt
        /j/notes/oracle-concepts-notes.txt
        /j/notes/move-to-the-cloud.txt
        /j/notes/mercurial-notes.txt
        /j/notes/blackbelt-factory-java-notes.txt
        /j/notes/ampcamp-2012-notes.txt
        /j/notes/today-todo-2011.txt
        /j/notes/today-todo-2012.txt
