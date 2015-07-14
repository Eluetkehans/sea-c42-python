#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):

    def __init__(self, content="", name="", style=""):
        self.style = style
        self.content = content
        self.name = name
        self.children = [content] if content else []

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent="    "):
        if len(self.style) >= 1:
            file_out.write("{}<{}{}>\n".format(indent, self.name, ' style="' +
                                               self.style + '"'))
        else:
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

    def __init__(self, name="", content="", style=""):
        Element.__init__(self, name="html", content="", style="")

    def render(self, file_out, indent=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, "")


class Body(Element):

    def __init__(self, content="", style=""):
        Element.__init__(self, name="body", content=content, style=style)


class P(Element):

    def __init__(self, content="", style=""):
        Element.__init__(self, name="p", content=content, style=style)


class Head(Element):

    def __init__(self, content="", style=""):
        Element.__init__(self, name="head", content=content, style=style)


class OneLineTag(Element):

    def __init__(self, content="", style="", name=""):
        Element.__init__(self, name=name, content=content, style=style)

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


class Title(OneLineTag):

    def __init__(self, content="", style=""):
        OneLineTag.__init__(self, name="title", content=content, style=style)


class SelfClosingTag(Element):

    def __init__(self, content="", style="", name=""):
        Element.__init__(self, name=name, content=content, style=style)

    def render(self, file_out, indent="    "):
        file_out.write("{}<{} />\n".format(indent, self.name))


class Hr(SelfClosingTag):

    def __init__(self, content="", style=""):
        SelfClosingTag.__init__(self, name="hr", content=content, style=style)


class Br(SelfClosingTag):

    def __init__(self, content="", style=""):
        SelfClosingTag.__init__(self, name="br", content=content, style=style)
