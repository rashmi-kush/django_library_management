    
from django.urls import path,include
from login import views
urlpatterns = [
    path('',views.loginview),
    path('logout/',views.logoutview ,name='logout'),
    path('operation/',views.operation,name='operation'),
    path('signin/',views.loginview,name='signin')
    ]
  
    
