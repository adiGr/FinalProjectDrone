__author__ = 'ReemAdi'

LIMIT_LATITUDE = 90.0
LIMIT_LONGITUDE = 180.0
DEVIATION = 0.05


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
        if _longitude<=LIMIT_LONGITUDE and _longitude>=0:
            self.longitude = _longitude
        elif _longitude<0:
            self.longitude = 0
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
        if (_longitude <= LIMIT_LONGITUDE) and (_longitude >= 0):
            self.longitude = _longitude
        elif _longitude<0:
            self.longitude = 0
        else:
            self.longitude = LIMIT_LONGITUDE


    def set_altitude(self, _altitude):
        try:
            self.altitude = float (_altitude)
            if _altitude < 0:
                self.altitude = 0
        except ValueError:
            self.altitude = 0



    #######################################
    # Equals
    #######################################
    def equalsTo(self, cmpLocation):
        if cmpLocation.latitude == self.latitude and cmpLocation.longitude == self.longitude and cmpLocation.altitude == self.altitude:
            return True
        else:
            return False

    def is_right_alt(self, high_meter):
        try:
            high_meter =float(high_meter)
        except ValueError:
            return False
        if abs(high_meter - self.altitude)< DEVIATION:
            return True
        return False

    def is_equals_lat(self, lat):
        try:
            lat =float(lat)
        except ValueError:
            return False
        if lat > LIMIT_LATITUDE or lat <-LIMIT_LATITUDE:
            lat = lat% LIMIT_LATITUDE
        if abs(lat - self.latitude) < DEVIATION:
            return True
        return False


    def is_equals_lon(self, lon):
        try:
            lon =float(lon)
        except ValueError:
            return False
        if lon > LIMIT_LONGITUDE or lon <0:
            lon = lon% LIMIT_LATITUDE
        if abs(lon - self.longitude)< DEVIATION:
            return True
        return False

    #######################################
    # Convert From Vehicle Location
    #######################################
    def setFromVehicleLocation(self, vecLoc):
        self.set_latitude(vecLoc.lat)
        self.set_longitude(vecLoc.lon)
        self.set_altitude(vecLoc.alt)


    #######################################
    # Convert From JSON Location
    #######################################
    def setFromJSONLocation(self, JSONLoc):
        self.latitude = JSONLoc['latitude']
        self.longitude = JSONLoc['longitude']
        self.altitude = JSONLoc['altitude']


    #######################################
    # Print Location
    #######################################
    def displayLocation(self):
        print "|  latitude: %0.2f  |  longitude: %0.2f  |  altitude: %0.2f  " % (self.latitude, self.longitude, self.altitude)

