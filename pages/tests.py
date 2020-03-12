from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView, EventPageView, PastPageView, ReviewsPageView, DrinkPageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Главная')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'О нас')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )


class EventPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('event')
        self.response = self.client.get(url)

    def test_eventpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_eventpage_template(self):
        self.assertTemplateUsed(self.response, 'event.html')

    def test_eventpage_contains_correct_html(self):
        self.assertContains(self.response, 'О нас')

    def test_eventpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_eventpage_url_resolves_eventpageview(self):
        view = resolve('/event/')
        self.assertEqual(
            view.func.__name__,
            EventPageView.as_view().__name__
        )


class PastPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('past')
        self.response = self.client.get(url)

    def test_pastpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_pastpage_template(self):
        self.assertTemplateUsed(self.response, 'past.html')

    def test_pastpage_contains_correct_html(self):
        self.assertContains(self.response, 'О нас')

    def test_pastpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_pastpage_url_resolves_pastpageview(self):
        view = resolve('/past/')
        self.assertEqual(
            view.func.__name__,
            PastPageView.as_view().__name__
        )


class ReviewsPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('reviews')
        self.response = self.client.get(url)

    def test_reviewspage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_reviewspage_template(self):
        self.assertTemplateUsed(self.response, 'reviews.html')

    def test_reviewspage_contains_correct_html(self):
        self.assertContains(self.response, 'О нас')

    def test_reviewspage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_reviewspage_url_resolves_reviewspageview(self):
        view = resolve('/reviews/')
        self.assertEqual(
            view.func.__name__,
            ReviewsPageView.as_view().__name__
        )



class DrinkPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('drink')
        self.response = self.client.get(url)

    def test_drinkpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_drinkpage_template(self):
        self.assertTemplateUsed(self.response, 'drink.html')

    def test_drinkpage_contains_correct_html(self):
        self.assertContains(self.response, 'О нас')

    def test_drinkpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

    def test_drinkpage_url_resolves_drinkpageview(self):
        view = resolve('/drink/')
        self.assertEqual(
            view.func.__name__,
            DrinkPageView.as_view().__name__
        )