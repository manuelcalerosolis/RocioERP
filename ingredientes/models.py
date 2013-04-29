from django.db import models

# Create your models here.

class Familia_ingrediente(models.Model):
    nombre 			= models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

# Create your models here.

class Ingrediente(models.Model):
	familia 		= models.ForeignKey(Familia_ingrediente)
	nombre 			= models.CharField(max_length=200)
	kilocalorias 	= models.PositiveIntegerField()

	def __unicode__(self):
		return self.nombre

	def __str__(self):
		return self.nombre
