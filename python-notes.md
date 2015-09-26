## pydoc notes

        capella-> pydoc readline

or write HTML output:

        capella-> pydoc -w atexit
        wrote atexit.html

or start a web server listening on a port:

        pydoc -p 5001

then browse at

        http://localhost:5001/

## doctest notes

an interesting way to convert strings to python types:

        s = "GOOG,100,623.45"
        field_types = [str, int, float]
        fields = [ty(val) for ty, val in zip(field_types, s.split(','))]
        fields
        ['GOOG', 100, 623.45]

python does support decimal arithmetic via the decimal module.

the sum(seq, initial) operator takes an initial value.
the type of the initial value usually determines the type of the result.
type conversion is apparently not done between the values to be summed:

        >>> pprint(l)
        [Decimal('24.5'), 25.5]
        >>> print sum(l)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: unsupported operand type(s) for +: 'Decimal' and 'float'
        >>> print sum(l, Decimal(0))
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: unsupported operand type(s) for +: 'Decimal' and 'float'

the ternary operator is called 'conditional expression evaluation', and is written

        a if condition else b

        >>> l = [ 23, 123, 56 ]
        >>> capped = [ 75 if v > 75 else v for v in l ]
        >>> capped
        [23, 75, 56]

use the enumerate function to supply sequence indices


        >>> for i in xrange(501, 801, 100):
        ...   print i
        ...
        501
        601
        701
        >>> for i in enumerate(xrange(501, 801, 100)):
        ...   print i
        ...
        (0, 501)
        (1, 601)
        (2, 701)

use itertools.izip to combine two sequences together one at a time
without buffering them all in memory as zip does.

the for statement can take an else clause, which is executed at the end
of the for loop if it was not exited via break:

        # ensure we found a blank line that signals a section  separator
        for line in open("foo.txt"):
          stripped = line.strip()
          if not stripped:
            break
          # process line
        else:
          raise RuntimeError("Missing section separator")

use raise by itself to re-raise an exception in a handler

        assert(expr, msg)

can be used to make assertions in code

        if __debug__:
          stmts

can be used as well.

When the optimize flag (-O) is passed to the interpreter, these __debug__ statments are
eliminated from the byte code, minimizing the runtime effect.
The bottom line is that they support an assertion style of defensive programming.

any function that calls yield is a generator

## Exceptions

python is block scoped, so any variables set inside the try, except, else or finally
blocks are available outside that scope.

The general form of try is:

        (in_except, in_else, in_fin) = (False, False, False)
        try:
            foo = "foo set in try"
        except:
            foo = "foo set in except"
            in_except = True
        else:
            foo = "foo set in else"
            in_else = True
        finally:
            foo = "foo set in finally"
            in_fin = True

        print(foo)
        print(in_except, in_else, in_fin)

which gives:

        python3 try-scoping.py
        foo set in finally
        except: False; else: True; fin: True


A file example:

        for arg in sys.argv[1:]:
            try:
                f = open(arg, 'r')
            except IOError:
                print('cannot open', arg)
            else:
                print(arg, 'has', len(f.readlines()), 'lines')
                f.close()


the finally clause is executed _before_ the exception, if any, is handled

