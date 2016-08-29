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
