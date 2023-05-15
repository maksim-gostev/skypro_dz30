from django.db import models

from ads.models import Ad
from users.models import User


class Selection(models.Model):
    name = models.CharField(max_length=200)
    ads = models.ManyToManyField(Ad, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'