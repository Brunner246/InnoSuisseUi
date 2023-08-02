import abc


class IController(abc.ABC):
    @abc.abstractmethod
    def do_something(self):
        pass
