from django.urls import path
from .views import HomePageView, AboutPageView, HelpPageView, pravodkaView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('help/', HelpPageView.as_view(), name='help'),
    path('pravodka/', pravodkaView, name='pravodka'),
]
