import time

__author__ = 'ReemAdi'

from dronekit import *
from Location import Location

DELAY = 0.5

class Drone:

    def __init__(self,connect_string = '/dev/ttyAMA0'):
        print 'Connecting to vehicle on: /dev/ttyAMA0'
        self.vehicle = connect(connect_string,  wait_ready=True,baud=57600)


    def take_off(self,init_alt_in_meter):
        while not self.vehicle.is_armable:
            time.sleep(DELAY)
            print "drone isn't arm-able"

        #here the drone is armable and move to the next step
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True
        while not self.vehicle.armed:
            time.sleep(DELAY)
        #after all the atriubute is set the simple take off can be done
        self.vehicle.simple_takeoff(init_alt_in_meter)
        loc = Location()
        loc.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        while not loc.is_right_alt(init_alt_in_meter):
            loc.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
            time.sleep(DELAY)


    def up(self,init_alt_in_meter):
        loc = Location()
        loc1 = Location()
        loc.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        loc1.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        loc.set_altitude(loc.get_altitude()+init_alt_in_meter)
        locationGlobal = LocationGlobal(loc.latitude,loc.longitude,loc.altitude)
        self.vehicle.simple_goto(locationGlobal)
        while not loc1.is_right_alt(loc.altitude):
            loc1.setFromVehicleLocation(self.vehicle.location.global_relative_frame)


    def down(self,init_alt_in_meter):
        self.up(-init_alt_in_meter)

    def send_ned_velocity(self,velocity_x, velocity_y, velocity_z, duration):
        pass 
        """


        # send command to vehicle on 1 Hz cycle
        for x in range(0,duration):
            self.vehicle.send_mavlink(msg)
            time.sleep(1)

    def forward(self,move_forward_in_meter):
        self.send_ned_velocity(-2,0,0,10)
        while True:
            print "global relative_frame: %s" % self.vehicle.location.global_relative_frame"""

