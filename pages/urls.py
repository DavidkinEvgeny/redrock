from django.urls import path
from .views import HomePageView, AboutPageView, EventPageView, PastPageView, ReviewsPageView, DrinkPageView, PartyDetailViews


urlpatterns = [
    path('detail/<int:pk>/', PartyDetailViews.as_view(), name='detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('past/', PastPageView.as_view(), name='past'),
    path('event/', EventPageView.as_view(), name='event'),
    path('reviews/', ReviewsPageView.as_view(), name='reviews'),
    path('drink/', DrinkPageView.as_view(), name='drink'),
    path('', HomePageView.as_view(), name='home'),
]