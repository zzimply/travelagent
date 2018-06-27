from django.urls import path

from . import views

urlpatterns = [
    path('countriesform/', views.countries_form, name='countries_form'),
    path('countriesview/', views.countries_view, name='countries_view'),
    path('', views.guide_view, name='guide_view'),
]