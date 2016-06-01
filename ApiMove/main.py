import time

__author__ = 'ReemAdi'
import sys
from Drone import Drone
from dronekit_sitl import SITL
import datetime
from Battery import Battery
from dronekit import *

def main():
    print "Start simulator (SITL)"
    sitl = SITL()
    sitl.download('copter', '3.3', verbose=True)
    sitl_args = ['-I0', '--model', 'quad', '--home=31.768797, 35.193556,0,315 ']
    sitl.launch(sitl_args, await_ready=True, restart=True)
    # Import DroneKit-Python
    # Connect to the Vehicle.


    drone = Drone('tcp:127.0.0.1:5760')
    #drone = Drone("com3")
    drone.take_off(3)

    #drone.up(3)
    print "#######################################################################################"
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    drone.move_forward(2)
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    print "#######################################################################################"
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    drone.move_right(2)
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    print "#######################################################################################"
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    drone.move_backwards(2)
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    print "#######################################################################################"
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    drone.move_left(2)
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    print "#######################################################################################"
    #print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    #drone.move_backwards(2)
    #print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    #print "#######################################################################################"

    drone.land()
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    print "the heading is : %s" % drone.vehicle.heading
    print "#######################################################################################"
    drone.vehicle.close()
    #f.close()
    # Shut down simulator
    sitl.stop()
    print("Completed")

if __name__ == '__main__':
    main()