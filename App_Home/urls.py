from django.urls import path
from . import views 

app_name="App_Home"

urlpatterns = [
    path('',views.index,name='index'),
    path('details/<pk>',views.details,name='details'),
    path('books',views.Books,name='books'),
]