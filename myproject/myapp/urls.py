from . import views
from django.urls import path
# it will render the function that is in the views.py 
urlpatterns = [
    path('',views.index,name="index"), # index is the function name
    path('counter',views.counter,name="counter"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('post/<str:pk>',views.post,name="post")#dynamic url routing in django
]
# 