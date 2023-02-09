from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aboutfm100/', views.aboutfm100, name='aboutfm100'),
    path('testpage/', views.testpage, name='testpage'),
    path('login/', views.loginpage, name='login'),
]