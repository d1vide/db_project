from django import forms
from .models import *


class Necessary_componentForm(forms.ModelForm):
    class Meta:
        model = Necessary_component
        fields = '__all__'


class InvoiceForm(forms.Form):
    amount = forms.IntegerField(required=False, label='Количество')
    necessary_component = forms.CharField(required=False, label='Необходимый компонент')
    stock = forms.CharField(required=False, label='Склад')
    service_center = forms.CharField(required=False, label='Сервисный центр')


class SupplyerForm(forms.Form):
    name = forms.CharField(required=False, label='Поставщик')
    invoice = forms.IntegerField(required=False, label='Накладная')


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        widgets = {
            'address': forms.Textarea({'cols': '30', 'rows': '2'})
        }


class Worker_stockForm(forms.Form):
    name = forms.CharField(required=False, label='Имя')
    surname = forms.CharField(required=False, label='Фамилия')
    stock = forms.CharField(required=False, label='Адрес склада')


class ComponentForm(forms.Form):
    stock = forms.CharField(required=False, label='Склад')
    amount = forms.IntegerField(required=False, label='Количество')
    component = forms.CharField(required=False, label='Компонент')
