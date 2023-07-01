from django import forms
from .models import AccountDetailModel,CustomerModel

class AccountDetailForm(forms.ModelForm):
    class Meta:
        model = AccountDetailModel
        fields = "__all__"
        
class CustomerForm(forms.ModelForm):
    accounts = forms.ModelMultipleChoiceField(queryset=AccountDetailModel.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox-inline'}))
    class Meta:
        model = CustomerModel
        fields = "__all__"