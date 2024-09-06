from django.urls import path
from . import views

urlpatterns =[
path("",views.index,name="index"),
path("single/<int:object_id>/",views.single,name="single"),
path("allblogs/",views.allblogs,name="allblogs"),
path("contact/",views.contact,name="contact")
]