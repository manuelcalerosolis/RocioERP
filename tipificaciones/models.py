from django.db import models

TIPOS = ( 
	( 'TP', 'Tipo de plato' ),
	( 'CD', 'Cocinado'),
	( 'PB', 'Publicación'),
)

# Create your models here.
class Tipificacion(models.Model):
    tipo 		= models.CharField(max_length=2, choices=TIPOS)
    nombre 		= models.CharField(max_length=200)

    def __str__(self):
    	return self.nombre
