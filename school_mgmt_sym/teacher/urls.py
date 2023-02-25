from django.urls import path
from . import views

urlpatterns =[
    path('addteacher/',views.registerteachers,name="add_teacher"),
    path('displayteacher/',views.getteachers,name="display_teacher")
]