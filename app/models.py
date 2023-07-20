from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=140, verbose_name='Имя')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    text = models.CharField(max_length=140)
    payment = models.IntegerField(null=True)

    def __str__(self):
        return self.name