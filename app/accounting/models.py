from datetime import datetime

from django.db import models


# Create your models here.

class Product(models.Model):
    article = models.CharField(verbose_name="Артикул", max_length=12, unique=True)


class Storage(models.Model):
    sku = models.ForeignKey(Product, verbose_name="Вопрос", blank=False, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name="Количество товара")
    actual_date = models.DateTimeField(verbose_name="Дата/время последней синхронизации",
                                       default=datetime(year=2022, month=12, day=13, hour=19, minute=00, second=00),
                                       blank=False, null=False)
