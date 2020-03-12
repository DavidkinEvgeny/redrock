from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class EventPageView(TemplateView):
    template_name = 'event.html'


class PastPageView(TemplateView):
    template_name = 'past.html'


class ReviewsPageView(TemplateView):
    template_name = 'reviews.html'


class DrinkPageView(TemplateView):
    template_name = 'drink.html'