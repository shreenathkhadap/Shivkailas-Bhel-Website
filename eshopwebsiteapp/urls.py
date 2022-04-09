
from django.urls import path

from django.urls.conf import include 
from eshopwebsiteapp import views 
urlpatterns = [
   path('' , views.index , name="index" ),
   path('contact/' , views.contact , name="contact"),
   path('about/' , views.about , name="about"),
   path('products/' , views.products , name="products"),
   path('services/' , views.services , name="services"),
   path('postcontact/' , views.postcontact , name="postcontact"),
   # path('test/' , views.test , name="test"),
   path('about/' , views.about , name="about"),

]
