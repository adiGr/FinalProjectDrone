import time

__author__ = 'ReemAdi'

from dronekit import *
from Location import Location

DELAY = 0.5

class Drone:

    def __init__(self,connect_string = '/dev/ttyAMA0'):
        print 'Connecting to vehicle on: '+connect_string
        self.vehicle = connect(connect_string,  wait_ready=True,baud=57600)


    def take_off(self,init_alt_in_meter):
        while not self.vehicle.is_armable:
            time.sleep(DELAY)
            print "Waiting for arming"

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
        loc.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc.set_altitude(loc.get_altitude()+init_alt_in_meter)
        location_global = LocationGlobal(loc.latitude,loc.longitude,loc.altitude)
        self.vehicle.simple_goto(location_global)
        while not loc1.is_right_alt(loc.altitude):
            loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        if init_alt_in_meter > 0:
            print "complete function up"
        else:
            print "complete function down"

    def down(self,init_alt_in_meter):
        self.up(-init_alt_in_meter)


    def forward(self,move_forward_in_meter):
        dest_location = Location()
        loc1 = Location()
        loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        dest_location.setFromVehicleLocation(self.vehicle.location.global_frame)
        add_lat = math.sin(self.vehicle.heading)*move_forward_in_meter
        add_lon = math.cos(self.vehicle.heading)*move_forward_in_meter
        dest_location.set_latitude(dest_location.get_latitude()+ add_lat)
        dest_location.set_longitude(dest_location.get_longitude()+add_lon)
        location_global = LocationGlobal(dest_location.get_latitude(),dest_location.get_longitude(),dest_location.get_altitude())
        print "dest: lat: %s  lon: %s alt: %s" % (location_global.lat,location_global.lon,location_global.alt)
        print "now:lat:%f\tlong:%f" % (loc1.get_latitude(),loc1.get_longitude())
        self.vehicle.simple_goto(location_global,groundspeed=100)
        while loc1.is_equals_lat(dest_location.latitude) is False or loc1.is_equals_lon(dest_location.longitude) is False:
            loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
            #print "dest:lat:%f\tlong:%f" % (dest_location.get_latitude(),dest_location.get_longitude())
            print "now: %s" % (self.vehicle.location.global_frame)
            time.sleep(10**DELAY)


        if move_forward_in_meter > 0:
            print "complete function forward"
        else :
            print "complete function backwards"

    def forward_relative(self,move_forward_in_meter):
        dest_location = Location()
        loc1 = Location()
        loc1.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        dest_location.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        add_lat = math.sin(self.vehicle.heading)*move_forward_in_meter
        add_lon = math.cos(self.vehicle.heading)*move_forward_in_meter
        dest_location.set_latitude(dest_location.get_latitude()+ add_lat)
        dest_location.set_longitude(dest_location.get_longitude()+add_lon)
        location_global = LocationGlobal(dest_location.get_latitude(),dest_location.get_longitude(),dest_location.get_altitude())
        print "dest: lat: %s  lon: %s alt: %s" % (location_global.lat,location_global.lon,location_global.alt)
        print "now:lat:%f\tlong:%f" % (loc1.get_latitude(),loc1.get_longitude())
        self.vehicle.simple_goto(location_global)
        while loc1.is_equals_lat(dest_location.latitude) is False or loc1.is_equals_lon(dest_location.longitude) is False:
            loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
            #print "dest:lat:%f\tlong:%f" % (dest_location.get_latitude(),dest_location.get_longitude())
            print "now: %s" % (self.vehicle.location.global_relative_frame)
            time.sleep(10**DELAY)


        if move_forward_in_meter > 0:
            print "complete function forward"
        else :
            print "complete function backwards"

    def backwards(self,move_forward_in_meter):
        self.forward(-move_forward_in_meter)


    def turn_right(self,turn_right_in_degree):
        self.vehicle.gimbal.rotate(0, 0, 90)
        time.sleep(10)


    def turn_left(self,turn_left_in_degree):
        self.turn_right(-turn_left_in_degree)


    def move_right(self,move_in_meter):
        loc = Location()
        loc1 = Location()
        loc.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc.set_longitude(loc.get_longitude()+move_in_meter*math.cos(self.vehicle.heading+90))
        loc.set_latitude(loc.get_latitude()+move_in_meter*math.sin(self.vehicle.heading+90))
        location_global = LocationGlobal(loc.latitude,loc.longitude,loc.altitude)
        self.vehicle.simple_goto(location_global)
        while not loc1.is_equals_lat(loc.latitude):
            loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        if move_in_meter > 0:
            print "complete function right"
        else:
            print "complete function left"


    def move_left(self,move_in_meter):
        self.move_right(-move_in_meter)



