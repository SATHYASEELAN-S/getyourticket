from django.urls import path
from . import views
app_name='user'

urlpatterns=[
    path('',views.home,name='home'),
    path('logout/',views.logoutuser,name='logout'),
    path('login/',views.loginuser,name='login'),
    path('com/',views.com,name='community'),
]