"""
A wizard can cast spell on goblin and reduce his hp (which has range(0, 100))
He can also make the goblin visible or invisible.
In addition to this,
the wizard can keep track of his spells and choose to undo or redo them.
Initially, the goblin has 100 hp and visible.
"""

import abc


class Command(metaclass=abc.ABCMeta):
    def __init__(self):
        self.target = None

    @abc.abstractmethod
    def execute(self, target):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self):
        raise NotImplementedError

    @abc.abstractmethod
    def redo(self):
        raise NotImplementedError


class ShrinkSpell(Command):
    def execute(self, target):
        self.target = target
        self.target.hp = target.hp - 10

    def undo(self):
        if self.target is not None:
            hp = self.target.hp + 10
            hp = 100 if hp > 100 else hp
            self.target.hp = hp

    def redo(self):
        if self.target is not None:
            hp = self.target.hp - 10
            hp = 0 if hp < 0 else hp
            self.target.hp = hp

    def __repr__(self):
        return "ShrinkSpell: {} - {}".format(self.target, self.target.hp)


class InvisibilitySpell(Command):
    def execute(self, target):
        self.target = target
        self.target.visibility = True

    def undo(self):
        if self.target is not None:
            self.target.visibility = not self.target.visibility

    def redo(self):
        self.undo()

    def __repr__(self):
        return "InvisibilitySpell: {} - {}".format(self.target,
                                                   self.target.visibility)


class Wizard(object):
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def cast_spell(self, command, target):
        command.execute(target)
        self.undo_stack.append(command)

    def undo_last_spell(self):
        """Undo last spell"""
        if self.undo_stack:
            spell = self.undo_stack.pop()
            self.redo_stack.append(spell)
            spell.undo()

    def redo_last_spell(self):
        """Redo last spell"""
        if self.redo_stack:
            spell = self.redo_stack.pop()
            self.undo_stack.append(spell)
            spell.redo()


class Goblin(object):
    def __init__(self):
        self.hp = 100
        self.visibility = False

    def print_status(self):
        return self.hp

    def __repr__(self):
        return "{} - {}".format(self.hp, self.visibility)
