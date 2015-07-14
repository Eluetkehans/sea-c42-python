#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):

    def __init__(self, content="", name=""):
        self.name = name
        self.children = [content] if content else []
        self.content = content

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent="    "):
        file_out.write("{}<{}>\n".format(indent, self.name))
        for child in self.children:
            if(type(child) == str):
                # Add new content string without rendering
                file_out.write(indent + "    " + child + "\n")
            else:
                # Add new child node, by recursively rendering
                child.render(file_out, indent + "    ")
        file_out.write("%s</%s>\n" % (indent, self.name))



class Html(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name="html", content="")

    def render(self, file_out, indent=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, "")


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="body", content=content)


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="p", content=content)


class Head(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="head", content=content)


class Title(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="title", content=content)

    # This is exactly the same as Element.render, except some line breaks
    # Had to be taken out.
    def render(self, file_out, indent="    "):
        file_out.write("{}<{}>".format(indent, self.name))
        for child in self.children:
            if(type(child) == str):
                # Add new content string without rendering
                file_out.write(child)
            else:
                # Add new child node, by recursively rendering
                child.render(file_out, indent)
        file_out.write("</%s>\n" % (self.name))
