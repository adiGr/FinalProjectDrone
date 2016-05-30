__author__ = 'ReemAdi'


from dronekit import *
from Location import Location

DELAY = 0.5

class Drone_global:

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


    def forward(self,move_forward_in_meter):
        dest_location = Location()
        loc1 = Location()
        head = self.vehicle.heading
        loc1.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        dest_location.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        add_lat = math.sin(self.vehicle.heading)*(move_forward_in_meter/100000.0)
        add_lon = math.cos(self.vehicle.heading)*(move_forward_in_meter/100000.0)
        dest_location.set_latitude(round(dest_location.get_latitude()+ add_lat,7))
        dest_location.set_longitude(round(dest_location.get_longitude()+add_lon,7))
        location_global = LocationGlobalRelative(dest_location.get_latitude(),dest_location.get_longitude(),dest_location.get_altitude())
        self.vehicle.simple_goto(location_global,groundspeed=100)
        while True:
            time.sleep(DELAY)
            if abs(self.vehicle.location.global_relative_frame.lat-location_global.lat) < 0.0000001 and abs(self.vehicle.location.global_relative_frame.lon-location_global.lon) < 0.000001  :
                break;
            self.condition_yaw(head)

        if move_forward_in_meter > 0:
            print "complete function forward\n"
        else :
            print "complete function backwards\n"


    def backwards(self,move_forward_in_meter):
        self.forward(-move_forward_in_meter)

    #only when is in the air
    def turn_right(self,turn_right_in_degree):
        self.vehicle.gimbal.rotate(0, 0, 90)
        time.sleep(1)

    #only when is in the air
    def turn_left(self,turn_left_in_degree):
        self.turn_right(-turn_left_in_degree)
        time.sleep(1)


    def right(self,move_in_meter):
        loc = Location()
        loc1 = Location()
        head = self.vehicle.heading
        loc.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc.set_longitude(round(loc.get_longitude()+move_in_meter/100000.0*math.cos(self.vehicle.heading+90),7))  ############maybe 90 or 45 because of the angle
        loc.set_latitude(round(loc.get_latitude()+move_in_meter/100000.0*math.sin(self.vehicle.heading+90),7)) ############maybe 90 or 45 because of the angle
        location_global = LocationGlobal(loc.latitude,loc.longitude,loc.altitude)
        self.vehicle.simple_goto(location_global)
        while True:
            time.sleep(DELAY)
            if abs(self.vehicle.location.global_relative_frame.lat-location_global.lat) < 0.0000001 and abs(self.vehicle.location.global_relative_frame.lon-location_global.lon) < 0.000001:
                break;
            self.condition_yaw(head)

        if move_in_meter > 0:
            print "complete function right"
        else:
            print "complete function left"


    def left(self,move_in_meter):
        self.right(-move_in_meter)


    def condition_yaw(self,heading, relative=False):
        if relative:
            is_relative = 1 #yaw relative to direction of travel
        else:
            is_relative = 0 #yaw is an absolute angle
        msg = self.vehicle.message_factory.command_long_encode(
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
            0, #confirmation
            heading,    # param 1, yaw in degrees
            0,          # param 2, yaw speed deg/s
            1,          # param 3, direction -1 ccw, 1 cw
            is_relative, # param 4, relative offset 1, absolute angle 0
            0, 0, 0)    # param 5 ~ 7 not used
        # send command to vehicle
        self.vehicle.send_mavlink(msg)
