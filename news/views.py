from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

#view to add date
def news_of_day(request):
    date = dt.date.today()
    #function to convert date object to find exact day
    return render (request,'all-news/today-news.html', {"date": date,})

#converting views
def convert_dates(dates):
    #Function that gets the weekday number for the date
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Returning the actual day of the week
    day = days[day_number]
    return day
#news archives view
def past_days_news(request,past_date):
    try:
        #Converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)
    return render(request,'all-news/past-news.html', {"date":date})
