#!/usr/bin/python3


"""a function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
  """Function returns a UTF* text file
    Args:
        filename: placeholder of file to read
    Return:
        UTF8 text file
    """
    with open(filename,'r',encoding="utf-8") as f:
         textfile = f.read()
    print(textfile)
