This stackoverflow article gives a good overview of tutorials, it gives 4 references:
http://stackoverflow.com/questions/5844869/comprehensive-beginners-virtualenv-tutorial
http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv

Apparently Lion does not ship with virtualenv:

python --version
Python 2.7.1

python -m virtualenv
/usr/bin/python: No module named virtualenv

Notes from SimonOnSoftware: Virtualenv Tutorial {
http://simononsoftware.com/virtualenv-tutorial/

All packages installed via easy_install are global.
One tutorial recommends using

--no-site-packages

argument to virtualenv to, I think, create local copies inside the virtual env,
of site-packages.

here is a sample command:

virt@ymon:~$ virtualenv virt_env/virt2 --no-site-packages

After the virtualenv is created, one activates it:
One sources a file in the env that was created:

virt@ymon:~$ source virt_env/virt1/bin/activate

which I am sure sets path, etc.  It changes the prompt, to e.g.:
virt@ymon:~$

One can deactivate (leave) the virtualenv like this:
(virt1)virt@ymon:~$ deactivate

To see what is installed in a virtualenv
Simon says to use a thrid party package 'yolk' to see what packages are installed.

}

Notes from Chris Scott: A Primer on Virtualenv: {
http://iamzed.com/2009/05/07/a-primer-on-virtualenv/

Chris recommends installing virtualenv with easy_install:

$ sudo easy_install virtualenv

by default virtualenv will symlink to the site-packages.
To achieve more isolation, use --no-site-packages when creating the virtualenv

... activate ...

the main changes virtualenv makes are: {

VIRTUAL_ENV="/Users/chris/Documents/clients/mycoolproject"
export VIRTUAL_ENV

_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH
}

once the virtualenv is created and activated, Chris recommends installing packages
with easy_install, like this:

$ easy_install ipython

NB. no sudo.

Chris also likes pip; apparently for creating groups of packages.
Chris says pip is virtualenv-aware.
He sites this example:

    Check out the Pinax project’s installation docs for an example of this
    http://pinax.readthedocs.org/en/latest/index.html#development-instructions

Chris' tips:

- Use the virtualenvwrapper script to make working with and changing to/from multiple
  virtualenvs easy.
  http://www.doughellmann.com/projects/virtualenvwrapper/

Watch this screencast of virtualenvwrapper:
http://mathematism.com/2009/jul/30/presentation-pip-and-virtualenv/

this lists the interesting commands:

mkvirtualenv (create a new virtualenv)
rmvirtualenv (remove an existing virtualenv)
workon (change the current virtualenv)
add2virtualenv (add external packages in a .pth file to current virtualenv)
cdsitepackages (cd into the site-packages directory of current virtualenv)
cdvirtualenv (cd into the root of the current virtualenv)
deactivate (deactivate virtualenv, which calls several hooks)

pip:
pip is a replacement for easy_install that is virtualenv aware.
(written by the same guy I think)

there is a syntax for describing package requirements eg:

Django>=1.1
Pinax==0.5

it supports installing from tarballs, git, svn, ...

pip can install a bunch of stuff from a 'requirements' document (plain text)
pip freeze will write a requirements doc from a set of packages.

}

Find out what -u does for easy_install;
  saltycrane uses this to install virtualenv{,wrapper}
  sudo easy_install -U virtualenv
    --upgrade (-U)                 force upgrade (searches PyPI for latest
                                   versions)

Read about 'distribute'
  saltycrane likes this

Go read the documentation for virtualenvwrapper.

To create my dev environment, I think I want to:

install virtualenv, and virtualenvwrapper native in the installed python environment
  which is python 2.7 in my capella / lion environment

make a restdogs environment
make a pip requirements file for all of modules I need for restdogs
  pip

Looks like pip is not installed in python 2.7 by default
is it on dev2?  A: no

----

What is distribute and should I use it now?
documentation:
http://packages.python.org/distribute/

package home:
http://pypi.python.org/pypi/distribute

Notes from the docs page: {
Distribute is a fork of the Setuptools project.

Distribute is intended to replace Setuptools as the standard method for working with
Python module distributions.

For those who may wonder why they should switch to Distribute over Setuptools, it’s quite simple:

- Distribute is a drop-in replacement for Setuptools
- The code is actively maintained, and has over 10 commiters
- Distribute offers Python 3 support !

It appears that Distribute is how python packaging is done in python 3.

From: http://packages.python.org/distribute/setuptools.html

    Distribute is a collection of enhancements to the Python distutils (for Python 2.3.5
    and up on most platforms; 64-bit platforms require a minimum of Python 2.4) that allow
    you to more easily build and distribute Python packages, especially ones that have
    dependencies on other packages.
}

Read: The Hitchhiker’s Guide to Packaging¶
http://guide.python-distribute.org/index.html

