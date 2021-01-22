from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.
def detail(request, charactor1, charactor2):
    context={"char_1" : charactor1, "char_2" : charactor2 }
    return render(request, 'novel.html', context)

def error(request):
    return HttpResponse(" '  115.85.183.207:8000/novel/캐릭터이름/캐릭터이름  ' 을 입력하세요~")


