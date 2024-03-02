from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=64)
	custom_topping = models.BooleanField(default=False)
	custom_extra = models.BooleanField(default=False)
	custom_size = models.BooleanField(default=False)


	def __str__(self):
		return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Topping(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return f"{self.name}"

class Extra(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return f"{self.name}"
	
class Monto_Inicial(models.Model):
    montoinicial = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True) 
    fecha_cierre = models.DateTimeField(auto_now_add=True)
    caja_abierta = models.BooleanField(default=False)
    total_ingresos = models.FloatField(default=0)
    total_egresos = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.total_ingresos is None:
            self.total_ingresos = 0
        if self.total_egresos is None:
            self.total_egresos = 0

    def __str__(self):
        return f"Monto Inicial: {self.montoinicial}, Fecha de Registro: {self.fecha_registro}, Caja Abierta: {self.caja_abierta}, Total Ingresos: {self.total_ingresos}, Total Egresos: {self.total_egresos}, Total: {self.total}"

class Prov_Servicio(models.Model):
	name= models.CharField(max_length=64)
	address= models.CharField(max_length=64)
	phone= models.CharField(max_length=64)
	mail= models.CharField(max_length=64)
	type= models.CharField(max_length=64)

def __str__(self):
        return f"Nombre: {self.name}, Domicilio: {self.address}, Telefono: {self.phone}, Mail: {self.mail}, Tipo: {self.type}"


class Servicio(models.Model):
	id_caja = models.ForeignKey(Monto_Inicial, on_delete=models.CASCADE)
	id_prov_ser = models.ForeignKey(Prov_Servicio, on_delete=models.CASCADE)
	factura = models.CharField(max_length=64)
	montototal = models.FloatField()

def __str__(self):
        return f"Numero Factura: {self.factura}, Monto: {self.montototal}"


class Monto_Final(models.Model):
	montofinal = models.FloatField()
	fecha_cierre = models.DateTimeField(auto_now_add=True)
	def __str__(self):

		return f"Monto Final: {self.montofinal}, Cierre: {self.fecha_cierre}"
	
class Pago_Impuesto(models.Model):
	nameimpuesto= models.CharField(max_length=64)
	montopagar = models.FloatField()

	def __str__(self):

		return f"Impuesto: {self.nameimpuesto} ,Monto a pagar: {self.montopagar}"

		
class Price_List(models.Model):
	name = models.CharField(max_length=64)
	base_price = models.FloatField()
	large_supp = models.FloatField()

	def __str__(self):

		return f"{self.name}, Base: {self.base_price}, large_supp: {self.large_supp}"


class Item_List(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	base_price_id = models.ForeignKey(Price_List, on_delete=models.CASCADE)


	def __str__(self):
		return f" {self.name}, Base Price1: ${self.base_price_id.base_price}"
# {self.category.name}

class Cart_List(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Item_List, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True,)
	extra = models.ManyToManyField(Extra, blank=True)
	toppings = models.ManyToManyField(Topping, blank=True)
	calculated_price = models.FloatField()
	is_current = models.BooleanField(default=True)

	def __str__(self):
		topping_list = []
		for topping in self.toppings.all():
			topping_list.append(topping)
		extra_list = []
		for extra in self.extra.all():
			extra_list.append(extra)
		if self.size ==None:
			return f"{self.item_id.category.name} {self.item_id.name} - Price: ${self.calculated_price}"
		else:
			return f"{self.item_id.category.name} {self.item_id.name}, {self.size.name} { topping_list } { extra_list }- Price: ${self.calculated_price}"
	

class Order(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	cart_id = models.ManyToManyField(Cart_List)
	complete = models.BooleanField(default=False)
	
	def __str__(self):
		if self.complete == False:
			return f"{self.user_id}, Status: On Order"
		else:
			return f"{self.user_id}, Status: Complete"