from django.db import models
import uuid
# Create your models here.

class Solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_carga = models.DateField(auto_now=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tipo, self.descripcion)