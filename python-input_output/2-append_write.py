#!/usr/bin/python

"""appends a string at the end of a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):

    
    """function writes text to file
    Args:
        filename: name of file to write to
        text: text to write
    Return:
        returns number of text characters
    """

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    alen = len(text)
    return alen
