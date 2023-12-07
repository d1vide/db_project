from django.urls import path

from . import views

app_name = 'tables'

urlpatterns = [
    path('', views.index, name='index'),
    path('invoice', views.invoice, name='invoice'),
    path('necessary_component', views.necessary_component, name='nec_comp'),
    path('supplyer', views.supplyer, name='supplyer'),
    path('stock', views.stock, name='stock'),
    path('worker', views.worker, name='worker'),
    path('components', views.components, name='components'),
]
