from datetime import datetime, date

from django.db import models

import users.models

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    # Сообщение в рассылке
    theme = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField(max_length=5000, verbose_name='Тело сообщения')

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'сообщение рассылки'
        verbose_name_plural = 'сообщения рассылки'
        ordering = ('mailing',)

class Client(models.Model):
    # Клиенты для рассылки
    email = models.EmailField(unique=True, verbose_name='почта')
    author = models.ForeignKey(users.models.User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email',)



class Mailing(models.Model):

    FREQUENCY_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]

    STATUS_CHOICES = [
        ('CREATED', 'Создана'),
        ('LAUNCHED', 'Запущена'),
        ('COMPLETED', 'Завершена')

    ]

    # Рассылка
    name = models.CharField(max_length=150, verbose_name='Название')
    send_time = models.TimeField(default=datetime.now, verbose_name='Время рассылки')
    start_date = models.DateField(default=date.today, verbose_name='Дата начала')
    end_date = models.DateField(default=date.today, verbose_name='Дата окончания')
    periodicity = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='CREATED', verbose_name='Статус')
    author = models.ForeignKey(users.models.User, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    message = models.ForeignKey(Message, verbose_name='сообщение', on_delete=models.CASCADE, **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name='клиенты', **NULLABLE)
    last_run = models.DateField(verbose_name='дата последней отправки рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('name',)
        permissions = [
            ('deactivate_mailing',
             'Deactivate_mailing',)
        ]




class Attempt(models.Model):
    DELIVERED = 'delivered'
    NOT_DELIVERED = 'not_delivered'

    STATUS = (
        (DELIVERED, 'доставлено'),
        (NOT_DELIVERED, 'не доставлено'),
    )

    # Попытка рассылки
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    last_attempt = models.DateTimeField(verbose_name='Дата последней попытки', **NULLABLE)
    status = models.CharField(max_length=50, choices=STATUS, default=NOT_DELIVERED, verbose_name='статус')
    server_code = models.CharField(max_length=50, verbose_name='Ответ сервера', **NULLABLE)

    def __str__(self):
        return f'{self.mailing}'

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
        ordering = ('mailing',)