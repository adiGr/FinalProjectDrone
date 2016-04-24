from unittest import TestCase
from dronekit import *
from dronekit_sitl import SITL
from Drone import Drone

__author__ = 'ReemAdi'


class TestBattery(TestCase):
    def test_set_volt(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        print "Connecting to vehicle on: 'tcp:127.0.0.1:5760'"
        vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
        print " Battery: %s" % vehicle.battery
        battery = Battery( vehicle.battery.voltage)
########fail the test
