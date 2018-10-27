from django.conf.urls import url
from .views import BlogHome

app_name='blog_details'

urlpatterns=[
    url(r'^$',BlogHome,name='home'),
]