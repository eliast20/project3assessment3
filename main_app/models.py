from django.db import models
from django.urls import reverse

class WishItem(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('wish_detail', kwargs={'pk': self.pk})
