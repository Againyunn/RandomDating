from django.shortcuts import render , redirect 
from django.http.response import HttpResponse
from . models import Project
import random

# Create your views here.

def workers(request):
    context={"loop_1" : range(1,32) } #dictionary로 지정하여 loop_1 과 loop_2로 넣어서 render를 통해 넘길 수 있다.
    return render(request, 'Calender.html', context) 

def randomSearch(request) :
    return render(request,'random.html' )

def certification(request) :
    return render(request, 'certification.html')

def result(request) :
        dateList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
        data = random.choice(dateList)
    
    #return render(request,'randomtest.html',data)
    #HttpResponse(f"{data} ")
    
        if data == 0 :
            return render(request,'보드게임.html')
        if data == 1 :
            return render(request,'방탈출.html')
        if data == 2 :
            return render(request,'고궁방문.html')
        if data == 3 :
            return render(request,'산책.html')
        if data == 4 :
            return render(request,'자전거타기.html')
        if data == 5 :
            return render(request,'드라이브.html')
        if data == 6 :
            return render(request,'등산.html')
        if data == 7 :
            return render(request,'전시회.html')
        if data == 8 :
            return render(request,'파티룸.html')
        if data == 9 :
            return render(request,'룸카페멀티방.html')
        if data == 10 :
            return render(request,'오락실.html')
        if data == 11 :
            return render(request,'노래방.html')
        if data == 12 :
            return render(request,'영화관람.html')
        if data == 13 :
            return render(request,'놀이공원.html')
        if data == 14 :
            return render(request,'아쿠아리움.html')
        if data == 15 :
            return render(request,'쇼핑.html')
        if data == 16 :
            return render(request,'만화카페.html')
        if data == 17 :
            return render(request,'공방데이트.html')
        if data == 18 :
            return render(request,'칵테일바.html')
        if data == 19 :
            return render(request,'인생네컷.html')
        if data == 20 :
            return render(request,'찜질방.html')
        if data == 21 :
            return render(request,'퍼즐맞추기.html')
        if data == 22 :
            return render(request,'그림그리기.html')
        if data == 23 :
            return render(request,'게임하기.html')
        if data == 24 :
            return render(request,'전망대관람.html')
        if data == 25 :
            return render(request,'실내낚시.html')
        if data == 26 :
            return render(request,'vr방데이트.html')
        if data == 27 :
            return render(request,'커플마사지받기.html')
        if data == 28 :
            return render(request,'커플젠가하기.html')
        if data == 29 :
            return render(request,'실내엑티비티.html')
        if data == 30 :
            return render(request,'호캉스.html')
        if data == 31 :
            return render(request,'어릴때앨범구경.html')
        if data == 32 :
            return render(request,'소원들어주기.html')
        if data == 33 :
            return render(request,'애인얼굴그려주기.html')
        if data == 34 :
            return render(request,'진실게임.html')
        if data == 35 :
            return render(request,'오늘은내가쉐프.html')
        if data == 36 :
            return render(request,'밸런스게임.html')
        if data == 37 :
            return render(request,'깜짝이벤트.html')
        if data == 38 :
            return render(request,'너의이름은.html')
        if data == 39 :
            return render(request,'왕게임.html')
        if data == 40 :
            return render(request,'커플요가.html')
