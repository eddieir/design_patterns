"""
Implement duck system in Head First Design Pattern books
with multiple inheritance styles
"""

import abc


## Fly and concrete classes
class FlyBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        return "fly with wings"


class FlyNoWay(FlyBehavior):
    def fly(self):
        return "fly no way"


## Quack and concrete classes
class QuackBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self):
        return "quack"


class Speak(QuackBehavior):
    def quack(self):
        return "speak"


class MuteQuack(QuackBehavior):
    def quack(self):
        return "mute"


# Construct various type of duck
class RubberDuck(MuteQuack, FlyNoWay):
    pass


class DecoyDuck(Quack, FlyWithWings):
    pass


class DonaldDuck(Speak, FlyNoWay):
    pass

