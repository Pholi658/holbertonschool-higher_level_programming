#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and returns the number of characters written"""

def write_file(filename="", text=""):
    """function writes text to file
    Args:
        filename: name of file to write to
        text: text to write
    Return:
        returns number of characters
    """
    with open(filename,'w', encoding ="utf-8") as f:
        f.write(text)
        wordlen = len(text)
        return wordlen
