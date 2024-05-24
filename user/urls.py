from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('',views.home,name='home'),
    path('search_results/', views.search, name='result'),
    path('logout/',views.logoutuser,name='logout'),
    path('login/',views.loginuser,name='login'),
 
]