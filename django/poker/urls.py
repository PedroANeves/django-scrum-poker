from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('table/<str:table_name>', views.table),
]