Notes from HH Guide to Packaging: {

A python package is defined to be:

    A package is simply a directory with an __init__.py file inside it.

    This creates a package that can be imported using the import.

    Therefore, distutils was created to install packages into the PYTHONPATH with little
    difficulty.  PYTHONPATH == sys.path in code.

Traditionally, a developer groups related packages into an install tree, and then
adds that tree to PYTHONPATH so they can be imported.

The most convenient way to do this was to add a 'path configuration file' to an existing
directory in PYTHONPATH.

    Path configuration files have an extension of .pth, and each line must contain a
    single path that will be appended to sys.path.

    Paths can be absolute or relative, in which case they’re relative to the directory
    containing the .pth file. See the documentation of the site module for more
    information.

Also, two environment variables modify sys.path:

    PYTHONHOME  sets an alternate value for the prefix of the Python installation.

    PYTHONPATH  can be set to a list of paths that will be added to the beginning of sys.path.
                NB: directories must exist

Finally, sys.path is just a python list, so apps can modify it at will.

A python installation has a site-packages directory inside the module directory.
This is where user-installed packages are 'dropped.'
A .pth file in this directory is maintained.

jwm: I don't see any .pth files in my site-packages directories.

jwm: the intro pimps Distribute under 'Benefits of packaging'

http://guide.python-distribute.org/introduction.html#current-state-of-packaging
says: {

past:
  setuptools
  distutils

present:
  Distribute
  distutils
  distutils2

future:
  pip
  Standard Library

distutils:
  - is part of the the std lib
  - will be discontinued in Python 3.3
  - distutil2 will be backward compatible to 2.4 onward
  - will be part of std lib in python 3.3

    The distutils module provides the basics for packaging Python. Unfortunately, the
    distutils module is riddled with problems, which is why a small group of python
    developers are working on distutils2. However, until distutils2 is complete it is
    recommended that the Developer either use pure distutils or the Distribute package for
    packaging Python software.

    In the mean time, if a package requires the setuptools package, it is our
    recommendation that you install the Distribute package, which provides a more up to
    date version of setuptools than does the original Setuptools package.

    In the future distutils2 will replace setuptools and distutils, which will also remove
    the need for Distribute. And as stated before distutils will be removed from the
    standard library. For more information, please refer to the Future of Packaging.

    NB: Please use the Distribute package rather than the Setuptools package because there
    are problems in this package that can and will not be fixed.
}

Notes from: Installing the Package Tools: {
http://guide.python-distribute.org/installation.html

Distribute is the preferred mechanism.  Here is why:

    In the current state of packaging in Python, one needs a set of tools to easily
    manipulate the packaging ecosystem. There are two tools in particular that are
    extremely handy in the current ecosystem. There is a third tool, Virtual Environments,
    that will be discussed later in this documentation that will assist in isolating a
    packaging ecosystem from the global one. The combination of these tools will help to
    find, install and uninstall packages.

    Distribute is a collection of enhancements to the Python standard library module:
    distutils (for Python 2.3.5 and up on most platforms; 64-bit platforms require a
    minimum of Python 2.4) that allows you to more easily build and distribute Python
    packages, especially ones that have dependencies on other packages.

    Distribute was created because the Setuptools package is no longer
    maintained. Third-party packages will likely require setuptools, which is provided by
    the Distribute package. Therefore, anytime time a packages depends on the Setuptools
    package, Distribute will step in to say it already provides the setuptools module.

The preferred way to install Distribute is:

  wget http://python-distribute.org/distribute_setup.py
  python distribute_setup.py

Pip  (Pip install Python)

The other recommended tool is pip.

    The pip application is a replacement for easy_install. It uses mostly the same
    techniques for finding packages, so packages that were made easy_installable should be
    pip-installable as well.

pip installation:

    The Pip installer can be installed using the source tarball or using easy_install. The
    source tarball is the recommended method of installation.

    The latest version of the source tarball can be obtained from PyPI:

However, pypi.python.org points to a 'get pip' link, which says:
  http://www.pip-installer.org/en/latest/installing.html

    The recommended way to use pip is within virtualenv, since every virtualenv has pip
    installed in it automatically. This does not require root access or modify your system
    Python installation. For instance:

      $ curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py
      $ python virtualenv.py my_new_env
      $ . my_new_env/bin/activate
      (my_new_env)$ pip install ...

    When used in this manner, pip will only affect the active virtual environment. If you
    do want to install pip globally into your Python installation, see the instructions
    below.
}

So I have virtualenv installed on capella, having run easy_install virtualenv on Lion in
python 2.7: {
/Library/Python/2.7/site-packages/virtualenv-1.7.1.2-py2.7.egg/virtualenv.pyc
/Library/Python/2.7/site-packages/virtualenv-1.7.1.2-py2.7.egg/virtualenv_support
/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python/py2app/recipes/virtualenv.py
/System/Library/Frameworks/Python.framework/Versions/2.5/Extras/lib/python/py2app/recipes/virtualenv.pyc
/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/py2app/recipes/virtualenv.py
/System/Library/Frameworks/Python.framework/Versions/2.6/Extras/lib/python/py2app/recipes/virtualenv.pyc
/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/py2app/recipes/virtualenv.py
/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/py2app/recipes/virtualenv.pyc
/Users/jwm/tmp/virtualenv-where.out
/usr/local/bin/virtualenv

}

So go back to the HitchHikers guide and read about virtualenv: {
  Not much there.
}

HH Guide: Future of packaging: (very short): {
http://guide.python-distribute.org/future.html

    Inshort...
    setup.py gone!
    distutils gone!
    distribute gone!
    pip and virtualenv here to stay!
    eggs ... gone!

    See also http://bitbucket.org/tarek/distutils2/src/tip/docs/design/wiki.rst

which is a stale link.

Eventually I find the distutils2 docs page, which will be called 'packaging' in python 3.3
python 3.3 is in alpha circa 19 Mar 2012, so knowing how distutils2 works seems like
the thing to do.
}

However, the top level python docs page
http://python.org/doc/
specifically calls out the HH Guide to Packaging as official and supported.

}

Which python to use?  2 or 3? {
http://wiki.python.org/moin/Python2orPython3

    Short version: Python 2.x is the status quo, Python 3.x is the present and future of
    the language

    At the time of writing (July 4, 2010), the final 2.7 release is out, with a statement
    of extended support for this end-of-life release. The 2.x branch will see no new major
    releases after that. 3.x is under active development and has already seen stable
    releases, such as the recent 3.2. This means that all recent standard library
    improvements, for example, are only available in Python 3.x.

    Guido van Rossum (the original creator of the Python language) decided to clean up
    Python 2.x properly, with less regard for backwards compatibility than is the case for
    new releases in the 2.x range. The most drastic improvement is the better unicode
    support (with all text strings being unicode by default) as well as saner
    bytes/unicode separation.

    Besides, several aspects of the core language (such as print and exec being
    statements, integers using floor division) have been adjusted to be easier for
    newcomers to learn and to be more consistent with the rest of the language, and old
    cruft has been removed (for example, all classes are now new-style, range() returns a
    memory efficient iterable, not a list as in 2.x).

}

