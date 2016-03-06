__author__ = 'ReemAdi'

LIMIT_LATITUDE = 90.0
LIMIT_LONGITUDE = 180.0


class Location:
    #######################################
    # Constructor
    #######################################
    def __init__(self, _latitude=0.0, _longitude=0.0, _altitude=0.0):
        try:
            _latitude = float (_latitude)
        except ValueError:
            _latitude = 0
        if _latitude<=LIMIT_LATITUDE and _latitude>=-LIMIT_LATITUDE:
            self.latitude = _latitude
        elif _latitude<-LIMIT_LATITUDE:
            self.latitude = -LIMIT_LATITUDE
        else:
            self.latitude = LIMIT_LATITUDE
        #----------------------------------#

        try:
            _longitude = float (_longitude)
        except ValueError:
            _longitude = 0
        if _longitude<=LIMIT_LONGITUDE and _longitude>=-LIMIT_LONGITUDE:
            self.longitude = _longitude
        elif _longitude<-LIMIT_LONGITUDE:
            self.longitude = -LIMIT_LONGITUDE
        else:
            self.longitude = LIMIT_LONGITUDE

        #----------------------------------#
        try:
            self.altitude = float (_altitude)
        except ValueError:
            self.altitude = 0
    #######################################
    # Getters
    #######################################
    def get_latitude(self):
        return self.latitude


    def get_longitude(self):
        return self.longitude


    def get_altitude(self):
        return self.altitude


    #######################################
    # Setters
    #######################################
    def set_latitude(self, _latitude):
        try:
            _latitude = float (_latitude)
        except ValueError:
            _latitude = 0
        if (_latitude <= LIMIT_LATITUDE) and (_latitude >= -LIMIT_LATITUDE):
            self.latitude = _latitude
        elif _latitude<-LIMIT_LATITUDE:
            self.latitude = -LIMIT_LATITUDE
        else:
            self.latitude = LIMIT_LATITUDE


    def set_longitude(self, _longitude):
        try:
            _longitude = float (_longitude)
        except ValueError:
            _longitude = 0
        if (_longitude <= LIMIT_LONGITUDE) and (_longitude >= -LIMIT_LONGITUDE):
            self.longitude = _longitude
        elif _longitude<-LIMIT_LONGITUDE:
            self.latitude = -LIMIT_LONGITUDE
        else:
            self.latitude = LIMIT_LONGITUDE


    def set_altitude(self, _altitude):
        try:
            self.altitude = float (_altitude)
        except ValueError:
            self.altitude = 0
