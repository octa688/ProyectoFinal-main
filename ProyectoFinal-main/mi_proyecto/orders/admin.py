from django.contrib import admin
from .models import Monto_Final, Monto_Inicial, Pago_Impuesto, Prov_Servicio , Servicio


# Register your models here.





admin.site.register(Monto_Inicial)
admin.site.register(Monto_Final)
admin.site.register(Pago_Impuesto)
admin.site.register(Prov_Servicio)
admin.site.register(Servicio)






# class MenuPriceResource(resources.ModelResource):

#     class Meta:
#         model = MenuPrice