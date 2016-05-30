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
        sitl.stop()


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
        sitl.stop()


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
        sitl.stop()



    def test_set_battery_from_vehicle(self):
        # check number zero the limit
        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,0,0)
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(NEGATIVE_NUMBER,0,0)
        # check number NEGATIVE number one the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,NEGATIVE_NUMBER,0)
        # check number NEGATIVE number two the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,0,NEGATIVE_NUMBER)
        # check number NEGATIVE number three the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(POSITIVE_NUMBER,0,0)
        # check number POSITIVE number one the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, POSITIVE_NUMBER)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,0,POSITIVE_NUMBER)
        # check number POSITIVE number two the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, POSITIVE_NUMBER)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,POSITIVE_NUMBER,0)
        # check number POSITIVE number three the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, POSITIVE_NUMBER)


        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(CHAR_NUMBER,0,0)
        # check number char number number one the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, int(CHAR_NUMBER))
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)
        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,0,CHAR_NUMBER)
        # check number char number number two the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, int(CHAR_NUMBER))
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,CHAR_NUMBER,0)
        # check number char number number three the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, int(CHAR_NUMBER))

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(CHARACTER,0,0)
        # check number char number one the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,CHARACTER,0)
        # check number char number two the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

        battery_test = Battery(bet(0,0,0))
        battery_test_copy = bet(0,0,CHARACTER)
        # check number char number three the limit
        battery_test.set_battery_from_vehicle(battery_test_copy)
        self.assertEqual(battery_test.volt, 0)
        self.assertEqual(battery_test.level, 0)
        self.assertEqual(battery_test.current, 0)

    def test_if_low_battery_level(self):
        # check number zero the limit
        battery_test = Battery(bet(0,0,0))
        self.assertTrue(battery_test.if_low_battery_level(),"battey low")

        battery_test = Battery(bet(0,0,4))
        self.assertTrue(battery_test.if_low_battery_level(),"battey low")

        battery_test = Battery(bet(0,0,5))
        self.assertTrue(battery_test.if_low_battery_level(),"battey low")

        battery_test = Battery(bet(0,0,6))
        self.assertFalse(battery_test.if_low_battery_level(),"battey low")

    def test_if_full_battery_level(self):
        # check number high limit
        battery_test = Battery(bet(0,0,100))
        self.assertTrue(battery_test.if_full_battery_level(),"full battey")
        # check number up the limit
        battery_test = Battery(bet(0,0,101))
        self.assertTrue(battery_test.if_full_battery_level(),"full battey")
      # check number low the limit
        battery_test = Battery(bet(0,0,50))
        self.assertFalse(battery_test.if_full_battery_level(),"full battey")
      # check number low the limit (99)
        battery_test = Battery(bet(0,0,99))
        self.assertFalse(battery_test.if_full_battery_level(),"full battey")