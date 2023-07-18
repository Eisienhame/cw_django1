# Generated by Django 4.2.3 on 2023-07-14 12:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=150, verbose_name='Тема')),
                ('content', models.TextField(max_length=5000, verbose_name='Тело сообщения')),
            ],
            options={
                'verbose_name': 'сообщение рассылки',
                'verbose_name_plural': 'сообщения рассылки',
                'ordering': ('mailing',),
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('send_time', models.TimeField(default=datetime.datetime.now, verbose_name='Время рассылки')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Дата начала')),
                ('end_date', models.DateField(default=datetime.date.today, verbose_name='Дата окончания')),
                ('periodicity', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=50, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('CREATED', 'Создана'), ('LAUNCHED', 'Запущена'), ('COMPLETED', 'Завершена')], default='CREATED', max_length=50, verbose_name='Статус')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('mailings', models.ManyToManyField(to='main.mailing')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('email',),
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateTimeField(blank=True, null=True, verbose_name='Дата последней попытки')),
                ('status', models.CharField(choices=[('delivered', 'доставлено'), ('not_delivered', 'не доставлено')], default='not_delivered', max_length=50, verbose_name='статус')),
                ('server_code', models.IntegerField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mailing', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'попытка рассылки',
                'verbose_name_plural': 'попытки рассылки',
                'ordering': ('mailing',),
            },
        ),
    ]