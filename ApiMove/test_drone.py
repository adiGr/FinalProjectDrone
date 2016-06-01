from unittest import TestCase
from Drone import Drone
from dronekit_sitl import SITL
import math

__author__ = 'ReemAdi'


class TestDrone(TestCase):
    def test_take_off(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        headBefor =drone.vehicle.heading
        locBefor = drone.vehicle.location.global_relative_frame
        drone.take_off(3)
        headAfter = drone.vehicle.heading
        locAfter = drone.vehicle.location.global_relative_frame
        self.assertTrue( round(locAfter.alt-locBefor.alt)==3 and ((headBefor+5)%360<headAfter or(headBefor-5)%360 >headAfter))
        drone.vehicle.close()
        sitl.stop()

    def test_up(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        headBefor =drone.vehicle.heading
        locBefor = drone.vehicle.location.global_relative_frame
        drone.take_off(3)
        headAfter = drone.vehicle.heading
        locAfter = drone.vehicle.location.global_relative_frame
        drone.up(2)
        print drone.vehicle.location.global_relative_frame
        drone.up(4)
        print drone.vehicle.location.global_relative_frame
        drone.up(1)
        print drone.vehicle.location.global_relative_frame
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)

    def test_down(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        headBefor =drone.vehicle.heading
        locBefor = drone.vehicle.location.global_relative_frame
        drone.take_off(25)
        headAfter = drone.vehicle.heading
        locAfter = drone.vehicle.location.global_relative_frame
        drone.down(1)
        print drone.vehicle.location.global_relative_frame
        drone.down(4)
        print drone.vehicle.location.global_relative_frame
        drone.down(5)
        print drone.vehicle.location.global_relative_frame
        drone.vehicle.close()
        sitl.stop()

    def test_land(self):
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        headBefor =drone.vehicle.heading
        locBefor = drone.vehicle.location.global_relative_frame
        drone.take_off(25)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        print drone.vehicle.location.global_relative_frame
        drone.take_off(4)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        print drone.vehicle.location.global_relative_frame
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        print drone.vehicle.location.global_relative_frame
        drone.take_off(10)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        print drone.vehicle.location.global_relative_frame
        drone.vehicle.close()
        sitl.stop()

    def test_move_forward(self):

        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        """""
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,45']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,90']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,135']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,180']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,225']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,270']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,315']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_forward(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
    def test_move_backwards(self):
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        """""
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,45']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,90']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,135']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,180']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,225']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,270']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,315']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_backwards(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
    def test_move_right(self):
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        """""
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,45']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,90']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,135']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,180']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,225']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,270']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,315']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_right(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """

    def test_move_left(self):
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,0']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        """""
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,45']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,90']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,135']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,180']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """
        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,225']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """

        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,270']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)

        """"
        sitl = SITL()
        sitl.download('copter', '3.3', verbose=True)
        sitl_args = ['-I0', '--model', 'quad', '--home=31.768923,35.193595,0,315']
        sitl.launch(sitl_args, await_ready=True, restart=True)
        drone = Drone('tcp:127.0.0.1:5760')
        drone.take_off(2)
        print drone.vehicle.location.global_relative_frame
        drone.move_left(2)
        print drone.vehicle.location.global_relative_frame
        drone.land()
        drone.vehicle.close()
        sitl.stop()
        #self.assertTrue(True)
        """

