from django.shortcuts import render

def account_home(request):
    return render (
        request,
        "accounts/account_home.html"
    )