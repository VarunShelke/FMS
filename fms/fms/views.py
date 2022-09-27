from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from pandas import ExcelWriter
from pandas import ExcelFile
import csv, io
import pandas as pd
import openpyxl
from . import jk
import threading
import datetime
from datetime import date
from backend import Main
from backend import WeatherAPI as api

a=0
b=0
c=0
d=0

rainfall = api.getRainfallData()
dt = date.today()
day = datetime.date.today().strftime("%A")

context = {'rain': rainfall, 'date': dt, 'day': day}
#Threading Block ------------------------------------------------------------------
backend_thread = threading.Thread(target = Main.execute)
backend_thread.start()
#----------------------------------------------------------------------------------
def login(request):
    if request.method == "POST":
        user=request.POST['username']
        pass1=request.POST['password']
    if user=="admin" and pass1=="admin":
        messages.success(request, "You are successfully Logged In!!! Dam is in Automation Mode!!")
        return render(request,'gate_con.html', context)
    else:
        messages.error(request,"Enter valid credentials!!")
        return render(request,"auth.html")

def auto(request):
    if request.POST:
        if '_on' in request.POST:
            messages.success(request, "Dam is in Automation Mode!!")
            return render(request, 'gate_con.html', context)
        elif '_off' in request.POST:
            a=1
            messages.success(request, "Dam is in Manual Mode!!")
            return render(request, 'doorcon.html', context)
c=a
def door_con(request):
    if request.POST:
        if '_op' in request.POST:
            messages.success(request, "Doors are opened!!")
            return render(request, 'doorcon.html', context)
        elif '_cl' in request.POST:
            messages.success(request, "Doors are closed!!")
            return render(request, 'doorcon.html', context)

def auth(request):
    jk.jk()
    return render(request,'auth.html')

def gate_con(request):
    if c==0:
        return render(request, 'gate_con.html', context)
    elif c==1:
        return render(request, 'doorcon.html', context)

def fetch_data(request):
    return render(request, 'fet.html')

def down_month_csv(request):
    dd = pd.read_excel("Dam.xlsx", index=False)
    con={'DATE': str}
    dd=dd.astype(con)
    dd.reset_index(drop=True)
    df = dd[['DATE', 'Water Level(cubic-ft/sec)', 'Water Level(cubic-meter/sec)', 'Water Storage(cubic-ft/sec)', 'Water Storage(cubic-meter/sec)', 'Availlable percent', 'Rainfall', 'Total Rainfall']]
    if request.method == "POST":
        dd=request.POST['mm']
        item = df[df['DATE'].str.contains(dd)]
        co = {'DATE': object}
        item = item.astype(co)
        df = item
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    writer = ExcelWriter(response)
    item.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    return response

def down_year_csv(request):
    dd = pd.read_excel("Dam.xlsx", index=False)
    con = {'DATE': str}
    dd = dd.astype(con)
    dd.reset_index(drop=True)
    df = dd[['DATE', 'Water Level(cubic-ft/sec)', 'Water Level(cubic-meter/sec)', 'Water Storage(cubic-ft/sec)', 'Water Storage(cubic-meter/sec)', 'Availlable percent', 'Rainfall', 'Total Rainfall']]
    if request.method == "POST":
        dd = request.POST['yy']
        item = df[df['DATE'].str.contains(dd)]
        co = {'DATE': object}
        item = item.astype(co)
        df = item
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    writer = ExcelWriter(response)
    item.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    return response

def down_date_csv(request):
    dd = pd.read_excel("Dam.xlsx", index=False)
    con = {'DATE': str}
    dd = dd.astype(con)
    dd.reset_index(drop=True)
    df = dd[['DATE', 'Water Level(cubic-ft/sec)', 'Water Level(cubic-meter/sec)', 'Water Storage(cubic-ft/sec)', 'Water Storage(cubic-meter/sec)', 'Availlable percent', 'Rainfall', 'Total Rainfall']]
    if request.method == "POST":
        dd = request.POST['dd']
        item = df[df['DATE'].str.contains(dd)]
        co = {'DATE': object}
        item = item.astype(co)
        df = item
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    writer = ExcelWriter(response)
    item.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    return response