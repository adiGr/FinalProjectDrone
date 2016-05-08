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
    def __init__(self, voltage, current, level):
        self.voltage = voltage
        self.current = current
        self.level = level


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
        # check char that non number
        battery_test.set_volt(CHARACTER)
        self.assertEqual(battery_test.get_volt(), 0)
        #check char that  number
        battery_test.set_volt(CHAR_NUMBER)
        self.assertEqual(battery_test.get_volt(), int(CHAR_NUMBER))


    def test_set_level(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        print "Connecting to vehicle on: 'tcp:127.0.0.1:5760'"
        vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
        print " Battery: %s" % vehicle.battery
        battery_test = Battery(vehicle.battery)
        # check number negative the limit
        battery_test.set_level(NEGATIVE_NUMBER)
        self.assertEqual(battery_test.level, 0)
        # check number positive the limit
        battery_test.set_level(POSITIVE_NUMBER)
        self.assertEqual(battery_test.get_level(), POSITIVE_NUMBER)
        # check ZERO
        battery_test.set_level(0)
        self.assertEqual(battery_test.get_level(), 0)
        #check char that non number
        battery_test.set_level(CHARACTER)
        self.assertEqual(battery_test.get_level(), 0)
        #check char that  number
        battery_test.set_level(CHAR_NUMBER)
        self.assertEqual(battery_test.get_level(), int(CHAR_NUMBER))


    def test_set_current(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        print "Connecting to vehicle on: 'tcp:127.0.0.1:5760'"
        vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
        print " Battery: %s" % vehicle.battery
        battery_test = Battery(vehicle.battery)
        # check number negative the limit
        battery_test.set_current(NEGATIVE_NUMBER)
        self.assertEqual(battery_test.current, 0)
        # check number positive the limit
        battery_test.set_current(POSITIVE_NUMBER)
        self.assertEqual(battery_test.get_current(), POSITIVE_NUMBER)
        # check ZERO
        battery_test.set_current(0)
        self.assertEqual(battery_test.get_current(), 0)
        #check char that non number
        battery_test.set_current(CHARACTER)
        self.assertEqual(battery_test.get_current(), 0)
        #check char that  number
        battery_test.set_current(CHAR_NUMBER)
        self.assertEqual(battery_test.get_current(), int(CHAR_NUMBER))

  

