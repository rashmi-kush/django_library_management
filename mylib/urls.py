
from django.urls import path,include
from mylib import views
urlpatterns = [
    path('',views.showwelcomepage),
    path('books/',views.showbooks,name='booklist'),
    path('signup/',include('register.urls'))]
    
