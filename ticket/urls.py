from django.urls import path
from . import views
# from . import views
app_name='ticket'

urlpatterns=[
    path('',views.bus,name='home'),
    # path('search_results/', views.search, name='result'),
    # path('logout/',views.logoutuser,name='logout'),
    # path('login/',views.loginuser,name='login'),
    # path('com/',views.com,name='community'),
]