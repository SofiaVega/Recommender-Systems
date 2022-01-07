from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about', views.about, name="about"),
    path('charts.html', views.charts, name='charts'),
    path('tables.html', views.tables, name="tables")
]
