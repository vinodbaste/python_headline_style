headline_style
=========

This filter changes a given text to Title Caps, and attempts to be clever
about SMALL words like a/an/the in the input.
The list of "SMALL words" which are not capped comes from the New York
Times Manual of Style, plus some others like 'vs' and 'v'.

The filter employs some heuristics to guess abbreviations that don't need conversion.

+------------------+----------------+
| Original         | Conversion     |
+==================+================+
| this is a test   | This Is a Test |
+------------------+----------------+
| THIS IS A TEST   | This Is a Test |
+------------------+----------------+
| this is a TEST   | This Is a TEST |
+------------------+----------------+

More examples and expected behavior for corner cases are available in the
`package test suite <https://github.com/ppannuto/python-headLineStyle/blob/main/headLineStyle/tests.py>`__.

Issues, updates, pull requests, etc should be directed
`to github <https://github.com/ppannuto/python-headLineStyle>`__.


Installation
------------

The easiest method is to simply use pip:

::

    (sudo) pip install headline_style


Usage
-----

headline_style provides only one function, simply:

.. code-block:: python

    >>> from headLineStyle import headLineStyle
    >>> headLineStyle('a thing')
    'A Thing'

A callback function may also be supplied, which will be called for every word:

.. code-block:: python

    >>> def abbreviations(word, **kwargs):
    ...   if word.upper() in ('TCP', 'UDP'):
    ...     return word.upper()
    ...
    >>> headLineStyle.headLineStyle('a simple tcp and udp wrapper', callback=abbreviations)
    'A Simple TCP and UDP Wrapper'

The callback function is supplied with an ``all_caps`` keyword argument, indicating
whether the entire line of text was entirely capitalized. Returning ``None`` from
the callback function will allow headLineStyle to process the word as normal.


Command Line Usage
------------------

headLineStyle also provides a command line utility ``headLineStyle``:

::

    $ headLineStyle make me a title
    Make Me a Title
    $ echo "Can pipe and/or whatever else" | headLineStyle
    Can Pipe and/or Whatever Else
    # Or read/write files:
    $ headLineStyle -f infile -o outfile

In addition, commonly used acronyms can be kept in a local file
at `~/.headLineStyle.txt`. This file contains one acronym per line.
The acronym will be maintained in the title as it is provided.
Once there is e.g. one line saying `TCP`, then it will be automatically
used when used from the command line.

::

    $ headLineStyle I LOVE TCP
    I Love TCP


Limitations
-----------

This is a best-effort library that uses regexes to try to do intelligent
things, but will have limitations. For example, it does not have the contextual
awareness to distinguish acronyms from words: us (we) versus US (United States).

The regexes and titlecasing rules were written for American English. While
there is basic support for Unicode characters, such that something like
"El Niño" will work, it is likely that accents or non-English phrases will
not be handled correctly.

If anyone has concrete solutions to improve these or other shortcomings of the
library, pull requests are very welcome!
