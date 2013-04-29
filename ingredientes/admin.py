from django.contrib import admin

# Register your models here.

from ingredientes.models import Familia_ingrediente
from ingredientes.models import Ingrediente

admin.site.register(Familia_ingrediente) 
admin.site.register(Ingrediente)

