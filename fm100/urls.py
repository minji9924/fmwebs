from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aboutfm100/', views.aboutfm100, name='aboutfm100'),
    path('testpage/phase1', views.testpage1, name='testpage1'),
    path('testpage/phase2', views.testpage2, name='testpage2'),
    path('testpage/phase3', views.testpage3, name='testpage3'),
    path('testpage/phase4', views.testpage4, name='testpage4'),

]