from django.contrib import admin
# from .models.productos import Producto
from .models import Cliente, Producto, Maquina, Orden, Contacto

# Register your models here.

# Admin model para cliente
class ClientesAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id_cliente','nombre','email','tel')
    search_fields = ['id_cliente', 'email']
    list_filter = ('id_cliente','email',)

class ProductosAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id_producto','nombre','cantidad','precio')
    search_fields = ['nombre', 'id_producto']
    list_filter = ('precio','id_producto')

class MaquinaAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id_maquina','id_propietario','is_activate')
    search_fields = ['id_maquina','id_propietario']
    list_filter = ('id_maquina','id_propietario')

class OrdenAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id_orden','fecha')
    search_fields = ['id_orden','fecha',]
    list_filter = ('id_orden',)

class ContactoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id_contacto','nombre','email','tel',)
    search_fields = ['id_contacto', 'email',]
    list_filter = ('id_contacto','email',)


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Maquina, MaquinaAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Contacto,ContactoAdmin)