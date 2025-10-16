from django.contrib import admin

# Register your models here.
from .models import Clientes, Productos

admin.site.register(Clientes)
admin.site.register(Productos)  
# Ahora puedes gestionar Clientes y Productos desde el admin de Django

class detalleInline(admin.TabularInline):
    # crear el model
    model = detalleVenta # Modelo relacionado
    extra = 1  # Número de formularios adicionales para agregar nuevos productos

@admin.register(venta)

class ventaAdmin(admin.ModelAdmin):
    
    inlines = [detalleInline]  # Incluir el inline para detalles de venta

    list_display = ('id', 'cliente', 'fecha', 'total')  # Campos a mostrar en la lista de ventas