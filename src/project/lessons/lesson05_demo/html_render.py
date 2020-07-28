#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = 'html'
    indent = "    "  # 4 spaces

    def __init__(self, content=None, ind="", **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attribute = kwargs
        self.cur_ind = ind

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        if self.attribute:
            open_tag = ["<{} ".format(self.tag)]
            for key, value in self.attribute.items():
                open_tag.append(f'{key}="{value}" ')
            open_tag[-1] = open_tag[-1][:-1]
            open_tag.append(">")
            return "".join(open_tag)
        else:
            return "<{}>".format(self.tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file, cur_ind=""):  # Question? How to pass cur_ind value from
        # other class or how to change it if the default is defined. I thought it would
        # work if it increase every time when the function is called, but not sure how
        # to do it.
        out_file.write(self.cur_ind + self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(self.cur_ind + self.indent + content)
                out_file.write('\n')
        out_file.write(self.cur_ind + self._close_tag())
        out_file.write("\n")


class Html(Element):

    tag = 'html'
    doc = '<!DOCTYPE html>'

    def __init__(self, content=None, **kwargs):
        super().__init__(content, **kwargs)

    def render(self, out_file, cur_ind=""):
        out_file.write(self.doc)
        out_file.write("\n")
        Element.render(self, out_file, cur_ind)


class Body(Element):

    tag = 'body'


class P(Element):

    tag = 'p'


class Head(Element):

    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):
        out_file.write(self.cur_ind + self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
        out_file.write('\n')

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):

    tag = 'title'


class SelfClosingTag(Element):

    def render(self, out_file, cur_ind=""):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(self.cur_ind + tag)


class Hr(SelfClosingTag):

    tag = 'hr'


class Br(SelfClosingTag):

    tag = 'br'

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['herf'] = link
        super().__init__(content, **kwargs)


class Ul(Element):

    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.level = level
        self.tag = 'h' + str(self.level)


class Meta(SelfClosingTag):

    tag = 'meta'



