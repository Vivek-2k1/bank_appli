from django.db import models

# Create your models here.
class AccountDetailModel(models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    Account_Type_Choices = [
        ('Savings','Savings'),
        ('Credit','Credit')
    ]
    account_type = models.CharField(max_length=40,choices=Account_Type_Choices)

    def __str__(self):
        return str(self.account_number)

class CustomerModel(models.Model):
    accounts = models.ManyToManyField(AccountDetailModel)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=150)
    ph_num = models.IntegerField()
    email = models.EmailField()