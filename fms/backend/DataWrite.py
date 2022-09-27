import os
import time
from datetime import date
from . import DataUpload
def fileWrite(waterLevel, rainFall):
    timeStamp = time.localtime()
    today = date.today()
    readable = time.strftime("%x %X", timeStamp)
    fileName = (str(today) + ".txt")
    if(readable[9:11] == "00"):
        os.rename("data.txt", fileName)
        DataUpload.dataBackup(fileName)
    data_write = open("data.txt","a")
    data_write.write(str(readable) + "\t" + str(waterLevel) + str(rainFall) +  "\n")
    data_write.close()