PEP 376 -- Database of Installed Python Distributions: {

http://python.org/dev/peps/pep-0376/
points to the future of packaging, and seems to endorse distutils2

Backward Compatibility and Roadmap: {
http://python.org/dev/peps/pep-0376/#backward-compatibility-and-roadmap

    These changes don't introduce any compatibility problems since they will be implemented in:

    - pkgutil in new functions
    - distutils2

    The plan is to include the functionality outlined in this PEP in pkgutil for Python
    3.2, and in Distutils2.

    Distutils2 will also contain a backport of the new pgkutil, and can be used for 2.4
    onward.

    Distributions installed using existing, pre-standardization formats do not have the
    necessary metadata available for the new API, and thus will be ignored. Third-party
    tools may of course to continue to support previous formats in addition to the new
    format, in order to ease the transition.
}

Seems like I don't have distutils2 on capella:
capella-> python -m distutils2.uninstall foobarbaz
/usr/bin/python: No module named distutils2
}

Official (latest?) Python Packaging Advice: {
http://docs.python.org/dev/packaging/

This is listed in the python 3.3a1 doc tree.
Is it in the 2.7.2 doc tree?  A: No.

The top level 'Distributing Python Modules'  link in the docs resolves to:
    3.3a1:    http://docs.python.org/dev/packaging/index.html

    3.2.2     http://docs.python.org/py3k/distutils/index.html
    (stable 3.x release)

    2.7.2:    http://docs.python.org/distutils/index.html
    (stable 2.x release)
}

So read the current stable packaging advice, both for package installers:
  Installing Python Modules
  Author:       Greg Ward
  Release:      2.7
  Date:         February 23, 2012
  http://docs.python.org/install/index.html
and package creators
  Distributing Python Modules
  Authors:      Greg Ward, Anthony Baxter
  Email:        distutils-sig@python.org
  Release:      2.7
  Date:         February 23, 2012
  http://docs.python.org/distutils/index.html

These likely won't have anything to say about virtualenvs.

