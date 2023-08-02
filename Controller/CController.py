from abc import ABC

from Interfaces.IController import IController


class CController(IController):
    # @override
    def do_something(self):
        print("do_something")


class CDummyController(IController):
    def do_something(self):
        print("dummy")