import time

__author__ = 'ReemAdi'
import sys
from Drone import Drone
from dronekit_sitl import SITL
from Battery import Battery


def main():
    print "Start simulator (SITL)"
    sitl = SITL()
    sitl.download('copter', '3.3', verbose=True)
    sitl_args = ['-I0', '--model', 'quad', '--home=-35.363261,149.165230,584,353']
    sitl.launch(sitl_args, await_ready=True, restart=True)

    # Import DroneKit-Python
    from dronekit import connect, VehicleMode

    # Connect to the Vehicle.
    """print "Connecting to vehicle on: 'tcp:127.0.0.1:5760'"
    vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

    # Get some vehicle attributes (state)
    print "Get some vehicle attribute values:"
    print " GPS: %s" % vehicle.gps_0
    print " Battery: %s" % vehicle.battery
    print " Last Heartbeat: %s" % vehicle.last_heartbeat
    print " Is Armable?: %s" % vehicle.is_armable
    print " System status: %s" % vehicle.system_status.state
    print " Mode: %s" % vehicle.mode.name    # settable
    print "Global Location: %s" % vehicle.location.global_frame


    print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)
    print " Mode: %s" % vehicle.mode.name    # settable

    vehicle.simple_takeoff(2)
    print "Global Location: %s" % vehicle.location.global_frame


    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt
        #Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>=2*0.95:
            print "Reached target altitude"
            break
        time.sleep(1)

    print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame




    battery = vehicle.battery
    battery = Battery (battery)
    print " Battery: %s\n" % battery.volt
    print " Battery: %s\n" % battery.current
    print " Battery: %s\n" % battery.level

    vehicle.close()
    """

    drone = Drone('tcp:127.0.0.1:5760')
    drone.take_off(2)
    print " global_relative_frame: %s\n" %  drone.vehicle.location.global_relative_frame
    #drone.up(3)
    #print " global_relative_frame up drone: %s\n" %  drone.vehicle.location.global_relative_frame
    #drone.down(1)
    #print " global_relative_frame down drone: %s\n" %  drone.vehicle.location.global_relative_frame
    #drone.down(4)
    #print " global_relative_frame down drone: %s\n" %  drone.vehicle.location.global_relative_frame
    # Close vehicle object before exiting script
    print "the heading is : %s" % drone.vehicle.heading
    #drone.forward(2)
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    #drone.backwards(2)
    print " global_relative_frame forward drone: %s\n" %  drone.vehicle.location.global_relative_frame
    # Shut down simulator
    sitl.stop()
    print("Completed")

if __name__ == '__main__':
    main()