Notes on Installing Python Modules: {
The document describes Distutils from the end-user's point of view.

Recommendation: use upstream packagers whenever possible: rpm, apt ...

This doc mostly describes installing from source distributions.

How to identify distributions that can work with distutils:
 - look for distros name and version number in the archive name: eg: tornado_tools-0.3.0.tar.gz
 - the distro will contain setup.py and README.txt or README

setup.cfg is the convention for python 3.3 packaging / distutils2 I think.

the standard recipe is thus:

python setup.py build
python setup.py install

If the defaults are used, install will put things in:

Platform    Standard installation location          Default value                           Notes
Unix        prefix/lib/pythonX.Y/site-packages      /usr/local/lib/pythonX.Y/site-packages  (1)
(pure)
Unix        exec-prefix/lib/pythonX.Y/site-packages /usr/local/lib/pythonX.Y/site-packages  (1)
(non-pure)

Notes:

1.  Most Linux distributions include Python as a standard part of the system, so prefix
    and exec-prefix are usually both /usr on Linux. If you build Python yourself on Linux
    (or any Unix-like system), the default prefix and exec-prefix are /usr/local.

to find prefix and exec_prefix, import them from sys and eval them:

For me on Lion I see:
>>> import sys
>>> print sys.prefix, sys.exec_prefix
/System/Library/Frameworks/Python.framework/Versions/2.7
/System/Library/Frameworks/Python.framework/Versions/2.7

on dev2 I see:
>>> print sys.prefix, sys.exec_prefix
/usr /usr


If you do not want or cannot install to the standard locations, then use an Alternate Installation

Alternate Installation

    The Distutils install command is designed to make installing module distributions to
    an alternate location simple and painless. The basic idea is that you supply a base
    directory for the installation, and the install command picks a set of directories
    (called an installation scheme) under this base directory in which to install
    files. The details differ across platforms, so read whichever of the following
    sections applies to you.

    Note that the various alternate installation schemes are mutually exclusive: you can
    pass --user, or --home, or --prefix and --exec-prefix, or --install-base and
    --install-platbase, but you can’t mix from these groups.

Alt Install: User scheme

    This scheme is designed to be the most convenient solution for users that don’t have
    write permission to the global site-packages directory or don’t want to install into
    it. It is enabled with a simple option:

    python setup.py install --user

Files will be installed into a subdirectories of site.USER_BASE, written below as userbase

which evals to:
>>> print site.USER_BASE
/Users/jwm/Library/Python/2.7

and
>>> print site.USER_BASE
/home/jwm/.local
as user jwm on dev2


As of this writing, that directory does not exist in my filesystem.

Here is where things get installed:
    Type of file        Installation directory
    modules             userbase/lib/pythonX.Y/site-packages
    scripts             userbase/bin
    data                userbase
    C headers           userbase/include/pythonX.Y/distname

    The advantage of using this scheme compared to the other ones described below is that
    the user site-packages directory is under normal conditions always included in
    sys.path (see site for more information), which means that there is no additional step
    to perform after running the setup.py script to finalize the installation.

    The build_ext command also has a --user option to add userbase/include to the compiler
    search path for header files and userbase/lib to the compiler search path for
    libraries as well as to the runtime search path for shared C libraries (rpath).

Alt Install: the home scheme

    The idea behind the “home scheme” is that you build and maintain a personal stash of
    Python modules. This scheme’s name is derived from the idea of a “home” directory on
    Unix, since it’s not unusual for a Unix user to make their home directory have a
    layout similar to /usr/ or /usr/local/. This scheme can be used by anyone, regardless
    of the operating system they are installing for.

    Installing a new module distribution is as simple as

    python setup.py install --home=<dir>

    To make Python find the distributions installed with this scheme, you may have to
    modify Python’s search path or edit sitecustomize (see site) to call site.addsitedir()
    or edit sys.path.

    The --home option defines the installation base directory. Files are installed to the
    following directories under the installation base as follows:

    Type of file        Installation directory
    modules             home/lib/python
    scripts             home/bin
    data                home
    C headers           home/include/python/distname

Alt Install: Unix (the prefix scheme)

    The “prefix scheme” is useful when you wish to use one Python installation to perform
    the build/install (i.e., to run the setup script), but install modules into the
    third-party module directory of a different Python installation (or something that
    looks like a different Python installation). If this sounds a trifle unusual, it
    is—that’s why the user and home schemes come before. However, there are at least two
    known cases where the prefix scheme will be useful.

    First, consider that many Linux distributions put Python in /usr, rather than the more
    traditional /usr/local. This is entirely appropriate, since in those cases Python is
    part of “the system” rather than a local add-on. However, if you are installing Python
    modules from source, you probably want them to go in /usr/local/lib/python2.X rather
    than /usr/lib/python2.X. This can be done with

    /usr/bin/python setup.py install --prefix=/usr/local

    Another possibility is a network filesystem where the name used to write to a remote
    directory is different from the name used to read it

    In either case, the --prefix option defines the installation base, and the
    --exec-prefix option defines the platform-specific installation base, which is used
    for platform-specific files. (Currently, this just means non-pure module
    distributions, but could be expanded to C libraries, binary executables, etc.) If
    --exec-prefix is not supplied, it defaults to --prefix. Files are installed as
    follows:

    Type of file        Installation directory
    Python modules      prefix/lib/pythonX.Y/site-packages
    extension modules   exec-prefix/lib/pythonX.Y/site-packages
    scripts             prefix/bin
    data                prefix
    C headers           prefix/include/pythonX.Y/distname

    There is no requirement that --prefix or --exec-prefix actually point to an alternate
    Python installation; if the directories listed above do not already exist, they are
    created at installation time.

    Incidentally, the real reason the prefix scheme is important is simply that a standard
    Unix installation uses the prefix scheme, but with --prefix and --exec-prefix supplied
    by Python itself as sys.prefix and sys.exec_prefix. Thus, you might think you’ll never
    use the prefix scheme, but every time you run python setup.py install without any
    other options, you’re using it.

    Note that installing extensions to an alternate Python installation has no effect on
    how those extensions are built: in particular, the Python header files (Python.h and
    friends) installed with the Python interpreter used to run the setup script will be
    used in compiling extensions. It is your responsibility to ensure that the interpreter
    used to run extensions installed in this way is compatible with the interpreter used
    to build them. The best way to do this is to ensure that the two interpreters are the
    same version of Python (possibly different builds, or possibly copies of the same
    build). (Of course, if your --prefix and --exec-prefix don’t even point to an
    alternate Python installation, this is immaterial.)

Custom Installation

    Sometimes, the alternate installation schemes described in section Alternate
    Installation just don’t do what you want. You might want to tweak just one or two
    directories while keeping everything under the same base directory, or you might want
    to completely redefine the installation scheme. In either case, you’re creating a
    custom installation scheme.

    To create a custom installation scheme, you start with one of the alternate schemes
    and override some of the installation directories used for the various types of files,
    using these options:

    Type of file        Override option
    Python modules      --install-purelib
    extension modules   --install-platlib
    all modules         --install-lib
    scripts             --install-scripts
    data                --install-data
    C headers           --install-headers

for more on this choice, see the doc.

Modifying Python’s Search Path

Looks like the best option here is to put values to be prepended to sys.path in the env
var PYTHONPATH.  The dirs must exist.

Distutils Configuration Files

Locations and names of config files

    On Unix and Mac OS X, the three configuration files (in the order they are processed) are:

    Type of file        Location and filename                           Notes
    system              prefix/lib/pythonver/distutils/distutils.cfg    (1)
    personal            $HOME/.pydistutils.cfg                          (2)
    local               setup.cfg                                       (3)

    Notes:

    1. Strictly speaking, the system-wide configuration file lives in the directory where
    the Distutils are installed; under Python 1.6 and later on Unix, this is as shown. For
    Python 1.5.2, the Distutils will normally be installed to
    prefix/lib/python1.5/site-packages/distutils, so the system configuration file should
    be put there under Python 1.5.2.

    2. On Unix, if the HOME environment variable is not defined, the user’s home directory
    will be determined with the getpwuid() function from the standard pwd module. This is
    done by the os.path.expanduser() function used by Distutils.

    3. I.e., in the current directory (usually the location of the setup script).

So it looks like I could specify a prefix for my packages in the setup.cfg for production
installations?

You can find out the complete set of options for any setup command using --help, eg:
once you have a reasonable setup.py file; an empty file will not do

    capella-> python setup.py build --help
    Common commands: (see '--help-commands' for more)

      setup.py build      will build the package underneath 'build/'
      setup.py install    will install the package

    Global options:
      --verbose (-v)  run verbosely (default)
      --quiet (-q)    run quietly (turns verbosity off)
      --dry-run (-n)  don't actually do anything
      --help (-h)     show detailed help message
      --no-user-cfg   ignore pydistutils.cfg in your home directory

    Options for 'build' command:
      --build-base (-b)  base directory for build library
      --build-purelib    build directory for platform-neutral distributions
      --build-platlib    build directory for platform-specific distributions
      --build-lib        build directory for all distribution (defaults to either
                         build-purelib or build-platlib)
      --build-scripts    build directory for scripts
      --build-temp (-t)  temporary build directory
      --plat-name (-p)   platform name to build for, if supported (default: macosx
                         -10.7-intel)
      --compiler (-c)    specify the compiler type
      --debug (-g)       compile extensions and libraries with debugging
                         information
      --force (-f)       forcibly build everything (ignore file timestamps)
      --executable (-e)  specify final destination interpreter path (build.py)
      --help-compiler    list available compilers

    usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
       or: setup.py --help [cmd1 cmd2 ...]
       or: setup.py --help-commands
       or: setup.py cmd --help
}

