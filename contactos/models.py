from django.db      import models

TIPOS = ( 
	( 'sugerencia', 'Sugerencias' ),
	( 'error', 'Errores'),
	( 'contacto', 'Contacto'),
)

# Create your models here.

class Contacto(models.Model):
    tipo 		= models.CharField(max_length=10, choices=TIPOS)
    texto 		= models.CharField(max_length=200)
    mail		= models.EmailField()

    def __unicode__(self):
        return self.texto

    def __str__(self):
        return self.texto

