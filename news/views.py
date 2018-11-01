from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

#view to add date
def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    #function to convert date object to find exact day
    return render (request,'all-news/today-news.html', {"date": date,"news":news})


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
    news = Article.days_news(date)
    return render(request,'all-news/past-news.html', {"date":date,"news":news})

#view for search results
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request,'all-news/search.html',{"message":message,"articles":searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

#view to add a single article
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html",{"article":article})