Notes on Distributing Python Modules: {

Overview of developer responsibilities:

 - write a setup script (setup.py by convention)
 - (optional) write a setup configuration file
 - create a source distribution
 - (optional) create one or more built (binary) distributions

A Simple Example

the setup script may be run multiple times during build/install, so keep it simple

for a foo module with one source file foo.py this setup.py suffices:

from distutils.core import setup
setup(name='foo',
      version='1.0',
      py_modules=['foo'],
     )

Notes:

 - most information that you supply to the Distutils is supplied as keyword arguments to
   the setup() function

 - those keyword arguments fall into two categories: package metadata (name, version
   number) and information about what’s in the package (a list of pure Python modules, in
   this case)

 - modules are specified by module name, not filename (the same will hold true for
   packages and extensions)

 - it’s recommended that you supply a little more metadata, in particular your name, email
   address and a URL for the project (see section Writing the Setup Script for an example)

Writing the Setup Script: {

To create a source distribution:

  python setup.py sdist

bdist_rpm will create an RPM:

  python setup.py bdist_rpm

You can find out what distribution formats are available at any time by running

  python setup.py bdist --help-formats

which on capella gives:

capella-> python setup.py bdist --help-formats
    List of available distribution formats:
      --formats=rpm      RPM distribution
      --formats=gztar    gzip'ed tar file
      --formats=bztar    bzip2'ed tar file
      --formats=ztar     compressed tar file
      --formats=tar      tar file
      --formats=wininst  Windows executable installer
      --formats=zip      ZIP file
      --formats=msi      Microsoft Installer
      --formats=egg      Python .egg file

on dev2:
    List of available distribution formats:
      --formats=rpm      RPM distribution
      --formats=gztar    gzip'ed tar file
      --formats=bztar    bzip2'ed tar file
      --formats=ztar     compressed tar file
      --formats=tar      tar file
      --formats=wininst  Windows executable installer
      --formats=zip      ZIP file

a package is defined to be:

  package
    a module that contains other modules; typically contained in a directory in the
    filesystem and distinguished from other directories by the presence of a file
    __init__.py.

  module distrubution
    a collection of Python modules distributed together as a single downloadable resource
    and meant to be installed en masse. Examples of some well-known module distributions
    are Numeric Python, PyXML, PIL (the Python Imaging Library), or mxBase. (This would be
    called a package, except that term is already taken in the Python context: a single
    module distribution may contain zero, one, or many Python packages.)

Here is the distutils setup.py:

#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='http://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
     )

NB the use of packages to name many sets of files to be included in this module distribution.

    The packages option tells the Distutils to process (build, distribute, install, etc.)
    all pure Python modules found in each package mentioned in the packages list.

It is possible to put the directories for packages elsewhere than .; use package_dir for this.

Relationships between Distribtions and Packages

    A distribution may relate to packages in three specific ways:

      1. It can require packages or modules.
      2. It can provide packages or modules.
      3. It can obsolete packages or modules.

    These relationships can be specified using keyword arguments to the
    distutils.core.setup() function.

Dependencies are expressed with setup keyword 'requires'.
Supplied packages are named with 'provides'.

Installing Scripts

Distutils will re-write the hash bang line:

    if the first line of the script starts with #! and contains the word “python”, the
    Distutils will adjust the first line to refer to the current interpreter location. By
    default, it is replaced with the current interpreter location. The --executable (or
    -e) option will allow the interpreter path to be explicitly overridden.

e.g. from PyXML:

setup(...
      scripts=['scripts/xmlproc_parse', 'scripts/xmlproc_val']
      )

Installing Package Data

use the package_data keyword.  See the docs for the format of package_data; it is non-trivial.

Installing Additional Files

data_files

specifies a sequence of (directory, files) pairs in the following way:

setup(...,
      data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
                  ('config', ['cfg/data.cfg']),
                  ('/etc/init.d', ['init-script'])]
     )

Note that you can specify the directory names where the data files will be installed, but
you cannot rename the data files themselves.

Additional meta-data

there is a lot of detail here:
http://docs.python.org/distutils/setupscript.html#additional-meta-data

a full list of the keywords
classifiers: which are categories of the module, eg Development Status :: 4 - Beta
versioning info, which is apparently complex.
  major.minor[.patch][sub]
  sub indicates
    alpha: a1, a2 ... aN
    beta:  b1, b2 ... bN
    final pre-release: pr1, pr2 ... prN

Debugging

the default is to write a simple error message.
define DISTUTILS_DEBUG to get a stack trace to find the error.
}

Writing the Setup Configuration File: {

setup.cfg

put infrequently used things here.
bdist_rpm is a particularly good candidate for this.

Here is distutils own bdist_rpm section of setup.cfg:

[bdist_rpm]
release = 1
packager = Greg Ward <gward@python.net>
doc_files = CHANGES.txt
            README.txt
            USAGE.txt
            doc/
            examples/
}

Creating a Source Distribution: {

show the commands supported by distutils: setup()
on Mac OS X: {
capella-> python setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  upload            upload binary package to PyPI
  check             perform some checks on the package

Extra commands:
  rotate            delete older distributions, keeping N newest files
  develop           install package in 'development mode'
  setopt            set an option in setup.cfg or another config file
  bdist_mpkg        create a Mac OS X mpkg distribution for Installer.app
  saveopts          save supplied options to setup.cfg or other config file
  egg_info          create a distribution's .egg-info directory
  py2app            create a Mac OS X application or plugin from Python scripts
  alias             define a shortcut to invoke one or more commands
  easy_install      Find/get/install Python packages
  bdist_egg         create an "egg" distribution
  install_egg_info  Install an .egg-info directory for the package
  test              run unit tests after in-place build

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help

}

on dev2 / Centos 5.8 final: {
dev2-> python setup.py --help-commands
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  upload            upload binary package to PyPI

Extra commands:
  rotate            delete older distributions, keeping N newest files
  develop           install package in 'development mode'
  setopt            set an option in setup.cfg or another config file
  saveopts          save supplied options to setup.cfg or other config file
  egg_info          create a distribution's .egg-info directory
  upload_docs       Upload documentation to PyPI
  alias             define a shortcut to invoke one or more commands
  easy_install      Find/get/install Python packages
  bdist_egg         create an "egg" distribution
  install_egg_info  Install an .egg-info directory for the package
  test              run unit tests after in-place build

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help

}

The tornado setup.cfg file: {
[egg_info]
tag_build =
tag_date = 0
tag_svn_revision = 0

}

the sdist command:
show the options available on OS X: {
Options for 'sdist' command:
  --formats         formats for source distribution (comma-separated list)
  --keep-temp (-k)  keep the distribution tree around after creating archive
                    file(s)
  --dist-dir (-d)   directory to put the source distribution archive(s) in
                    [default: dist]
  --help-formats    list available distribution formats

}

and on Centos: {
Options for 'sdist' command:
  --formats         formats for source distribution (comma-separated list)
  --keep-temp (-k)  keep the distribution tree around after creating archive
                    file(s)
  --dist-dir (-d)   directory to put the source distribution archive(s) in
                    [default: dist]
  --help-formats    list available distribution formats

}

Specifying which files to distribute

The defaults given here:
http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute
seem pretty reasonable.

If they don't work, use MANIFEST.in or MANIFEST to name each file in the distro.

There is a list of commands that MANIFEST.in supports, like:

include
exclude
recursive-include

at
http://docs.python.org/distutils/sourcedist.html#commands
}

