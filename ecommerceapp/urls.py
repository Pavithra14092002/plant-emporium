from django.urls import path
from ecommerceapp import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('contact', v.contact, name='contact'),
    path('about',v.about,name="about"),
    path('profile',v.profile,name="profile"),
    path("checkout/", v.checkout, name="Checkout"),
    # path('handlerequest/', v.handlerequest, name="HandleRequest")
    
    
    
]