from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('reg/', views.Register.as_view()),
    path('logout/', views.logOut),
    path('login/', views.Login.as_view())
]
