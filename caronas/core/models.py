from django.db import models


class Passengers(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.CharField('Endereço', max_length=250, blank=True, null=True)
    phone = models.BigIntegerField('Telefone')
    photo = models.ImageField('Foto', upload_to='passengers_photo', blank=True, null=True)
    evaluation = models.BooleanField('Avaliação', blank=True, null=True, default=True)
    obs = models.CharField('Observações', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Passageiro'
        verbose_name_plural = 'Passageiros'
        ordering = ['name']
