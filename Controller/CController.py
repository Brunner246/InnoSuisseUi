from abc import ABC

from Interfaces.IController import IController


class CController(IController):
    # @override
    def do_something(self):
        print(__class__.__name__)


class CDummyController(IController):
    def do_something(self):
        print(__class__.__name__)

