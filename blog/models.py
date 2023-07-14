from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    img = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    views = models.IntegerField(default=0, verbose_name='кол-во просмотров')
    date = models.DateTimeField(auto_now=True, verbose_name='дата публикации')
