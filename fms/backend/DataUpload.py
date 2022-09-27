import pyrebase

firebaseConfig = {
        "apiKey": "AIzaSyD-UEho90R68TxuYs1Yidf8Ja6XAPL0pmA",
        "authDomain": "flood-management-system-7c12f.firebaseapp.com",
        "databaseURL": "https://flood-management-system-7c12f.firebaseio.com",
        "projectId": "flood-management-system-7c12f",
        "storageBucket": "flood-management-system-7c12f.appspot.com",
        "messagingSenderId": "406115454100",
        "appId": "1:406115454100:web:7f4d97e3ade08986f33881"
      }
def dataBackup(fileName):

    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()

    path_on_cloud = "Rainfall Data/" + fileName
    path_local = fileName
    storage.child(path_on_cloud).put(path_local)