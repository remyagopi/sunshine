from django.conf.urls import url
from .views import LoginView,LogoutView,SignupView

app_name='accounts'

urlpatterns=[
    url(r'^login/$',LoginView,name='login'),
    url(r'^logout/$',LogoutView,name='logout'),
    url(r'^signup/$',SignupView,name='signup'),
]