from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('write_blog_post',views.write_blog_post,name="write_blog_post"),
    path('text_to_code',views.text_to_code,name="text_to_code"),
    path('explain_code',views.explain_code,name="explain_code")
]
