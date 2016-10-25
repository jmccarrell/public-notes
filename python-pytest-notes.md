## py.test

### presentations:

- Holger Krekel: Improving automated testing with py.test - PyCon 2014
    - [Youtube](https://www.youtube.com/watch?v=AiThU6JQbE8)
    - tutorial code: (the link in the video is wrong at the beginning of the video)

        $ wget http://merlinux.eu/~hpk/course/pycon-2014-code.zip

    - I never found the slides, but that didn't really matter too much to me.

#### pytest-django

- Andreas Pelme: pytest: helps you write better Django apps
    - from djangocon europe 2014
    - [slides](https://speakerdeck.com/pelme/pytest-helps-you-write-better-django-apps)
    - [youtube](https://www.youtube.com/watch?v=aaArYVh6XSM)

## notes

- tip: use `-rf` to report a bit more info about failed tests, including the full test name.
    - then you can run just that failed test by name
    - you can add this to the permanent command line options in the .ini file: addoption or something like that.

----

**Tue Oct 25 09:45:53 PDT 2016**

## py.test mock investigation

## [Improve your testing with Pytest and Mock](https://www.youtube.com/watch?v=RcN26hznmk4) - PyCon SG 2015

- linked off of py.test [talks and tutorials page](http://doc.pytest.org/en/latest/talks.html)
- 45 min preso
- no slides linked on the youtube page
- my code of his examples is in `/j/proj/pycon-2015-pytest-and-mock`

### Fixtures are awesome

- about 17:21 into the video

- can all other fixtures
- can be used to parameterize a test function against a collection of test values
- can be shared between files via `conftest.py`
- `@pytest.fixture(autouse=True)` acts as setup/teardown without explicit request by your test functions
- you can even test your fixtures (they are just functions)

- besides conftest.py, one can also put fixtures into a module, and then just manually import that module where it needs to be.

### verifying calls

- 19:36
- start of discussion of mocks
- when you want to test more than the result of just one function call
- when you need to test the interaction between several functions
- recommends mock, builtin to python 3
- recommends using spec= in calls to Mock() constructor, as it enforces greater interface compliance.

#### test doubles

- test double concept: construct parallel hierarchies of test objects that behave in similiar ways to the real objects.

- `assert_called_with` implements the semantic of asserting the most recent call value.
    - if there are multiple calls, `assert_called_with` matches against the most recent call

- mocks remember all of the calls
    - if you care about the order of the calls:
    - the `calls()` method returns all of the calls, in order with their args
    - so you can grab it, and assert whatever about its contents

### Tiny gotchas (read the docs)

- `assert_called` only tracks the most recent call
- if you call `mock('bar')`, then `mock.assert_any_call('foo')`, it will fail, but will not report the `bar` call.
- the docs are your friend

### stubbing return values

- replace the behavior
- a different kind of testing than testing the interaction between objects a la test doubles

### monkeypatching

- 32:53
- sounds like something you shouldn't do, but there are cases where it is needed.

- what if I can't pass in a mock?

```python
# from forecaster.py

from weather_service import WeatherService

class Forecaster:
    def __init__(self):
        self.weather_service = WeatherService()
        ...
```

- there is no opportunity to inject a mock here.  ie, no factory to override.

- the author prefers pytest monkeypatching *over* unittest.mock patch
    - because unittest.mock patch is implemented as a context manager, which means all of the test code gets indented.
    - which does not like
- he says the two are otherwise 'the same thing'

### monkeypatch to the rescue

- its a special predefined fixture
- use `monkeypatch.setattr()` to go into a module and set a value
- pytest removes the patch when the test function ends

- example
    - NB. the patching is done at the *module* level for the duration of the test

```python
def test_rain_when_barometer_rising(monkeypatch, mock_weather_service):
    WS = Mock(return_value=mock_weather_service)
    # write our mock into the module namespace
    monkeypatch.setattr('forecaster.WeatherService', WS)

    # now test
    forecaster = Forecaster()
    mock_ws.barometer.return_value = 'rising'
    assert forecaster.forecast == 'Going to rain'
```


- this works because python modules are singletons
- the module has already been loaded, so pytest can go in there and mutate the value for the duration of the test, then restore it.

### plugins

#### pytest idioms

- invoke the python debugger for each failure

`pytest <testfile> --pdb`

- debug the first failure, then stop running tests

`pytest <testfile> -x --pdb`

    -x, --exitfirst       exit instantly on first error or failed test.

- prefer ipdb?  use mverteuil/pytest-ipdb

```
pip install ... pytest-ipdb.git
pytest <testfile> --ipdb
```

### parameterize values of fixtures

- a powerful but somewhat hidden feature is the ability to parameterize *dependent* values of fixtures at test run time.
- ie, to change the value of a fixture that is dependent on another fixture.
- at runtime, pytest will walk the fixture dependency tree and override a value anywhere in the tree.
- an example:

----

- now back to the py.test fixtures page, specifically about crossing scope boundaries
    - session
    - module
    - class
    - function (default)

- the [docs](http://doc.pytest.org/en/latest/fixture.html#modularity-using-fixtures-from-a-fixture-function) say:

> Note, that the app fixture has a scope of module and uses a module-scoped smtp fixture. The example would still work if smtp was cached on a session scope: it is fine for fixtures to use “broader” scoped fixtures but not the other way round: A session-scoped fixture could not use a module-scoped one in a meaningful way.

- so fixtures can refer to a more global scope, but cannot refer to a more narrowly defined scope.

## [Auto grouping of test fixture instances](http://doc.pytest.org/en/latest/fixture.html#automatic-grouping-of-tests-by-fixture-instances)

- shows how the fixture tree is dynamically walked to minimize the number of active test fixture instances at any one time.

## [Using fixtures from classes, modules or projects](http://doc.pytest.org/en/latest/fixture.html#using-fixtures-from-classes-modules-or-projects)

- when you associate a test fixture with a class, pytest will create an instance of the fixture for *each test method*.
- you can declare multiple fixtures to operate on a class:

`@pytest.mark.usefixtures("cleandir", "anotherfixture")`

## [Shifting (visibility of) fixture functions](http://doc.pytest.org/en/latest/fixture.html#shifting-visibility-of-fixture-functions)

> If during implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file or even separately installable plugins without changing test code.

> The discovery of fixtures functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins.
