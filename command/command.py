"""
A remote controller has 2 button: turn light on and turn light off
It does a action to a Light object.
"""
import abc


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError


class NoCommand(Command):
    """
    Null object pattern for initialize
    """

    def execute(self):
        pass


class BaseLightCommand(Command):
    def __init__(self, light):
        self.light = light

class LightOnCommand(BaseLightCommand):
    def execute(self):
        self.light.on()

class LightOffCommand(BaseLightCommand):
    def execute(self):
        self.light.off()


class RemoteController(object):
    """
    Remote controller has 2 buttons: light on and light off
    """

    def __init__(self):
        # init with NoCommand
        self.target = NoCommand()

    def set_command(self, command):
        self.target = command

    def push_button(self):
        self.target.execute()


# Vendor classes
class Light(object):
    def __init__(self):
        self._status = 'off'

    def on(self):
        self._status = 'on'

    def off(self):
        self._status = 'off'

    @property
    def status(self):
        return self._status

