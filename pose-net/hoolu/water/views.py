#coding:utf-8
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Permission
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="email:", max_length=100)
    pwd = forms.CharField(label="password:", widget=forms.PasswordInput)


# from django.contrib.auth.models import User

# Create your views here.
def index(request, a):
    # users = User.objects.all()
    # for user in users:
    #    print(user.userprofile.desc)
    # return HttpResponse(users)
    # print(isinstance(request, HttpRequest))
    # print(isinstance(request,HttpResponse))
    user_list = User.objects.all()
    # response = HttpResponse("Here is the text of WebPage ..")
    # return response
    return render(request, 'index.html', {'user_list': user_list})


def test(request):
    return render(request, 'index.html')


def test2(request):
    # print(request.REQUEST.get('key'))
    # user_list = User.objects.all()
    # return render(request, 'index.html', {'user_list': user_list})
    t = loader.get_template('index.html')
    user_list = User.objects.all()
    # print(user_list.query)
    c = {'user_list': user_list}
    # return HttpResponse(t.render(c, request), content_type="text/html")
    # print(locals())
    return render_to_response('index.html', locals())


def test3(request, id, key):
    print(id)
    return render(request, 'index.html')


def test5(request):
    str_string = '123'
    # 远程服务器字典

    import redis
    




    return HttpResponse(str_string)


def login(request):
    if ('email' or 'pwd') not in request.GET:
        lf = LoginForm()
        return render_to_response('login.html', {'lf': lf})
    lf = LoginForm(request.GET)
    email = lf.data['email']
    pwd = lf.data['pwd']
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        pass

    try:
        if user.check_password(pwd):
            if user.has_perm("water.can_see"):
                return HttpResponse("you can delete news")
            return HttpResponse("you can not delete news")
            # return HttpResponse("login in:" + user.email)
    except:
        pass
    return HttpResponseRedirect("/water/login/")


def register(request):
    import uuid
    if ('email' or 'pwd') not in request.GET:
        lf = LoginForm()
        return render_to_response('register.html', {'lf': lf})
    lf = LoginForm(request.GET)
    email = lf.data['email']
    pwd = lf.data['pwd']
    user = User()
    user.username = uuid.uuid1()
    user.email = email
    user.set_password(pwd)
    user.desc = 'lazy'
    user.save()

    user.user_permissions = [Permission.objects.get(codename='can_add'),
                             Permission.objects.get(codename='can_view')]
    user.save()
    return HttpResponseRedirect('/water/login')
    pass
