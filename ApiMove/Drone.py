import time


__author__ = 'ReemAdi'

from dronekit import *
from Location import Location

DELAY = 3
DELAY_HALF_SEC = 0.5
ANGLE_FIX = 2
RIGHT_ANGLE = 90


class Drone:

    def __init__(self,connect_string = '/dev/ttyAMA0'):
        print 'Connecting to vehicle on: '+connect_string
        self.vehicle = connect(connect_string, wait_ready=True,baud=57600)
        self.is_first_function = False

    """ the function get the meter to take of
    and change the mode to guided and take of the drone
    when the function end the drone complete take off"""
    def take_off(self,init_alt_in_meter):
        while not self.vehicle.is_armable:
            time.sleep(DELAY_HALF_SEC)
            print "Waiting for arming"

        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True
        while not self.vehicle.armed:
            time.sleep(DELAY_HALF_SEC)
        meter  = init_alt_in_meter
        self.vehicle.simple_takeoff(meter)
        loc = Location()
        loc.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
        while not loc.is_right_alt(meter):
            loc.setFromVehicleLocation(self.vehicle.location.global_relative_frame)
            time.sleep(DELAY_HALF_SEC)
        #self.up(1)

    """ the function get the meter to move up
    according global frame location
    the function end when the drone get to the location plus the meter"""
    def up(self,init_alt_in_meter):
        if(self.is_first_function):
            head = self.vehicle.heading/ANGLE_FIX
            self.is_first_function = False
        else:
            head= self.vehicle.heading
        loc = Location()
        loc1 = Location()
        loc.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
        loc.set_altitude(loc.get_altitude()+init_alt_in_meter)
        location_global = LocationGlobal(loc.latitude,loc.longitude,loc.altitude)
        self.vehicle.simple_goto(location_global)
        while not loc1.is_right_alt(loc.altitude):
            loc1.setFromVehicleLocation(self.vehicle.location.global_frame)
            self.condition_yaw(head)
            time.sleep(DELAY)
        if init_alt_in_meter > 0:
            print "complete function up"
        else:
            print "complete function down"

    """ the function call the self.up with inverse param  """
    def down(self,init_alt_in_meter):
        self.up(-init_alt_in_meter)

    """the function change mode to land
    and land the drone in location that located  """
    def land(self):
        self.vehicle.mode = VehicleMode("LAND")
        for x in range(0,5):
            time.sleep(DELAY)
        print "complete land"


    """ the function change mode to RTL
    and land the drone in location that armed"""
    def returnToLanuch(self):
        self.vehicle.mode = VehicleMode("RTL")
        for x in range(0,5):
            time.sleep(DELAY)
        print "complete land"

    """ the function get the meter to move forward
    with reference to the heading
    the function end when the drone complete move forward"""
    def move_forward(self,meter):
        if(self.is_first_function):
            head = self.vehicle.heading/ANGLE_FIX
            self.is_first_function = False
        else:
            head= self.vehicle.heading
        position_z=self.vehicle.location.global_relative_frame.alt
        meter_in_x = math.sin(math.radians(head))*meter
        meter_in_y = math.cos(math.radians(head))*meter
        position_z*=-1
        self.command_move(meter_in_x,meter_in_y)
        for x in range(0,abs(meter)):
            self.condition_yaw(head)
            time.sleep(DELAY)
        if meter >0:
            print "complete move_forward"
        else:
            print "complete move_backwards"

    """ the function call the forward with inverse param  """
    def move_backwards(self,move_forward_in_meter):
        self.move_forward(-move_forward_in_meter)

    """ the function get the meter to move right
    with reference to the heading
    the function end when the drone complete move right"""
    def move_right(self,meter):
        if(self.is_first_function):
            head = self.vehicle.heading/ANGLE_FIX
            self.is_first_function = False
        else:
            head= self.vehicle.heading
        position_z=self.vehicle.location.global_relative_frame.alt
        meter_in_x = math.sin(math.radians(RIGHT_ANGLE +head))*meter
        meter_in_y = math.cos(math.radians(RIGHT_ANGLE +head))*meter
        position_z*=-1
        self.command_move(meter_in_x,meter_in_y)
        for x in range(0,abs(meter)):
            self.condition_yaw(head)
            time.sleep(DELAY)
        if meter >0:
            print "complete move_right"
        else:
            print "complete move_left"


    """ the function move the drone left with distance meter
     and call the right with inverse param  """
    def move_left(self,meter):
        self.move_right(-meter)


    def command_move(self,meter_in_x,meter_in_y):
        msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
        0,       #(not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_OFFSET_NED, # frame
        0b0000111111111000, # type_mask (only positions)
        meter_in_y, meter_in_x, 0,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
        # send command to vehicle
        self.vehicle.send_mavlink(msg)

    def condition_yaw(self,heading):
        msg = self.vehicle.message_factory.command_long_encode(
            0, 0,    # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
            0, #confirmation
            heading,    # param 1, yaw in degrees
            0,          # speed deg/s
            1,          # param 3, direction -1 ccw, 1 cw
            0, # absolute angle 0
            0, 0, 0)    # param 5 ~ 7 not used
        # send command to vehicle
        self.vehicle.send_mavlink(msg)