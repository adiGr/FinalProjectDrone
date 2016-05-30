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

        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True
        while not self.vehicle.armed:
            time.sleep(DELAY)
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


    def land(self):
        #high = math.round(self.vehicle.location.global_relative_frame.alt)
        #print high
        self.vehicle.mode = VehicleMode("LAND")
        for x in range(0,5):
            time.sleep(2)
        print "complete land"

    def returnToLanuch(self):
        self.vehicle.mode = VehicleMode("RTL")
        for x in range(0,5):
            time.sleep(2)
        print "complete land"


    def move_forward(self,meter):
        head = self.vehicle.heading
        position_z=self.vehicle.location.global_relative_frame.alt
        meter_in_x = math.cos(math.radians(90-head))*meter
        meter_in_y = math.sin(math.radians(90-head))*meter
        position_z*=-1
        self.command_move(meter_in_x,meter_in_y,position_z)
        for x in range(0,abs(meter)):
            self.condition_yaw(head)
            time.sleep(3)
        if meter >0:
            print "complete move_forward"
        else:
            print "complete move_backwards"
        self.vehicle.flush()

    def move_backwards(self,move_forward_in_meter):
        self.move_forward(-move_forward_in_meter)


    def move_right(self,meter):
        head = self.vehicle.heading
        position_z=self.vehicle.location.global_relative_frame.alt
        meter_in_x = math.sin(math.radians(90+head))*meter
        meter_in_y = math.cos(math.radians(90+head))*meter
        position_z*=-1
        self.set_roi(self.vehicle.location.global_relative_frame)
        self.command_move(meter_in_x,meter_in_y,position_z)
        for x in range(0,abs(meter)):
            self.condition_yaw(head)
            time.sleep(2)  #####chage for test in google

        if meter >0:
            print "complete move_right"
        else:
            print "complete move_left"
        self.vehicle.flush()


    def move_left(self,meter):
        self.move_right(-meter)
        time.sleep(3)


    def command_move(self,meter_in_x,meter_in_y,position_z):
        msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        meter_in_y, meter_in_x, position_z,
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

    @staticmethod
    def get_distance_metres(aLocation1, aLocation2):
        dlat = aLocation2.lat - aLocation1.lat
        dlong = aLocation2.lon - aLocation1.lon
        return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5

    def set_roi(self,location):
    # create the MAV_CMD_DO_SET_ROI command
        msg = self.vehicle.message_factory.command_long_encode(
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_CMD_DO_SET_ROI, #command
        0, #confirmation
        0, 0, 0, 0, #params 1-4
        location.lat,
        location.lon,
        location.alt
        )
        # send command to vehicle
        self.vehicle.send_mavlink(msg)