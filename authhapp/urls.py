from django.urls import path
from authhapp import views as v


urlpatterns = [
    path('signup/', v.signup, name='signup'),
    path('login/', v.handlelogin, name='handlelogin'),
    path('logout/', v.handlelogout, name='handlelogout')
]