import logging
import unittest

from observer import Hobbits, Orcs, Weather, WeatherType


class TestObserver(unittest.TestCase):
    def test_observable(self):
        weather = Weather()

        # register observable
        orcs, hobbits = Orcs(), Hobbits()
        weather.add_observer(orcs)
        weather.add_observer(hobbits)

        with self.assertLogs('behavioral.observer', level='INFO') as cm:
            # trigger event
            weather.time_pass()

        self.assertEqual(len(cm.output), 3)
        self.assertEqual(cm.output, [
            "INFO:behavioral.observer:Weather is changed to %s" % (weather.current_weather),
            "INFO:behavioral.observer:Orcs is %s" % (weather.current_weather),
            "INFO:behavioral.observer:Hobbits is %s" % (weather.current_weather),
        ])

        #
        weather.remove_observer(orcs)
        with self.assertLogs('behavioral.observer', level='INFO') as cm:
            # trigger event
            weather.time_pass()
        self.assertEqual(cm.output, [
            "INFO:behavioral.observer:Weather is changed to %s" % (weather.current_weather),
            "INFO:behavioral.observer:Hobbits is %s" % (weather.current_weather),
        ])
