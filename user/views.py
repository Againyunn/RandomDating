from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from . models import User

# Create your views here.
def detail(request, question_id):
    return HttpResponse(f"You're {question_id} looking at {question_id}")

def results(request, question_id):
    response = "You're looking at the results of question %s %s."
    return HttpResponse(response % (question_id, question_id)) # % 을 넣는다는 의미 : %s 의 변수에 ( )안의 값을 입력하라는 의미.

def calender(request):
    context={"loop_1" : range(1,32) } #dictionary로 지정하여 loop_1 과 loop_2로 넣어서 render를 통해 넘길 수 있다.
    return render(request, 'calender.html', context) # return render(request, 불러올 파일, 전송할 데이터)의 형태


def index(request):
    context={"index_1" : "코딩온" , "loop_1" : range(10) , "loop_2" : range(5, 10) } #dictionary로 지정하여 loop_1 과 loop_2로 넣어서 render를 통해 넘길 수 있다.
    return render(request, 'index.html', context) # return render(request, 불러올 파일, 전송할 데이터)의 형태

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
    
