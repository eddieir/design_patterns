from mixin import DonaldDuck, RubberDuck, DecoyDuck
import pytest


@pytest.mark.parametrize("duck, behavior", [
    (DecoyDuck(), ["quack", "fly with wings"]),
    (DonaldDuck(), ["speak", "fly no way"]),
    (RubberDuck(), ["mute", "fly no way"]),
])
def test_duck(duck, behavior):
    assert [duck.quack(), duck.fly()] == behavior