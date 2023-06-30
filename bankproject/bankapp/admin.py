from django.contrib import admin
from .models import AccountDetailModel,CustomerModel

# Register your models here.
admin.site.register(AccountDetailModel)
admin.site.register(CustomerModel)