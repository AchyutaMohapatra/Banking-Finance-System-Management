from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


User = settings.AUTH_USER_MODEL


class Diposit(models.Model):
    user = models.ForeignKey(
        User,
        related_name='deposits',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Withdrawal(models.Model):
    user = models.ForeignKey(
        User,
        related_name='withdrawals',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('10.00'))
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Interest(models.Model):
    user = models.ForeignKey(
        User,
        related_name='interests',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Contact(models.Model):
    name = models.TextField(max_length=50)
    phone = models.BigIntegerField()
    subject = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=50)
    class Meta:
       db_table = 'contact'
class Loan(models.Model):
    city = models.TextField(max_length=50)
    pan = models.TextField(max_length=50)
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    loan = models.TextField(max_length=50)
    loanamount = models.IntegerField()
    loanlength = models.TextField(max_length=50)
    class Meta:
       db_table = 'loan'

