from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер', related_name='profile')
    patronymic = models.CharField('Отчество', max_length=100)
    phone = models.CharField('Номер телефона', max_length=100)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.patronymic}"


class RequestType(models.Model):
    name = models.CharField('Название услуги', max_length=100)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField('Тип оплаты')

    def __str__(self):
        return self.name


class RequestStatus(models.Model):
    name = models.CharField('Статус')

    def __str__(self):
        return self.name


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Юзер')
    address = models.CharField('Адрес', max_length=100)
    date = models.DateTimeField('Дата', max_length=100)
    phone = models.CharField('Контактный номер телефона', max_length=100)
    type = models.ForeignKey(RequestType, verbose_name='Тип услуги', on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, verbose_name='Тип оплаты', on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, verbose_name='Статус', on_delete=models.CASCADE, default=1)
    is_other = models.BooleanField('Другая услуга')
    description = models.CharField('Описание услуги', blank=True, null=True)
    reject_message = models.CharField('Причина отмены', default='', blank=True, null=True)

    def __str__(self):
        return f"От {self.user.last_name} {self.user.first_name}, ${self.type.name} на {self.date}"
