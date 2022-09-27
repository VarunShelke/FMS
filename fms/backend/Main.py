import time
from . import HCSR04 as wls
from . import PushEmail as eml
from . import DataWrite
from . import ServoMotor as sm
from . import WeatherAPI as api
from . import kNN

def execute():
    while(True):
        rainFall = []
        damLevelPercent = []
        waterLevel = wls.distance()        #gets distance between water and the sensor
        #if(sm.isGateOpen == 1 and waterLevel > 5):
            #sm.closeGates()
        if(waterLevel < 5):
            eml.fullDamAlert(waterLevel)
            #if(waterLevel <= 3):
                #sm.openGates()
        damLevelPercent.append(((11 - waterLevel) * 181.81) / 2000 * 100)
        rainFall.append(api.getRainfallData())
        DataWrite.fileWrite(waterLevel, rainFall[0])
        severity = kNN.kNN_algorithm(rainFall, damLevelPercent)
        if(severity == 2):
            eml.moderateFloodAlert(severity)
        elif(severity == 3):
            eml.severeFloodAlert(severity)
        time.sleep(15)