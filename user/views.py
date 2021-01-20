from django.shortcuts import render
from . models import User

# Create your views here.
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
    
