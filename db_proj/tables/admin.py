from django.contrib import admin
from .models import *


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('necessary_component',
                    'amount',
                    'stock',
                    'service_center',)
    search_fields = ('necessary_component__name', 'stock__address')


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Necessary_component)
admin.site.register(Supplyer)
admin.site.register(Service_center)
admin.site.register(Stock)
admin.site.register(Worker_stock)
admin.site.register(Stock_component)
admin.site.register(Component)