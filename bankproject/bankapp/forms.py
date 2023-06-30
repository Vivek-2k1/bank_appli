from django import forms
from .models import AccountDetailModel,CustomerModel

class AccountDetailForm(forms.ModelForm):
    class Meta:
        model = AccountDetailModel
        fields = "__all__"
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"