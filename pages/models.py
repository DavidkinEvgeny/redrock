import datetime
from django.db import models
from datetime import date
from django.utils import timezone


class Party(models.Model):
    """Модель мероприятие."""
    title = models.CharField(max_length=150, verbose_name="заголовок")
    event_date = models.DateField(verbose_name="дата проведения")
    text_before = models.TextField(verbose_name="Текст до проведения", blank=True)
    text_after = models.TextField(verbose_name="Текст после проведения", blank=True)
    preview = models.ImageField(upload_to="preview/", verbose_name="превью")
    
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title

    def was_published(self):
        now = datetime.date.today()
        if self.event_date <= now:
            pub_day = 'event_day'
        else:
            pub_day = 'past_day'
        return pub_day


class Album(models.Model):
    """Модель Альбом."""
    photo = models.ImageField(upload_to="photo/", verbose_name="фотографии", null=True, blank=True)
    alt_text = models.CharField(max_length=150, verbose_name="Название картинки", default="RedRock")
    party = models.ForeignKey(Party, verbose_name="альбом", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.alt_text