Here is what [the manual](https://docs.python.org/3.4/tutorial/errors.html#defining-clean-up-actions) says about finally:

> A finally clause is always executed before leaving the [try](https://docs.python.org/3.4/reference/compound_stmts.html#try) statement, whether an exception has occurred or not. When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in a except or else clause), it is re-raised after the finally clause has been executed. The finally clause is also executed “on the way out” when any other clause of the try statement is left via a break, continue or return statement.


So if we raise an exception in our prior example,

        (in_except, in_else, in_fin) = (False, False, False)
        try:
            foo = "foo set in try"
            # raise Exception()
        except:
            foo = "foo set in except"
            in_except = True
        else:
            foo = "foo set in else"
            in_else = True
        finally:
            foo = "foo set in finally"
            in_fin = True

        print(foo)
        print("except: {0}; else: {1}; fin: {2}".format(in_except, in_else, in_fin))

 we get this:

        python3 try-scoping.py
        foo set in finally
        except: True; else: False; fin: True

----

virtualenv installation on capella

first read the [homebrew advice](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md)

capella-> brew search pip
aespipe	    brew-pip	lesspipe    spiped	pipeviewer

If you meant `pip' precisely:

Install pip with easy_install:

    easy_install pip

capella-> sudo easy_install pip
capella-> sudo pip install virtualenvwrapper

Then add the bashrc glue:
      export WORKON_HOME=$HOME/.virtualenvs
      export PROJECT_HOME=/proj
      source /usr/local/bin/virtualenvwrapper.sh


----
python virtualenv for ffdev work on proteus:

first install python with brew
read homebrew advice Homebrew-and-Python above: {

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
}

So that is what I did:
add /usr/local/share/python to $PATH
installed easy_install
upgraded distribute.

After this step I have:

sfo-mp8n0-> ls -l /usr/local/share/python/
total 32
-rwxr-xr-x  1 jmccarre  staff   349B May 25 01:28 easy_install*
-rwxr-xr-x  1 jmccarre  staff   357B May 25 01:28 easy_install-2.7*
-rwxr-xr-x  1 jmccarre  staff   301B May 25 01:28 pip*
-rwxr-xr-x  1 jmccarre  staff   309B May 25 01:28 pip-2.7*

----
Now I want to install virtualenvwrapper

http://www.doughellmann.com/projects/virtualenvwrapper/
says I have to install virtualenv separately.
So do that:

pip install virtualenv
  ...
    Installing virtualenv script to /usr/local/share/python

then back to v-e-wrapper

pip install virtualenvwrapper

----

**Sun Apr 26 15:31:46 PDT 2015**

From the python 3.4 [venv standard library page](https://docs.python.org/3/library/venv.html),
here is an idiom for an extension
class to handle pulling its specific keyword args off its invocation before
calling its superclass

    def __init__(self, *args, **kwargs):
        self.nodist = kwargs.pop('nodist', False)
        self.nopip = kwargs.pop('nopip', False)
        self.progress = kwargs.pop('progress', None)
        self.verbose = kwargs.pop('verbose', False)
        super().__init__(*args, **kwargs)

## pyenv

For now, install pyenv and try it out.

Ok, pyenv can't see any of my homebrew pythons:

        vega-> pyenv versions --list
        * system (set by /Users/jeff/.pyenv/version)

brew has installed many python 2 and python 3 instances:

        vega-> brew info python3
        python3: stable 3.4.3 (bottled), devel 3.5.0a3, HEAD
        https://www.python.org/
        /usr/local/Cellar/python3/3.4.0 (3903 files, 68M)
          Poured from bottle
        /usr/local/Cellar/python3/3.4.1 (3845 files, 66M)
          Poured from bottle
        /usr/local/Cellar/python3/3.4.1_1 (3845 files, 66M)
          Poured from bottle
        /usr/local/Cellar/python3/3.4.2_1 (5120 files, 86M)
          Built from source
        /usr/local/Cellar/python3/3.4.3 (4727 files, 83M) *
          Poured from bottle

python2s

        vega-> brew info python
        python: stable 2.7.9 (bottled), HEAD
        https://www.python.org
        /usr/local/Cellar/python/2.7.6_1 (5021 files, 83M)
          Poured from bottle
        /usr/local/Cellar/python/2.7.8 (4716 files, 75M)
          Poured from bottle
        /usr/local/Cellar/python/2.7.8_1 (4782 files, 76M)
          Poured from bottle
        /usr/local/Cellar/python/2.7.8_2 (6087 files, 96M)
          Built from source
        /usr/local/Cellar/python/2.7.9 (6137 files, 98M) *
          Built from source


### Questions

- q: how does pyenv discover if there is venv support available when it runs?
- a: you [tell it via an environment variable](https://github.com/yyuu/pyenv-virtualenvwrapper#using-pyvenv-instead-of-virtualenv)

        export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="true"

- q: how does pyenv know to use the homebrew installed pythons?
- a: homebrew tells us

    - To use Homebrew's directories rather than ~/.pyenv add to your profile:

            export PYENV_ROOT=/usr/local/opt/pyenv

    - but that doesn't seem to help:

            vega-> PYENV_ROOT=/usr/local/opt/pyenv pyenv versions
            * system (set by /usr/local/opt/pyenv/version)

- next q: does pyenv install download and install a completely new python?  Or re-use what brew has installed?
- a: well, since pyenv finds 169 different python variants to manage, I guess pyenv downloads
  its own versions.

### try installing 3.4.3

    vega-> pyenv install 3.4.3
    Downloading Python-3.4.3.tgz...
    -> https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz
    Installing Python-3.4.3...
    Installed Python-3.4.3 to /Users/jeff/.pyenv/versions/3.4.3

and now as expected:

        vega-> pyenv versions
        * system (set by /Users/jeff/.pyenv/version)
          3.4.3

### install pyenv-virtualenv

### set up pldev3

    vega-> pyenv virtualenv 3.4.3 pldev3
    Ignoring indexes: https://pypi.python.org/simple
    Requirement already satisfied (use --upgrade to upgrade): setuptools in /Users/jeff/.pyenv/versions/pldev3/lib/python3.4/site-packages
    Requirement already satisfied (use --upgrade to upgrade): pip in /Users/jeff/.pyenv/versions/pldev3/lib/python3.4/site-packages

Ok, that worked.  Now I see

        vega-> pyenv versions
        * system (set by /Users/jeff/.pyenv/version)
          3.4.3
          pldev3

use pldev3

        vega-> pyenv shell pldev3
        pyenv-virtualenv: activate pldev3
        (pldev3) vega-> pyenv versions
          system
          3.4.3
        * pldev3 (set by PYENV_VERSION environment variable)

Now install all the dependent packages:

        (pldev3) vega-> pip3 install -r backend-python3-pkgs.txt
          ...
        Successfully installed django-1.8 django-cors-headers-1.0.0 django-lockdown-1.1 django-rest-0.0.1 djangorestframework-3.1.1 elasticsearch-1.4.0 httplib2-0.9.1 ijson-2.2 lxml-3.4.4 mysqlclient-1.3.6 oauthlib-0.7.2 pycurl-7.19.5.1 pymysql-0.6.6 python-instagram-1.3.1 simplejson-3.6.5 six-1.9.0 urllib3-1.10.3

And run some unit tests:

But I get failures because I don't have a project home, and I don't install the modules
under development in my virtualenv.

If I try from teh root of the tree (/c/witlee/src), I get:

        (pldev3) vega-> python3 -m unittest witlee/data/product_loader/tests/test_product_loader.py
          ...
          File "/Users/jeff/.pyenv/versions/3.4.3/lib/python3.4/unittest/loader.py", line 114, in loadTestsFromName
            parent, obj = obj, getattr(obj, part)
        AttributeError: 'module' object has no attribute 'product_loader'

If I try from down in the test directory, it is worse:

        (pldev3) vega-> pushd witlee/data/product_loader/tests/
        /c/witlee/src/witlee/data/product_loader/tests /c/witlee/src
        (pldev3) vega-> python3 -m unittest test_product_loader.py
          ...
        Traceback (most recent call last):
          File "/Users/jeff/.pyenv/versions/3.4.3/lib/python3.4/unittest/loader.py", line 105, in loadTestsFromName
            module = __import__('.'.join(parts_copy))
          File "/c/witlee/src/witlee/data/product_loader/tests/test_product_loader.py", line 16, in <module>
            from witlee.settings import BASE_DIR
        ImportError: No module named 'witlee'

So I think the first error is telling me that data has no __init__.py?

but this test worked before on the virtualenvwrapper side when I had a .project:

        vega-> cat ~/.virtualenvs/pldev2/.project
        /c/witlee/src

So associate the project directory with the virtualenv with `setvirtualproject`, which is
[defined by virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#project-directory-management), and I suppose, re-implemented by pyenv-virtualenvwrapper.

        (pldev3) vega-> cd /c/witlee/src/
        (pldev3) vega-> setvirtualenvproject
        Setting project for pldev3 to /c/witlee/src

Now the unit test should run:

No, same error.

Ok, I want [path management](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#path-management), not rpoject management.

        (pldev3) vega-> add2virtualenv /c/witlee/src
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
        AttributeError: 'module' object has no attribute 'sysconfig'
        ERROR: currently-active virtualenv does not appear to have a site-packages directory

Wow.

Ok, am I cross-using virtualenvwrapper and pyenv-virtualenvwrapper?

Probably yes.

So comment-out classic virtualenvwrapper from my bash init, and try again. with pldev4.

Still get the same error.

If I switch back to pldev2, the unittests run.

How about if I remove data/__init__.py?

Yes, they continue to run validating my earlier assumption.

This fact, and the fact that add2virtualenv throws an error says I have something
more systemic wrong with my setup.

So go back to square one tomorrow and try to build again.

----

## python style

- a great python style guide was written by the google guys: [Google Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
