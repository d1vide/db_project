from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from .forms import *


def index(request):
    template_name = 'tables/index.html'
    return render(request, template_name)


def invoice(request):
    template_name = 'tables/invoice.html'
    invoices = Invoice.objects.all()
    form = InvoiceForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['amount'] is None:
            invoices = Invoice.objects.filter(necessary_component__name__contains=form.cleaned_data['necessary_component'],
                                            stock__address__contains=form.cleaned_data['stock'],
                                            service_center__name__contains=form.cleaned_data['service_center'])
        else:    
            invoices = Invoice.objects.filter(necessary_component__name__contains=form.cleaned_data['necessary_component'],
                                            amount__gte=form.cleaned_data['amount'],
                                            stock__address__contains=form.cleaned_data['stock'],
                                            service_center__name__contains=form.cleaned_data['service_center'])
    table = InvoiceTable(invoices)
    RequestConfig(request).configure(table)
    context = {'invoice_list': invoices, 'table': table, 'form': form}
    return render(request, template_name, context)


def necessary_component(request):
    template_name = 'tables/necessary_component.html'
    comps = Necessary_component.objects.all()
    form = Necessary_componentForm(request.GET or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        comps = Necessary_component.objects.filter(name__contains=name)
    table = NecessaryTable(comps)
    RequestConfig(request).configure(table)
    context = {'comps_list': comps, 'table': table, 'form': form}
    return render(request, template_name, context)


def supplyer(request):
    template_name = 'tables/supplyer.html'
    supplyers = Supplyer.objects.all()
    form = SupplyerForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['invoice'] is None:
            supplyers = Supplyer.objects.filter(name__contains=form.cleaned_data['name'])
        else:
            supplyers = Supplyer.objects.filter(name__contains=form.cleaned_data['name'],
                                                invoice__id__contains=form.cleaned_data['invoice'])
    table = SupplyerTable(supplyers)
    RequestConfig(request).configure(table)
    context = {'supp_list': supplyers, 'table': table, 'form': form}
    return render(request, template_name, context)


def stock(request):
    template_name = 'tables/stock.html'
    stocks = Stock.objects.all()
    form = StockForm(request.GET or None)
    if form.is_valid():
        stocks = Stock.objects.filter(address__contains=form.cleaned_data['address'])
    table = StockTable(stocks)
    RequestConfig(request).configure(table)
    context = {'stock_list': stocks, 'table': table, 'form': form}
    return render(request, template_name, context)


def worker(request):
    template_name = 'tables/worker.html'
    workers = Worker_stock.objects.all()
    form = Worker_stockForm(request.GET or None)
    if form.is_valid():
        workers = Worker_stock.objects.filter(name__contains=form.cleaned_data['name'],
                                              surname__contains=form.cleaned_data['surname'],
                                              stock__address__contains=form.cleaned_data['stock'])
    table = WorkerTable(workers)
    RequestConfig(request).configure(table)
    context = {'worker_list': workers, 'table': table, 'form': form}
    return render(request, template_name, context)


def components(request):
    template_name = 'tables/components.html'
    comps = Stock_component.objects.all()
    form = ComponentForm(request.GET or None)
    if form.is_valid():
        if form.cleaned_data['amount'] is None:
            comps = Stock_component.objects.filter(stock__address__contains=form.cleaned_data['stock'],
                                                   component__name__contains=form.cleaned_data['component'])
        else:
            comps = Stock_component.objects.filter(stock__address__contains=form.cleaned_data['stock'],
                                                   component__name__contains=form.cleaned_data['component'],
                                                   amount__gte=form.cleaned_data['amount'])
    table = ComponentsTable(comps)
    RequestConfig(request).configure(table)
    context = {'comps_list': comps, 'table': table, 'form': form}
    return render(request, template_name, context)