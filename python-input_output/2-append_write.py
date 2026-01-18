#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename,'a',encoding="utf-8") as f:
        """function appends text to file
        Args:
            filename: file to append to
            text: text to append
        Return:
            returns num of characters of text
        """
        f.write(text)
        wordlen = len(text)
        return wordlen
