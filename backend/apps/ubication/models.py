from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField(max_length=50)

    # Importante para la visualización en el admin
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    # Establece la representación en string del objeto
    def __str__(self):
        return self.name


# Modelo para manejar los municipios
class City(models.Model):
    name = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.name
    

class Ubication(models.Model):
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name="ubication", on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    postal_code = models.IntegerField(null=True)
    notes = models.TextField(blank=True) # Extra Descriptions to the addres

    class Meta: 
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"

    def __str__(self):
        return self.address
