from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    if request.method == "GET" :
        request =  render(request, "signup.html")
        res.delete_cookie('pw')
        return res


    if request.COOKIES.get('pw') is not None: #COOKIES 수정하면 안됨 -> 명령어다.
        en_pw = request.COOKIES.get('pw')
        print(en_pw)

    if request.method=="POST":
        pw = request.POST.get('password', '')
        print(pw)
        res = render(request, "signup.html")
        res.set_cookie('pw', make_password(pw))
        return res

    return render(request, "signup.html")
