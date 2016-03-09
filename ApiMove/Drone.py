__author__ = 'ReemAdi'

from dronekit import connect

class Drone:

    def __init__(self):
        print 'Connecting to vehicle on: /dev/ttyAMA0'
        self.vehicle = connect('/dev/ttyAMA0', baud=57600)


if __name__ == '__main__':
    Drone()

