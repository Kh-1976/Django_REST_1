from django.db import models

class Car(models.Model):
    name = models.CharField(verbose_name='Нименование', max_length=254)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

