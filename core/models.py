from django.db import models


# Create your models here.
class Submit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateTimeField(verbose_name='Дата и время сабмита', auto_now_add=True)


class Picture(models.Model):
    submit = models.ForeignKey(Submit, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=255)
    picture = models.ImageField(verbose_name='Изоражение')
    date_uploaded = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')