from django.db import models

class Categoria(models.Model):
    nom = models.CharField(max_length=255, help_text="Introduïx el nom de la categoria")
    descripcio = models.TextField()

    def __str__(self):
        return self.nom
