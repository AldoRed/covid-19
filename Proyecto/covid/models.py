from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField( max_length=50)
    correo = models.EmailField(max_length=254)
    numero = models.TextField()
    sintomas = models.TextField()

    def publish(self):
        self.save()