from django.shortcuts import render, HttpResponse, redirect

from time import strftime
from datetime import datetime
import pytz

chicago = pytz.timezone('America/Chicago') 
datetime_chi = datetime.now(chicago)

def format_current_time():
    current_time = 'It is ' + str(datetime_chi.strftime('%-I:%M %p %Z'))
    return(current_time)

def format_current_date():
    current_date = ' on ' + str(datetime_chi.strftime('%A, %B %d, %Y.'))
    return(current_date)

def index(request):
    data = {
    	'time': format_current_time(),
        'date': format_current_date()
    }
    return render(request, 'time_display_app/index.html',data)

def time_display(request):
    data = {
    	'time': format_current_time(),
        'date': format_current_date()
    }
    return render(request, 'time_display_app/index.html',data)