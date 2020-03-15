#!/usr/bin/env python2
# -*- coding: utf-8 -*-


# these 2 methods to_unicode and to_str are from
#  Item 3: Know the difference between bytes, str and unicode
#  _Effective Python_, by Brett Slatkin
def to_str(unicode_or_str):
    """convert arg to string, encoding bytes as utf-8 if needed.

    >>> u = u'4 arrows: \u2190 \u2191 \u2192 \u2193'
    >>> type(u)
    <type 'unicode'>
    >>> s = to_str(u)
    >>> type(s)
    <type 'str'>
    >>> back_to_u = to_unicode(s)
    >>> u == back_to_u
    True
    """

    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value


def to_unicode(unicode_or_str):
    """convert arg to unicode, decoding from the assumed encoding of utf-8

    >>> s = b'4 arrows: ← ↑ → ↓'
    >>> type(s)
    <type 'str'>
    >>> u = to_unicode(s)
    >>> type(u)
    <type 'unicode'>
    >>> u
    u'4 arrows: \u2190 \u2191 \u2192 \u2193'
    """
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value
