import datetime 
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone

from .models import Party, Album


class HomePageView(ListView):
    model = Party
    template_name = 'home.html'

    def get_queryset(self):
        return Party.objects.all().order_by('-event_date')

class AboutPageView(TemplateView):
    template_name = 'about.html'


class EventPageView(ListView):
    model = Party
    template_name = 'event.html'
    def get_queryset(self):
        return Party.objects.filter(event_date__lte=datetime.date.today()).order_by('-event_date')


class PartyDetailViews(DetailView):
    model = Party
    template_name = 'detail.html'

    def get_queryset(self):
        return Party.objects.all()
    

class PastPageView(ListView):
    model = Party
    template_name = 'past.html'
    def get_queryset(self):
        return Party.objects.filter(event_date__gt=datetime.date.today()).order_by('-event_date')


class ReviewsPageView(TemplateView):
    template_name = 'reviews.html'


class DrinkPageView(TemplateView):
    template_name = 'drink.html'


