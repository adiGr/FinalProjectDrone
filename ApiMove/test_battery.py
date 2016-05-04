from unittest import TestCase
from dronekit import *
from dronekit_sitl import SITL
from Battery import Battery

__author__ = 'ReemAdi'

POSITIVE_NUMBER = 10
NEGATIVE_NUMBER = -23
CHARACTER = 'C'
CHAR_NUMBER = '48'


class bet:
    def __init__(self, lat, lon, alt):
        self.lat = lat
        self.lon = lon
        self.alt = alt


class TestBattery(TestCase):
    def test_set_volt(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        print "Connecting to vehicle on: 'tcp:127.0.0.1:5760'"
        vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
        print " Battery: %s" % vehicle.battery
        battery_test = Battery(vehicle.battery)
        # check number negative the limit
        battery_test.set_volt(NEGATIVE_NUMBER)
        self.assertEqual(battery_test.volt, 0)
        # check number positive the limit
        battery_test.set_volt(POSITIVE_NUMBER)
        self.assertEqual(battery_test.get_volt(), POSITIVE_NUMBER)
        # check ZERO
        battery_test.set_volt(0)
        self.assertEqual(battery_test.get_volt(), 0)
        #check char that non number
        battery_test.set_volt(CHARACTER)
        self.assertEqual(battery_test.get_volt(), 0)
        #check char that  number
        battery_test.set_volt(CHAR_NUMBER)
        self.assertEqual(battery_test.get_volt(), int(CHAR_NUMBER))

