from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'a.html')

def worksheet(request):
    return render(request,  'worksheet.html')

def test(request):
    return HttpResponse( "<h1>안녕</hl>")

def signup(request):
    if req.method == 'POST' :
        print(req.POST['username'])
        #username == exit
        #h2로 나가기를 출력
        if username == 'exit' :
            return Httpresponse('나가기')
        elif username =='codingon' :
            return render(req, 'login.html')

        return HttpResponse("<h2>"+username+"</h2>")
    return render(req, 'worksheet.html')
