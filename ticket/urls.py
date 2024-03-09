from django.urls import path
from . import views
# from . import views
app_name='ticket'

urlpatterns=[
    path('',views.ticket,name='home'),
    # path('logout/',views.logoutuser,name='logout'),
    # path('login/',views.loginuser,name='login'),
    # path('com/',views.com,name='community'),
]