from django.conf.urls import url,include
from . import views
urlpatterns = [
        url('^$',views.welcome,name ='welcome'),
        url('^today/$',views.news_of_day,name='newsToday'),
        url('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
]