Creating Built Distributions: {

http://docs.python.org/distutils/builtdist.html#creating-rpm-packages
gives quite a few options that would likely be very useful in creating an actual RPM via:
python setup.py bdist_rpm

The Postinstallation script
http://docs.python.org/distutils/builtdist.html#the-postinstallation-script

    Starting with Python 2.3, a postinstallation script can be specified with the
    --install-script option. The basename of the script must be specified, and the script
    filename must also be listed in the scripts argument to the setup function.

    This script will be run at installation time on the target system after all the files
    have been copied, with argv[1] set to -install, and again at uninstallation time
    before the files are removed with argv[1] set to -remove.

addtional functions defined for this script:

    directory_created(path)
    file_created(path)
      These functions should be called when a directory or file is created by the
      postinstall script at installation time. It will register path with the uninstaller,
      so that it will be removed when the distribution is uninstalled. To be safe,
      directories are only removed if they are empty.

    and some Microsoft specific functions.
}

Examples: {

There are a number of examples in the Distutils Cookbook: {
http://wiki.python.org/moin/Distutils/Cookbook

  - InstallDataScattered
    -- make resource data-files get installed in the same directory tree as the Python
       files that depend on them

  - AutoDataDiscovery
    -- specify data-files to install with smart_install_data recursively by specifying
       only a top-level directory

  - AutoPackageDiscovery
     -- specify packages to install recursively by specifying only the top-level package
}

Pure Python distribution (by package): {
http://docs.python.org/distutils/examples.html#pure-python-distribution-by-package

    If you have more than a couple of modules to distribute, especially if they are in
    multiple packages, it’s probably easier to specify whole packages rather than
    individual modules. This works even if your modules are not in a package; you can just
    tell the Distutils to process modules from the root package, and that works the same
    as any other package (except that you don’t have to have an __init__.py file).
}
}
}


Notes on the tornado-2.2 setup.{py,cfg}: {

the setup.py is pretty simple, and is a good template to follow.

the tornado __init__.py at
~/tmp/tornado-2.2/tornado/__init__.py
names these variables: {

#!/usr/bin/env python

"""The Tornado web server and tools."""

version = "2.2"
version_info = (2, 2, 0, 0)
}
}

Notes on tornado-2.2 tests: {
tornado/test/__init__.py
is the 0 length file.

dev2-> PYTHONPATH=`pwd` tornado/test/runtests.py
.................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 193 tests in 1.111s

OK
[I 120320 04:25:47 testing:372] PASS

I couldn't get the tests to put out any more info with  --log_to_stderr --logging=debug


dev2-> PYTHONPATH=`pwd` tornado/test/runtests.py --log_to_stderr --logging=debug
.................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 193 tests in 1.029s

OK
[I 120320 04:29:02 testing:372] PASS

Ben Darnell said he runs this is a shell window so the tests get executed on every file save:

  python -m tornado.autoreload -m tornado.test.runtests

so try this for restful dogs:

  python -m restful-dogs.kennel -m restful-dogs.test.runtests

I need to refactor the code to match this style.
}

----
install virtualenv on capella:

re-install python via pip: {
capella-> brew install python
==> Downloading http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tar.bz2
File already downloaded in /Library/Caches/Homebrew
==> Patching
patching file Lib/whichdb.py
Hunk #1 succeeded at 91 with fuzz 1.
==> ./configure --prefix=/usr/local/Cellar/python/2.7.2 --enable-shared
==> make
==> make install
==> Downloading http://pypi.python.org/packages/source/d/distribute/distribute-0.6.24.tar.gz
File already downloaded in /Library/Caches/Homebrew
==> /usr/local/Cellar/python/2.7.2/bin/python setup.py install
==> Caveats
A "distutils.cfg" has been written to:
  /usr/local/Cellar/python/2.7.2/lib/python2.7/distutils
specifing the install-scripts folder as:
  /usr/local/share/python

If you install Python packages via "python setup.py install", easy_install, pip,
any provided scripts will go into the install-scripts folder above, so you may
want to add it to your PATH.

Distribute has been installed, so easy_install is available.
To update distribute itself outside of Homebrew:
    /usr/local/share/python/easy_install pip
    /usr/local/share/python/pip install --upgrade distribute

See: https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python
==> Summary
/usr/local/Cellar/python/2.7.2: 4803 files, 81M, built in 2.2 minutes
}

Now install pip via easy_install: {
capella->  /usr/local/share/python/easy_install pip
Searching for pip
Reading http://pypi.python.org/simple/pip/
Reading http://pip.openplans.org
Reading http://www.pip-installer.org
Best match: pip 1.1
Downloading http://pypi.python.org/packages/source/p/pip/pip-1.1.tar.gz#md5=62a9f08dd5dc69d76734568a6c040508
Processing pip-1.1.tar.gz
Running pip-1.1/setup.py -q bdist_egg --dist-dir /var/folders/3k/nl_973r97cn49hkv83r9w6_40000gn/T/easy_install-wEFo37/pip-1.1/egg-dist-tmp-RIY0p6
warning: no files found matching '*.html' under directory 'docs'
warning: no previously-included files matching '*.txt' found under directory 'docs/_build'
no previously-included directories found matching 'docs/_build/_sources'
Adding pip 1.1 to easy-install.pth file
Installing pip script to /usr/local/share/python
Installing pip-2.7 script to /usr/local/share/python

Installed /usr/local/lib/python2.7/site-packages/pip-1.1-py2.7.egg
Processing dependencies for pip
Finished processing dependencies for pip
}

