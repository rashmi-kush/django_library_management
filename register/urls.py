
from django.urls import path,include
from register import views
urlpatterns = [
    path('register/',views.regview,name='signup'),
    path('signin/',include('login.urls'))
    ]
    
