__author__ = 'ReemAdi'



FULL_BATTERY_LEVEL = 100
LOW_BATTERY_LEVEL = 5

class Battery:
    def __init__(self,battery):
        if battery.voltage < 0:
            self.volt = 0
        else:
            self.volt = battery.voltage
        if battery.current is None:
            self.current = 0
        else:
            self.current = battery.current
        if battery.level is None:
            self.level = 0
        else:
            self.level = battery.level


    #######################################
    # Setters                             #
    #######################################
    def set_volt(self,volt):
        if volt > 0:
            self.volt = volt
        else:
            self.volt = 0

    def set_current(self,curr):
        if curr is None:
            self.current = 0
        else:
            self.current = curr

    def set_level(self,lvl):
        if lvl is None:
            self.level = 0
        else:
            self.level = lvl


    def set_battery_from_vehicle(self,battery):
        self.set_volt(battery.voltage)
        self.set_current(battery.current)
        self.set_level(battery.level)

    #######################################
    # Getters                             #
    #######################################
    def get_volt(self):
        return self.volt

    def get_current(self):
        return self.current

    def get_level(self):
        return self.level



    def if_full_battery_level(self):
        if self.level >= FULL_BATTERY_LEVEL:
            return True
        return False

    def if_low_battery_level(self):
        if self.level is None:
            print "the autopilot cannot estimate the remaining battery"
        if self.level is None or self.level <= LOW_BATTERY_LEVEL:
            return True
        return False