Then upgrade distribute: {
capella-> /usr/local/share/python/pip install --upgrade distribute
Downloading/unpacking distribute from http://pypi.python.org/packages/source/d/distribute/distribute-0.6.27.tar.gz#md5=ecd75ea629fee6d59d26f88c39b2d291
  Downloading distribute-0.6.27.tar.gz (624Kb): 624Kb downloaded
  Running setup.py egg_info for package distribute

Installing collected packages: distribute
  Found existing installation: distribute 0.6.24
    Uninstalling distribute:
      Successfully uninstalled distribute
  Running setup.py install for distribute
    Before install bootstrap.
    Scanning installed packages
    Setuptools installation detected at /usr/local/lib/python2.7/site-packages
    Non-egg installation
    Removing elements out of the way...
    Already patched.
    /usr/local/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg-info already patched.

    Installing easy_install script to /usr/local/share/python
    Installing easy_install-2.7 script to /usr/local/share/python
    After install bootstrap.
    /usr/local/Cellar/python/2.7.2/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg-info already exists
Successfully installed distribute
Cleaning up...
}

Now install virtualenv and virtualenvwrapper in my brew-built python tree: {
capella-> pip install virtualenv
Downloading/unpacking virtualenv
  Downloading virtualenv-1.7.1.2.tar.gz (2.1Mb): 2.1Mb downloaded
  Running setup.py egg_info for package virtualenv

    warning: no previously-included files matching '*.*' found under directory 'docs/_templates'
Installing collected packages: virtualenv
  Running setup.py install for virtualenv

    warning: no previously-included files matching '*.*' found under directory 'docs/_templates'
    Installing virtualenv script to /usr/local/share/python
Successfully installed virtualenv
Cleaning up...
capella-> pip install virtualenvwrapper
Downloading/unpacking virtualenvwrapper
  Downloading virtualenvwrapper-3.4.tar.gz (795Kb): 795Kb downloaded
  Running setup.py egg_info for package virtualenvwrapper

Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/local/lib/python2.7/site-packages (from virtualenvwrapper)
Installing collected packages: virtualenvwrapper
  Running setup.py install for virtualenvwrapper

    changing mode of build/scripts-2.7/virtualenvwrapper.sh from 644 to 755
    changing mode of build/scripts-2.7/virtualenvwrapper_lazy.sh from 644 to 755
    Skipping installation of /usr/local/Cellar/python/2.7.2/lib/python2.7/site-packages/virtualenvwrapper/__init__.py (namespace package)
    Installing /usr/local/Cellar/python/2.7.2/lib/python2.7/site-packages/virtualenvwrapper-3.4-py2.7-nspkg.pth
    changing mode of /usr/local/share/python/virtualenvwrapper.sh to 755
    changing mode of /usr/local/share/python/virtualenvwrapper_lazy.sh to 755
Successfully installed virtualenvwrapper
Cleaning up...
}

Wire in virtualenv wrapper:
add to .bash_profile:

# set up virtualenv when installed
for p in /usr/local/share/python /usr/local/bin /usr/bin; do
    if [ -f "$p/virtualenvwrapper.sh" ]; then
        export WORKON_HOME=$HOME/.virtualenvs
        export PROJECT_HOME=/proj
        source "$p/virtualenvwrapper.sh"
    fi
done
unset p

