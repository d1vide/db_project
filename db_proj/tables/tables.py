import django_tables2 as tables
from .models import *


class InvoiceTable(tables.Table):
    class Meta:
        model = Invoice
        attrs = {'class': 'table table-bordered table-striped table-condensed'}


class NecessaryTable(tables.Table):
    class Meta:
        model = Necessary_component
        attrs = {'class': 'table table-bordered table-striped table-condensed'}


class SupplyerTable(tables.Table):
    class Meta:
        model = Supplyer
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class StockTable(tables.Table):
    class Meta:
        model = Stock
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class WorkerTable(tables.Table):
    class Meta:
        model = Worker_stock
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class ComponentsTable(tables.Table):
    class Meta:
        model = Stock_component
        attrs = {'class': 'table table-bordered table-striped table-condensed'}