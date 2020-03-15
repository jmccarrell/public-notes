#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for python 3; will not work for python 2:
#    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 10: ordinal not in range(128)


# these 2 methods to_str and to_bytes are from _Effective Python_, by Brett Slatkin
def to_str(bytes_or_str):
    """convert arg to string, decoding bytes via utf-8 if needed.

    >>> s = '4 arrows: ← ↑ → ↓'
    >>> t = to_str(s)
    >>> t
    '4 arrows: ← ↑ → ↓'
    >>> type(t)
    <class 'str'>
    >>> b = s.encode('utf-8')
    >>> type(b)
    <class 'bytes'>
    >>> bt = to_str(b)
    >>> bt
    '4 arrows: ← ↑ → ↓'
    >>> type(bt)
    <class 'str'>
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    """convert arg to bytes, encoding strings in utf-8, if needed.

    >>> s = '4 arrows: ← ↑ → ↓'
    >>> bs = to_bytes(s)
    >>> bs
    b'4 arrows: \xe2\x86\x90 \xe2\x86\x91 \xe2\x86\x92 \xe2\x86\x93'
    >>> type(bs)
    <class 'bytes'>
    >>> b = b'foobar'
    >>> type(b)
    <class 'bytes'>
    >>> bb = to_bytes(b)
    >>> bb
    b'foobar'
    >>> type(bb)
    <class 'bytes'>
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