----------------
fix up virtualenv wrapper startup on capella. {
Sat Apr 20 17:27:01 PDT 2013

The error I am getting now: {
Last login: Sat Apr 20 13:52:23 on ttys002
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named virtualenvwrapper.hook_loader
virtualenvwrapper.sh: There was a problem running the initialization hooks.

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenv has been installed for
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python and that PATH is
set properly.
}

which can be repeated:
capella-> /usr/local/share/python/virtualenvwrapper.sh
  ...
ImportError: No module named virtualenvwrapper.hook_loader

So try to re-install virtualenvwrapper from scratch:
Well, actually upgrade it: {
capella-> pip install --upgrade virtualenv
Downloading/unpacking virtualenv from http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz#md5=07e09df0adfca0b2d487e39a4bf2270a
  Downloading virtualenv-1.9.1.tar.gz (2.0MB): 2.0MB downloaded
  Running setup.py egg_info for package virtualenv

    warning: no previously-included files matching '*' found under directory 'docs/_templates'
    warning: no previously-included files matching '*' found under directory 'docs/_build'
Installing collected packages: virtualenv
  Found existing installation: virtualenv 1.7.1.2
    Uninstalling virtualenv:
      Successfully uninstalled virtualenv
  Running setup.py install for virtualenv

    warning: no previously-included files matching '*' found under directory 'docs/_templates'
    warning: no previously-included files matching '*' found under directory 'docs/_build'
    Installing virtualenv script to /usr/local/share/python
    Installing virtualenv-2.7 script to /usr/local/share/python
Successfully installed virtualenv
Cleaning up...
}

upgrade virtualenvwrapper: {
capella-> pip install --upgrade virtualenvwrapper
Downloading/unpacking virtualenvwrapper from http://pypi.python.org/packages/source/v/virtualenvwrapper/virtualenvwrapper-3.7.1.tar.gz#md5=17fd8cfe4ef7f569f62f2f3453e3bc02
  Downloading virtualenvwrapper-3.7.1.tar.gz (185kB): 185kB downloaded
  Running setup.py egg_info for package virtualenvwrapper

Requirement already up-to-date: virtualenv in /usr/local/lib/python2.7/site-packages (from virtualenvwrapper)
Downloading/unpacking virtualenv-clone (from virtualenvwrapper)
  Downloading virtualenv-clone-0.2.4.tar.gz
  Running setup.py egg_info for package virtualenv-clone

Downloading/unpacking stevedore (from virtualenvwrapper)
  Downloading stevedore-0.8.tar.gz (94kB): 94kB downloaded
  Running setup.py egg_info for package stevedore

    warning: no files found matching '*.py' under directory 'tests'
Requirement already up-to-date: distribute in /usr/local/lib/python2.7/site-packages/distribute-0.6.36-py2.7.egg (from stevedore->virtualenvwrapper)
Installing collected packages: virtualenvwrapper, virtualenv-clone, stevedore
  Found existing installation: virtualenvwrapper 3.4
    Uninstalling virtualenvwrapper:
      Successfully uninstalled virtualenvwrapper
  Running setup.py install for virtualenvwrapper

    changing mode of build/scripts-2.7/virtualenvwrapper.sh from 644 to 755
    changing mode of build/scripts-2.7/virtualenvwrapper_lazy.sh from 644 to 755
    Skipping installation of /usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/virtualenvwrapper/__init__.py (namespace package)
    Installing /usr/local/Cellar/python/2.7.3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/virtualenvwrapper-3.7.1-py2.7-nspkg.pth
    changing mode of /usr/local/share/python/virtualenvwrapper.sh to 755
    changing mode of /usr/local/share/python/virtualenvwrapper_lazy.sh to 755
  Running setup.py install for virtualenv-clone

    Installing virtualenv-clone script to /usr/local/share/python
  Running setup.py install for stevedore

    warning: no files found matching '*.py' under directory 'tests'
Successfully installed virtualenvwrapper virtualenv-clone stevedore
Cleaning up...
}

NB that this is installing to /usr/local/share/python, not to the system python.
But I believe the system python has to be involved in creating the virtual env.

So to get pip installed natively for the system level python,
I follow the directions here:
http://guide.python-distribute.org/installation.html

which tell me to install pip from sources; but that advice seems outdated.

But, I follow the trail to:
http://www.pip-installer.org/en/latest/installing.html

where I am told that virtualenv will install pip. :-/

So maybe the correct sequence is:

install virtualenv in the global space
use virtualenv to create an environment that contains:
  virtualenvwrapper
  distribute
  pip

so read the docs on virtualenv to get the latest low down:
http://virtualenv.readthedocs.org/en/latest/

virtualenv has support for installing itself to the global environment:

    To install globally from source:

    $ curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz
    $ tar xvfz virtualenv-X.X.tar.gz
    $ cd virtualenv-X.X
    $ [sudo] python setup.py install


virtualenv can work without virtualenvwrapper, of course.
So see what support, if any, OS X and centos have for virtualenv natively:

centos yum has none:
[ec2-user@domU-12-31-39-0A-1E-E3 ~]$ sudo yum search python | grep -i virtual
[ec2-user@domU-12-31-39-0A-1E-E3 ~]$ sudo yum search virtualenv
  ...
No Matches found
[ec2-user@domU-12-31-39-0A-1E-E3 ~]$


os x brew has none:
capella-> brew search virtualenv
No formula found for "virtualenv". Searching open pull requests...

So natively on my OS X machine, install virtualenv from pypi as source.
I considered not choosing to support setuptools; to only support distribute, which is the future.
I decided to try this first, to see what would happen for me.
This will create a pip in the system directory as well.

So following the pattern above, I have: {

cd ~/tmp
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1

first try the install without sudo to see what happens.  I am sure I will need sudo...

then install it with sudo:

capella-> sudo python setup.py install
running install
running bdist_egg
  ...
creating /Library/Python/2.7/site-packages/virtualenv-1.9.1-py2.7.egg
Extracting virtualenv-1.9.1-py2.7.egg to /Library/Python/2.7/site-packages
Adding virtualenv 1.9.1 to easy-install.pth file
Installing virtualenv script to /usr/local/bin
Installing virtualenv-2.7 script to /usr/local/bin

Installed /Library/Python/2.7/site-packages/virtualenv-1.9.1-py2.7.egg
Processing dependencies for virtualenv==1.9.1
Finished processing dependencies for virtualenv==1.9.1
}

So now I have 2 versions of virtualenv installed:

capella-> ls -lh $(which virtualenv)
-rwxr-xr-x  1 jwm  admin   415B Apr 20 13:59 /usr/local/share/python/virtualenv*
capella-> ls -lh /usr/local/bin/virtualenv
-rwxr-xr-x  1 root  admin   276B Apr 20 15:17 /usr/local/bin/virtualenv*

They are both 1.9.1, but this is confusing at best.

So now if I create a virtual env, that will install a pip.

Do I have pip installed globally?
A: Not clear; I see this one:

capella-> which pip
/usr/local/share/python/pip
capella-> pip --version
pip 1.2 from /usr/local/lib/python2.7/site-packages/pip-1.2-py2.7.egg (python 2.7)

but this is the old version that does not use SSL to install packages:
(from virtualenv pypi site, and elsewhere):

    When using pip to install virtualenv, we advise using pip-1.3 or greater. Prior to
    version 1.3, pip did not not download from PyPI over SSL.

So what if I use pip to upgrade pip?

Ok, that worked: {
capella-> pip install --upgrade pip
  ...
    Installing pip script to /usr/local/share/python
    Installing pip-2.7 script to /usr/local/share/python
Successfully installed pip
Cleaning up...
capella-> pip --version
pip 1.3.1 from /usr/local/lib/python2.7/site-packages/pip-1.3.1-py2.7.egg (python 2.7)
capella-> which pip
/usr/local/share/python/pip
}

So now I have pip, virtualenv and virtualenvwrapper all upgraded to the latest.
But I have multiple copies, some of which were configured to find the non-system python.

----------------
DONE So go delete the brew python altogether, to leave only snow leopard python 2.7.2 in place.
I deleted an old /usr/local/bin/pip as well.

Now there is no pip, but I do have a virtualenv that appears to be the updated version
and appears to work.

So how do I use virtualenv to create a complete environment?
A: I don't want to.  Use virtualenvwrapper like I have done before.
Install pip globally, then use pip to install virtualenvwrapper, then create ffdev...
That worked.
}
