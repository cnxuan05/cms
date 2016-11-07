from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request,a):
    user_list = User.objects.all()
    return render(request, 'index.html', {'user_list': user_list})


def test(request):
    return render(request,'index.html')