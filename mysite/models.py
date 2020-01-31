from django.db import models


class Articles(models.Model):
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')

    class Meta():
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return '%s: %s' % (self.create_date, self.name)