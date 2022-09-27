def readWaterLevel():
    read_file = open("data.txt", "r+")
    for lastline in read_file:
        pass
    read_file.close()
    return int(lastline[18:20])