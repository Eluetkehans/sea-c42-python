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

    def __str__(self):
        indented = add_indent(self.content)
        return "<{}>\n{}\n<\{}>\n".format(self.name, indented, self.name)

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

    def __str__(self):
        indented = add_indent(self.content)
        return "<!DOCTYPE html>\n<{}>\n{}\n<\{}>\n".format(self.name, indented, self.name)

    def render(self, file_out, indent=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, "")


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="body", content=content)


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="p", content=content)


def add_indent(content):
    """Adds four blank spaces infront of every line of a given string."""
    lines = content.split("\n")
    ind_lines = []
    for line in lines:
        ind_lines.append("    " + line)
    return "\n".join(ind_lines)
