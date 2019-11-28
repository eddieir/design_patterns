"""
The Command Pattern encapsulates a request as an
object, thereby letting you parameterized other objects
with different requests, queue or log requests, and support
undoable operations.
"""

from command import RemoteController, Light, LightOnCommand, LightOffCommand
from command2 import Wizard, Goblin, ShrinkSpell, InvisibilitySpell


def test_remote_controller():
    light = Light()
    assert light.status == 'off'

    controller = RemoteController()

    # Encapsulate light "on" request as a LightCommand object
    light_on_command = LightOnCommand(light)
    # pass command object to remote controller
    controller.set_command(light_on_command)
    # do an action to change to object state
    controller.push_button()
    assert light.status == 'on'

    light_off_command = LightOffCommand(light)
    controller.set_command(light_off_command)
    controller.push_button()
    # Execute request object
    assert light.status == 'off'


def test_wizard_and_goblin():
    wizard = Wizard()
    goblin = Goblin()

    assert goblin.hp == 100

    # undo at first time
    wizard.undo_last_spell()
    wizard.redo_last_spell()
    assert goblin.hp == 100

    wizard.cast_spell(ShrinkSpell(), goblin)
    assert goblin.hp == 90

    wizard.undo_last_spell()
    assert goblin.hp == 100

    wizard.redo_last_spell()
    assert goblin.hp == 90

    wizard.cast_spell(InvisibilitySpell(), goblin)
    assert goblin.visibility is True

    wizard.undo_last_spell()
    assert goblin.visibility is False

    wizard.redo_last_spell()
    assert goblin.visibility is True
