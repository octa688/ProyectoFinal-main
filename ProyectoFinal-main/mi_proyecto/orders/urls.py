from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.index, name="index2"),
    path("close_caja", views.closecaja, name="close_caja"),
    path("err_open_caja", views.erropencaja, name="err_open_caja"),
    path("err_monto_total", views.errmontototal, name="err_monto_total"),
    path("aperturadecaja", views.aperturadecaja, name="aperturadecaja"),
    path("prov_servicios", views.provservicios, name="prov_servicios"),
    path("cierredecaja", views.cierredecaja, name="cierredecaja"),
    path("pagoimpuestos", views.pagoimpuestos, name="pagoimpuestos"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("cart", views.cart_view, name="cart"),
    path("order", views.order_view, name="order"),
    path("guardar_dato", views.guardar_dato, name="pagina_exitosa"),
    path("guardar_servicio", views.guardar_servicio, name="pagina_exitosa_servicio"),
    path("editar_servicio/<int:pk>/", views.editar_servicio, name="pagina_exitosa_editar_servicio"),
    path("eliminar_servicio/<int:pk>/", views.eliminar_servicio, name="pagina_exitosa_eliminar_servicio"),
    path("guardar_pago_impuesto", views.guardar_pago_impuesto, name="pagina_exitosa_pagoimpuesto"),
    path("guardar_dato_cierracaja", views.guardar_dato_cierrecaja, name="pagina_exitosa_cierrecaja"),
    path("topping/<int:cart_id>/", views.topping_view, name="topping"),
    path("removefromcart/<int:cart_id>/", views.removefromcart_view, name="removefromcart"),
    ]
