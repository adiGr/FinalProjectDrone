from unittest import TestCase
from Location import Location
import json
import requests

__author__ = 'ReemAdi'

LIMIT_NUMBER_LATITUDE = 90
LIMIT_NUMBER_LONGITUDE = 180
POSITIVE_NUMBER = 47839754.97894
NEGATIVE_NUMBER = -55646545.654565445
CHARACTER = 'C'
CHAR_NUMBER = '48.37589'



class Vec:

    def __init__(self,lat,lon,alt):
        self.lat  = lat
        self.lon = lon
        self.alt = alt

class TestLocation(TestCase):


    def test_get_latitude(self):
        #check the default number
        self.assertEqual(Location().get_latitude(),0)
        #check number positive the limit
        self.assertEqual(Location(LIMIT_NUMBER_LATITUDE).get_latitude(),LIMIT_NUMBER_LATITUDE)
        #check number negative the limit
        self.assertEqual(Location(-LIMIT_NUMBER_LATITUDE).get_latitude(),-LIMIT_NUMBER_LATITUDE)
        #check number positive the limit
        self.assertEqual(Location(LIMIT_NUMBER_LATITUDE+1).get_latitude(),LIMIT_NUMBER_LATITUDE)
        #check number negative the limit
        self.assertEqual(Location(-LIMIT_NUMBER_LATITUDE-1).get_latitude(),-LIMIT_NUMBER_LATITUDE)
        #check char in the function init
        self.assertEqual(Location(CHARACTER,'3',0).get_latitude(),0)
        #check char in the function init
        self.assertEqual(Location(CHAR_NUMBER,'3',0).get_latitude(),float(CHAR_NUMBER))


    def test_get_longitude(self):
        #check the default number : zero
        self.assertEqual(Location().get_longitude(),0)
        #check the number zero
        self.assertEqual(Location(0,0,0).get_longitude(),0)
        #check the positive number: the limit
        self.assertEqual(Location(0,LIMIT_NUMBER_LONGITUDE).get_longitude(),LIMIT_NUMBER_LONGITUDE)
        #check the negative number: the limit
        self.assertEqual(Location(0,-LIMIT_NUMBER_LONGITUDE).get_longitude(),0)
        #check positive out of the limit
        self.assertEqual(Location(0,LIMIT_NUMBER_LONGITUDE+1).get_longitude(),LIMIT_NUMBER_LONGITUDE)
        #check negative out of the limit:
        self.assertEqual(Location(0,-LIMIT_NUMBER_LONGITUDE-1).get_longitude(),0)
        #check char in the function init
        self.assertEqual(Location(0,CHARACTER,0).get_longitude(),0)
        #check char in the function init
        self.assertEqual(Location(0,CHAR_NUMBER,0).get_longitude(),float(CHAR_NUMBER))

    def test_get_altitude(self):
        #check the get function
        self.assertEqual(Location().get_altitude(),0)
        #check the zero
        self.assertEqual(Location(0,0,0).get_altitude(),0)
        #check the positive number
        self.assertEqual(Location(0,0,POSITIVE_NUMBER).get_altitude(),POSITIVE_NUMBER)
        #check the negative number
        self.assertEqual(Location(0,0,NEGATIVE_NUMBER).get_altitude(),NEGATIVE_NUMBER)
        #check when enter a string no number:
        self.assertEqual(Location(0,0,CHARACTER).get_altitude(),0)
        #check when enter a string that number:
        self.assertEqual(Location(0,0,CHAR_NUMBER).get_altitude(),float(CHAR_NUMBER))


    def test_set_latitude(self):
        #create object location
        loc = Location()
        #set the default location
        loc.set_latitude(0)
        self.assertTrue(loc.get_latitude() == 0)
        #set latitude limit positive number
        loc.set_latitude(LIMIT_NUMBER_LATITUDE)
        self.assertTrue(loc.get_latitude() == LIMIT_NUMBER_LATITUDE)
        #check is success the set on the latitude the underscore limit
        loc.set_latitude(-LIMIT_NUMBER_LATITUDE)
        self.assertTrue(loc.get_latitude() == -LIMIT_NUMBER_LATITUDE)
        #check if the number that not in the limits set the closest number limit.
        loc.set_latitude(LIMIT_NUMBER_LATITUDE+1)
        self.assertEqual(loc.get_latitude(),LIMIT_NUMBER_LATITUDE)
        loc.set_latitude(-LIMIT_NUMBER_LATITUDE-1)
        self.assertEqual(loc.get_latitude(),-LIMIT_NUMBER_LATITUDE)
        #check if the latitude set a character when it's character - set zero
        loc.set_latitude(CHARACTER)
        self.assertEqual(loc.get_latitude(),0)
        #when it's number - set the number as float
        loc.set_latitude(CHAR_NUMBER)
        self.assertEqual(loc.get_latitude(),float(CHAR_NUMBER))


    def test_set_longitude(self):
        loc=Location()
        loc.set_longitude(0)
        #check if the longitude equal to zero
        self.assertEqual(loc.get_longitude(),0)
        #set function change to limit  number
        loc.set_longitude(LIMIT_NUMBER_LONGITUDE)
        self.assertEqual(loc.get_longitude(),LIMIT_NUMBER_LONGITUDE)
        #out of limit number LIMIT_NUMBER_LONGITUDE
        loc.set_longitude(LIMIT_NUMBER_LONGITUDE+1)
        self.assertEqual(loc.get_longitude(),LIMIT_NUMBER_LONGITUDE)
        #set lower limit
        loc.set_longitude(-LIMIT_NUMBER_LONGITUDE)
        self.assertEqual(loc.get_longitude(),0)
        #set less then lower limit-> set the lower limit
        loc.set_longitude(-LIMIT_NUMBER_LONGITUDE-1)
        self.assertEqual(loc.get_longitude(),0)
        #check if the latitude set a character
        loc.set_longitude(CHARACTER)
        self.assertEqual(loc.get_longitude(),0)
        #check if the latitude set a character number
        loc.set_longitude(CHAR_NUMBER)
        self.assertEqual(loc.get_longitude(),float(CHAR_NUMBER))


    def test_set_altitude(self):
        loc = Location()
        #set the default location
        self.assertEqual(loc.get_altitude(),0)
        loc.set_altitude(0)
        self.assertEqual(loc.get_altitude(),0)
        #check character -> set zero
        loc.set_altitude(CHARACTER)
        self.assertEqual(loc.get_altitude(),0)
        #check character number -> convert to the number
        loc.set_altitude(CHAR_NUMBER)
        self.assertEqual(loc.get_altitude(),float(CHAR_NUMBER))


    def test_equalsTo(self):
        loc = Location()
        loc1 = Location()
        #---------------latitude--------------------#
        self.assertTrue(loc.equalsTo(loc1))
        loc1.set_latitude(LIMIT_NUMBER_LATITUDE)
        self.assertFalse(loc.equalsTo(loc1))
        loc.set_latitude(LIMIT_NUMBER_LATITUDE)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_latitude(LIMIT_NUMBER_LATITUDE+1)
        self.assertTrue(loc.equalsTo(loc1))
        loc1.set_latitude(LIMIT_NUMBER_LATITUDE+1)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_latitude(-LIMIT_NUMBER_LATITUDE)
        self.assertFalse(loc.equalsTo(loc1))
        loc1.set_latitude(-LIMIT_NUMBER_LATITUDE)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_latitude(-LIMIT_NUMBER_LATITUDE-1)
        self.assertTrue(loc.equalsTo(loc1))
        loc1.set_latitude(-LIMIT_NUMBER_LATITUDE-1)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_latitude(CHARACTER)
        self.assertFalse(loc.equalsTo(loc1))
        loc1.set_latitude(CHARACTER)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_latitude(CHAR_NUMBER)
        self.assertFalse(loc.equalsTo(loc1))
        loc1.set_latitude(CHAR_NUMBER)
        self.assertTrue(loc.equalsTo(loc1))
        #print "%f   %f " % ( loc.longitude, loc.latitude)
        #print "%f   %f " % ( loc1.longitude, loc1.latitude)
        #---------------longitude-------------------------#
        loc1.set_longitude(LIMIT_NUMBER_LONGITUDE)
        self.assertFalse(loc.equalsTo(loc1))
        loc.set_longitude(LIMIT_NUMBER_LONGITUDE)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_longitude(LIMIT_NUMBER_LONGITUDE+1)
        #print "%f   %f " % ( loc.longitude, loc.latitude)
        #print "%f   %f " % ( loc1.longitude, loc1.latitude)
        self.assertTrue(loc.equalsTo(loc1))
        loc1.set_longitude(LIMIT_NUMBER_LONGITUDE+1)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_longitude(-LIMIT_NUMBER_LONGITUDE)
        self.assertFalse(loc.equalsTo(loc1))
        loc1.set_longitude(-LIMIT_NUMBER_LONGITUDE)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_longitude(-LIMIT_NUMBER_LONGITUDE-1)
        self.assertTrue(loc.equalsTo(loc1))
        loc1.set_longitude(-LIMIT_NUMBER_LONGITUDE-1)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_longitude(CHARACTER)
        self.assertTrue(loc.equalsTo(loc1))
        loc1.set_longitude(CHARACTER)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_longitude(CHAR_NUMBER)
        self.assertFalse(loc.equalsTo(loc1))
        loc1.set_longitude(CHAR_NUMBER)
        self.assertTrue(loc.equalsTo(loc1))
        #-------------altitude--------------------#
        loc.set_altitude(CHARACTER)
        self.assertTrue(loc.equalsTo(loc1))
        loc.set_altitude(CHAR_NUMBER)
        self.assertFalse(loc.equalsTo(loc1))
        loc1.set_altitude(CHAR_NUMBER)
        self.assertTrue(loc.equalsTo(loc1))

    def test_setFromVehicleLocation(self):
        #test Vehicle and after that check the location
        vec= Vec(0,0,0)
        loc = Location()
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        vec.alt == loc.altitude and
                        vec.lat == loc.latitude)
        vec= Vec(LIMIT_NUMBER_LATITUDE,0,0)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        vec.alt == loc.altitude and
                        vec.lat == loc.latitude)
        vec= Vec(LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE,0)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        vec.alt == loc.altitude and
                        vec.lat == loc.latitude)
        vec= Vec(LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE,POSITIVE_NUMBER)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        vec.alt == loc.altitude and
                        vec.lat == loc.latitude)

        vec= Vec(LIMIT_NUMBER_LATITUDE+1,LIMIT_NUMBER_LONGITUDE,POSITIVE_NUMBER)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        vec.alt == loc.altitude and
                        LIMIT_NUMBER_LATITUDE == loc.latitude)
        vec= Vec(LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE+1,POSITIVE_NUMBER)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(LIMIT_NUMBER_LONGITUDE == loc.longitude and
                        vec.alt == loc.altitude and
                        vec.lat == loc.latitude)
        vec= Vec(LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE,CHAR_NUMBER)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        float(vec.alt) == loc.altitude and
                        vec.lat == loc.latitude)
        vec= Vec(LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE,CHARACTER)
        loc.setFromVehicleLocation(vec)
        self.assertTrue(vec.lon == loc.longitude and
                        0 == loc.altitude and
                        vec.lat == loc.latitude)



    def test_displayLocation(self):
        loc = Location()
        loc.displayLocation()
        loc= Location(LIMIT_NUMBER_LATITUDE,0,0)
        loc.displayLocation()
        loc=Location(-LIMIT_NUMBER_LATITUDE,0,0)
        loc.displayLocation()
        loc=Location(LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE,0)
        loc.displayLocation()
        loc=Location(LIMIT_NUMBER_LATITUDE,-LIMIT_NUMBER_LONGITUDE,0)
        loc.displayLocation()
        loc=Location(-LIMIT_NUMBER_LATITUDE,LIMIT_NUMBER_LONGITUDE,0)
        loc.displayLocation()
        loc=Location(-LIMIT_NUMBER_LATITUDE,-LIMIT_NUMBER_LONGITUDE,0)
        loc.displayLocation()
        self.assertTrue(1)

    def test_is_right_alt(self):
        loc = Location()
        self.assertFalse(loc.is_right_alt(CHARACTER))
        self.assertFalse(loc.is_right_alt(CHAR_NUMBER))
        loc.set_altitude(CHAR_NUMBER)
        self.assertTrue(loc.is_right_alt(CHAR_NUMBER))
        self.assertTrue(loc.is_right_alt(float(CHAR_NUMBER)-0.04))
        self.assertTrue(loc.is_right_alt(float(CHAR_NUMBER)+0.04))
        self.assertFalse(loc.is_right_alt(float(CHAR_NUMBER)-0.06))
        self.assertFalse(loc.is_right_alt(float(CHAR_NUMBER)+0.06))
        self.assertTrue(loc.is_right_alt(float(CHAR_NUMBER)-0.05))
        self.assertTrue(loc.is_right_alt(float(CHAR_NUMBER)+0.05))
        self.assertFalse(loc.is_right_alt(float(CHAR_NUMBER)-0.051))
        self.assertFalse(loc.is_right_alt(float(CHAR_NUMBER)+0.051))

    def test_is_equals_lat(self):
        loc = Location()
        self.assertTrue(loc.is_equals_lat(0))
        self.assertFalse(loc.is_equals_lat(1))
        self.assertFalse(loc.is_equals_lat(0.05))
        self.assertFalse(loc.is_equals_lat(-0.05))
        self.assertFalse(loc.is_equals_lat(-0.06))
        self.assertTrue(loc.is_equals_lat(-0.04))
        self.assertTrue(loc.is_equals_lat(-0.03))
        self.assertTrue(loc.is_equals_lat(-0.02))
        self.assertTrue(loc.is_equals_lat(-0.01))
        self.assertTrue(loc.is_equals_lat(+0.04))
        self.assertTrue(loc.is_equals_lat(+0.03))
        self.assertTrue(loc.is_equals_lat(+0.02))
        self.assertTrue(loc.is_equals_lat(+0.01))
        self.assertFalse(loc.is_right_alt(CHARACTER))
        self.assertFalse(loc.is_right_alt(CHAR_NUMBER))
        loc.set_latitude(LIMIT_NUMBER_LATITUDE)
        self.assertTrue(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE+1))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE+0.05))
        self.assertTrue(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE-0.05))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE-0.06))
        self.assertTrue(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE-0.04))
        self.assertTrue(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE-0.03))
        self.assertTrue(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE-0.02))
        self.assertTrue(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE-0.01))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE+0.04))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE+0.03))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE+0.02))
        self.assertFalse(loc.is_equals_lat(LIMIT_NUMBER_LATITUDE+0.01))
        loc.set_latitude(-LIMIT_NUMBER_LATITUDE)
        self.assertTrue(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+1))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE-0.05))
        self.assertTrue(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+0.05))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+0.06))
        self.assertTrue(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+0.04))
        self.assertTrue(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+0.03))
        self.assertTrue(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+0.02))
        self.assertTrue(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE+0.01))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE-0.04))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE-0.03))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE-0.02))
        self.assertFalse(loc.is_equals_lat(-LIMIT_NUMBER_LATITUDE-0.01))



    def test_is_equals_lon(self):
        loc = Location()
        self.assertTrue(loc.is_equals_lon(0))
        self.assertFalse(loc.is_equals_lon(1))
        self.assertFalse(loc.is_equals_lon(0.05))
        self.assertFalse(loc.is_equals_lon(-0.05))
        self.assertFalse(loc.is_equals_lon(-0.06))
        self.assertFalse(loc.is_equals_lon(-0.04))
        self.assertFalse(loc.is_equals_lon(-0.03))
        self.assertFalse(loc.is_equals_lon(-0.02))
        self.assertFalse(loc.is_equals_lon(-0.01))
        self.assertTrue(loc.is_equals_lon(+0.04))
        self.assertTrue(loc.is_equals_lon(+0.03))
        self.assertTrue(loc.is_equals_lon(+0.02))
        self.assertTrue(loc.is_equals_lon(+0.01))
        self.assertFalse(loc.is_equals_lon(CHARACTER))
        self.assertFalse(loc.is_equals_lon(CHAR_NUMBER))
        loc.set_longitude(LIMIT_NUMBER_LONGITUDE)
        self.assertTrue(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE+1))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE+0.05))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE-0.05))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE-0.06))
        self.assertTrue(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE-0.04))
        self.assertTrue(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE-0.03))
        self.assertTrue(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE-0.02))
        self.assertTrue(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE-0.01))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE+0.04))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE+0.03))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE+0.02))
        self.assertFalse(loc.is_equals_lon(LIMIT_NUMBER_LONGITUDE+0.01))



