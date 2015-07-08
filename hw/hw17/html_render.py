#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):

    def __init__(self, name="", content=""):
        self.name = name
        self.content = content

    def append(self, new_text):
        self.content += new_text

    def render(self, file_name, ind=""):
        indent = ind
        indent += self.content
        write_out = open(file_name, "w")
        write_out.write(indent)
        write_out.close()
