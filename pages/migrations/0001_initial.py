# Generated by Django 3.0.6 on 2020-05-10 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('event_date', models.DateField(verbose_name='дата проведения')),
                ('text_before', models.TextField(blank=True, verbose_name='Текст до проведения')),
                ('text_after', models.TextField(blank=True, verbose_name='Текст после проведения')),
                ('preview', models.ImageField(upload_to='preview/', verbose_name='превью')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='фотографии')),
                ('alt_text', models.CharField(default='RedRock', max_length=150, verbose_name='Название картинки')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Party', verbose_name='альбом')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
    ]
