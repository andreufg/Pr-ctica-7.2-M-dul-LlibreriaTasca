from django.db import models
from django.utils import timezone

class Llibre(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    preu = models.FloatField()
    exemplars = models.IntegerField()
    data = models.DateField(default=timezone.now)
    segonama = models.BooleanField(default=False)
    estat_choices = [('bo', 'Bo'), ('regular', 'Regular'), ('dolent', 'Dolent')]
    estat = models.CharField(max_length=10, choices=estat_choices, default='bo')

    @property
    def rotura_estoc(self):
        return self.exemplars < 10

    def __str__(self):
        return self.nom

