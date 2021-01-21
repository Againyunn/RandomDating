from django.shortcuts import render, redirect
from . models import User

# Create your views here.
def login(request):
    if request.method == "POST" :
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        data = {}
        if not (userid and password) :
            data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'login.html', data )
        
        else:
            user = User.objects.get(userid=userid)
            if user.password == password:
                return redirect('../main') 
            else:
                data['error'] = '아이디 또는 비밀번호가 틀립니다.'
                return render(request, 'login.html', data)
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST" :
        userid = request.POST.get('userid')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        data= {}
        if not (userid and username and password) :
            data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'register.html', data )
        else:
            user = User(userid=userid, username=username, password=password, gender=gender)    
            user.save()
        return redirect('../main') #주소를 어디로 이동할지 정해주는 코드
        # ../ 은 1단계 앞을 의미한다. 따라서 ../main은 한단계 앞의 main을 의미한다.
    else:
        return render(request, 'register.html')

def main(request):
    return render(request, 'main.html')

def user(request):
    user = User.objects.order_by('registered')
    return render(request, 'user.html', {'user':user} )

def form(request):
    if request.method =="POST":
        post = request.POST
        data = {
                'first': post.get('first'),
                'second': post.get('second')
        }
        return render(request, 'receive.html' , data )
    else:
        return render(request, 'form.html')
    
