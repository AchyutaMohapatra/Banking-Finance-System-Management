from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import DepositForm, WithdrawalForm
from transactions.models import Contact, Loan


@login_required()
def deposit_view(request):
    form = DepositForm(request.POST or None)

    if form.is_valid():
        deposit = form.save(commit=False)
        deposit.user = request.user
        deposit.save()
        # adds users deposit to balance.
        deposit.user.account.balance += deposit.amount
        deposit.user.account.save()
        messages.success(request, 'You Have Deposited {} $.'
                         .format(deposit.amount))
        return redirect("home")

    context = {
        "title": "Deposit",
        "form": form
    }
    return render(request, "transactions/form.html", context)


@login_required()
def withdrawal_view(request):
    form = WithdrawalForm(request.POST or None, user=request.user)

    if form.is_valid():
        withdrawal = form.save(commit=False)
        withdrawal.user = request.user
        withdrawal.save()
        # subtracts users withdrawal from balance.
        withdrawal.user.account.balance -= withdrawal.amount
        withdrawal.user.account.save()

        messages.success(
            request, 'You Have Withdrawn {} $.'.format(withdrawal.amount)
        )
        return redirect("home")

    context = {
        "title": "Withdraw",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        contact = Contact(name=name, phone=phone, subject=subject, message=message, email=email)
        contact.save()
        print("Message Saved successfully!! We will contact you Soon 😊😊😊")
    return render(request, "core/contact.html")

def chatbot(request):
    return render(request, "core/chatbot.html")



def loan(request):
    if request.method == "POST":
        city = request.POST.get('city')
        pan = request.POST.get('pan')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        loan = request.POST.get('loan')
        loanamount = request.POST.get('loanamount')
        loanlength = request.POST.get('loanlength')

        ldata = Loan(city=city, pan = pan, name = name, email=email,mobile=mobile, loan = loan, loanamount=loanamount, loanlength=loanlength)
        ldata.save()
        print("Message Saved successfully")

        

    return render(request, "core/loan.html")

def atm(request):
    return render(request, "core/atm.html")


