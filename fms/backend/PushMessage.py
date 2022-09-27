import smtplib

def sendEmail(sendTo, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login("fmsscoe@gmail.com", "v@run2011")
    s.sendmail("fmsscoe@gmail.com", sendTo, message)
    s.quit()

def moderateFloodAlert(severity):
    alert = ("Flood severity is predicted as MODERATE. Please take actions and alert related systems.")
    sendEmail("varun.shelke.22@outlook.com", alert)

def severeFloodAlert(severity):
    alert = ("Flood severity is predicted as HIGH. Please take actions and alert related systems.")
    sendEmail("varun.shelke.22@outlook.com", alert)
    sendEmail("sadalagebhushan@gmail.com", alert)

def fullDamAlert(waterLevel):
    alert = ("Dam is about to get full. Please operate the doors. Water level is " + str(30 - waterLevel))
    sendEmail("varun.shelke.22@outlook.com", alert)