from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import random


# Create your views here.
#def login(req):
    #if req.method == 'GET':
     #   return render(req, 'login.html')

    #elif req.method == 'POST':
      #  username = req.POST.get('username', None)
      #  useremail = req.POST.get('useremail', None)

       # err = {}

        #if not (useremail and username) :
         #   err['err'] = '유효성이 잘못되었습니다.'
          #  return render(req, 'login.html', err)
       # else: 
        #    member = Members.objects.get(username=username)

         #   if useremail == member.useremail :
                
          #  return HttpResponse(f'<h1>{member.useremail}</h1>')

        # username = req.POST.get('username', None)
        # email = req.POST.get('password', None)

        # err = {}
        # if not(username and email) : 
        #     err['err'] ='비밀번호 오류'
        #     return  render(req, 'login.html', err)
        # else :
            ## db read
            ## session 만들기

       # return redirect('/')

def index(req):
    lotto = []
    while len(lotto) < 6:
       lotto.append(random.randint(1,46))
       lotto = list(set(lotto))
    #print(lotto)
    return HttpResponse(f"<h1>lotto 번호 추천 { lotto }</h1>")



def gugu(request):
    num =request.GET.get('num', '')
    return HttpResponse(f'<h1> gugu : {num_gugu(num)} </h1>')

def num_gugu(num):
    str = ""
    for i in range(9):
        str += f"<br> {int(num)} X {i+1} = {int(num) * (i+1)} " 
    return str

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
