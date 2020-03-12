from django.urls import path
from .views import HomePageView, AboutPageView, EventPageView, PastPageView, ReviewsPageView, DrinkPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('event/', EventPageView.as_view(), name='event'),
    path('past/', PastPageView.as_view(), name='past'),
    path('reviews/', ReviewsPageView.as_view(), name='reviews'),
    path('drink/', DrinkPageView.as_view(), name='drink'),
    path('', HomePageView.as_view(), name='home'),
]