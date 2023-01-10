from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('text',views.get_text,name="get_text")
]
