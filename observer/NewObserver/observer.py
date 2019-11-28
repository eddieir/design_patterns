import abc
import logging 
import random 
from enum import IntEnum

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class WeatherType(IntEnum):
    SUNNY, RAINY, WINDY, COLD, = range(4)


class WeatherObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, current_weather: WeatherType):
        raise NotImplementedError


class Orcs(WeatherObserver):
    def update(self, current_weather: WeatherType):
        LOG.info("Orcs is %s", current_weather)


class Hobbits(WeatherObserver):
    def update(self, current_weather: WeatherType):
        LOG.info("Hobbits is %s", current_weather)


class Weather(object):
    def __init__(self):
        self.observers = []
        self.current_weather = None

    def add_observer(self, observer: WeatherObserver):
        if hasattr(observer, 'update'):
            self.observers.append(observer)

    def remove_observer(self, observer: WeatherObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update(self.current_weather)

    def time_pass(self):
        """
        A trigger to update to observers
        """
        self.current_weather = random.choice(list(WeatherType))
        LOG.info("Weather is changed to %s", self.current_weather)
        self.notify()


if __name__ == "__main__":
    weather = Weather()
    # add to observer list
    weather.add_observer(Orcs())
    weather.add_observer(Hobbits())

    # trigger event
    weather.time_pass()
