"""
    Copyright (c) 2021 Fedora Websites and Apps

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

from click import style, echo


class StatusDecorator(object):
    def __init__(self):
        self.PASS = style("[ \u2713 ]", fg="green", bold=True)
        self.FAIL = style("[ \u2717 ]", fg="red", bold=True)
        self.WARN = style("[ ! ]", fg="yellow", bold=True)
        self.HEAD = style("[ \u2605 ]", fg="magenta", bold=True)
        self.STDS = "     "

    def success(self, request_message):
        echo(self.PASS + " " + request_message)

    def failure(self, request_message):
        echo(self.FAIL + " " + request_message)

    def warning(self, request_message):
        echo(self.WARN + " " + request_message)

    def section(self, request_message):
        echo(self.HEAD + " " + style(request_message, fg="magenta", bold=True))

    def general(self, request_message):
        echo(self.STDS + " " + request_message)
