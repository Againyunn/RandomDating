from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    if request.method=="POST":
        pw = request.POST.get('password', '')
        print(pw)
        res = render(request, "signup.html")
        res.set_cookie('pw', make_password(pw))
        return res

    return render(request, "signup.html")
