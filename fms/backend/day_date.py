from datetime import date

def getDate():
    today = date.today()
    dt = today.strftime("%d/%m/%Y")
    return dt

def getDay():
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = date.today()
    return day_list[today.weekday()]   #returns string of that day