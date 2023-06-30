from django.shortcuts import render
from .models import AccountDetailModel,CustomerModel
from .forms import AccountDetailForm,CustomerForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = AccountDetailForm(request.POST)
        if data.is_valid():
            account_number = data.cleaned_data['account_number']
            if len(str(account_number)) != 12:
                msg = "Invalid account number. The account number must be exactly 12 digits."
                fm = AccountDetailForm()
                return render(request,'home.html',{"fm":fm,"msg":msg})
            
            try:
                account = AccountDetailModel.objects.get(account_number=account_number)
                account.balance = data.cleaned_data['balance']
                account.account_type = data.cleaned_data['account_type']
                account.save()
                msg = "Account updated successfully."
            except AccountDetailModel.DoesNotExist:
                account = data.save()
                msg = "Account created successfully."
            fm = AccountDetailForm()
            return render(request, 'home.html', {"fm": fm, "msg": msg})
        else:
            msg = data
            return render(request,'home.html',{"msg":msg})
    else:
        fm = AccountDetailForm()
        return render(request,'home.html',{"fm":fm})
    
def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'customer.html')
    else:
        form = CustomerForm()

    account_type = request.GET.get('account_type')
    account_number = request.GET.get('account_number')

    customers = CustomerModel.objects.all().prefetch_related('accounts')

    if account_type:
        customers = customers.filter(accounts__account_type=account_type)
    if account_number:
        customers = customers.filter(accounts__account_number__icontains=account_number)

    context = {
        'form': form,
        'customers': customers,
    }
    return render(request, 'customer.html', context)