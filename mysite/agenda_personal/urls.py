from django.urls import path

from . import views

app_name = 'agenda_personal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('result/<int:pk>/', views.ResultView.as_view(), name='result'),
]