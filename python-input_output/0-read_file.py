#!/usr/bin/python3

"""function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """Function returns a UTF* text file
    Args:
        filename: name of file to read
    Return:
        UTF8 text file
    """
    with open(filename,'r',encoding="utf-8") as f:
       text = f.read()
       print(text)
    return text
