from django.conf.urls import url
from .views import PostList,PostDetailView, PostCreateView,PostDeleteView,PostUpdateView

app_name='post'

urlpatterns=[
    url(r'^$',PostList,name='list'),
    url(r'^(?P<pk>\d+)/$',PostDetailView,name='detail'),
    url(r'^create/$', PostCreateView, name='post-create'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView,name='delete'),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView, name='update'),

]
