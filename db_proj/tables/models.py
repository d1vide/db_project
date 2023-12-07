from django.db import models


class Necessary_component(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название',
                            blank=True)

    class Meta:
        verbose_name = 'нужный компонент'
        verbose_name_plural = 'Нужные компоненты'

    def __str__(self):
        return self.name


class Stock(models.Model):
    address = models.TextField(verbose_name='Адрес', blank=True)

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.address


class Component(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название')
    stocks = models.ManyToManyField(Stock,
                                    through='Stock_component',
                                    verbose_name='Склады')

    class Meta:
        verbose_name = 'компонент'
        verbose_name_plural = 'Компоненты'

    def __str__(self):
        return self.name


class Stock_component(models.Model):
    stock = models.ForeignKey(Stock,
                              on_delete=models.CASCADE,
                              verbose_name='Склад')
    component = models.ForeignKey(Component,
                                  on_delete=models.CASCADE,
                                  verbose_name='Компонент')
    amount = models.IntegerField(default=0,
                                 verbose_name='Количество')

    class Meta:
        verbose_name = 'склад-компонент'
        verbose_name_plural = 'Склад-компоненты'

    def __str__(self):
        return f'{self.component} {self.stock}'


class Worker_stock(models.Model):
    name = models.CharField(max_length=64, 
                            verbose_name='Имя')
    surname = models.CharField(max_length=64,
                               verbose_name='Фамилия')
    stock = models.ForeignKey(Stock,
                              on_delete=models.CASCADE,
                              verbose_name='Склад')

    class Meta:
        verbose_name = 'работник склада'
        verbose_name_plural = 'Работники складов'

    def __str__(self):
        return self.surname


class Service_center(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название')
    address = models.TextField(verbose_name='Адрес')
    phone = models.IntegerField(verbose_name='Телефон')

    class Meta:
        verbose_name = 'сервисный центр'
        verbose_name_plural = 'Сервисные центры'

    def __str__(self):
        return self.name


class Invoice(models.Model):
    necessary_component = models.ForeignKey(Necessary_component,
                                            on_delete=models.CASCADE,
                                            verbose_name='Необходимый компонент')
    amount = models.IntegerField(verbose_name='Кол-во')
    stock = models.ForeignKey(Stock,
                              on_delete=models.CASCADE,
                              verbose_name='Склады')
    service_center = models.ForeignKey(Service_center,
                                       on_delete=models.CASCADE,
                                       verbose_name='Сервисные центры')

    class Meta:
        verbose_name = 'накладная'
        verbose_name_plural = 'Накладные'

    def __str__(self):
        return f'Накладная {self.pk}'


class Supplyer(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название')
    invoice = models.ForeignKey(Invoice,
                                on_delete=models.CASCADE,
                                verbose_name='Накладная')

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
    

