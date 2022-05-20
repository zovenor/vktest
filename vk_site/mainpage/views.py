from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import ListOfUsersModel
import pickle
from django.conf import settings


def mainpage(request):
    data_url = str(f'{settings.BASE_DIR}/data.pickle')
    if request.user.is_authenticated:
        if request.method == 'POST':
            link = request.POST['link']
            ListOfUsersModel.objects.create(user=request.user, link=link)
            return redirect('/')
        lst = ListOfUsersModel.objects.filter(user=request.user)
        fileData = pickle.load(open(data_url, 'rb'))
        statuses = [[fileData[el][::-1], lst.get(id=int(el)).link] for el in fileData if int(el) in [el.id for el in lst]]
        print(statuses)
        data = {
            'list': lst,
            'statuses': statuses,
        }
        return render(request, 'mainpage/list.html', data)
    else:
        return render(request, 'mainpage/index.html')


class Register(View):
    def get(self, request):
        return render(request, 'mainpage/register.html')

    def post(self, request):
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=name, password=password1)
            login(request, user)
        return redirect('/')


def logOut(request):
    logout(request)
    return redirect('/')


class Login(View):
    def get(self, request):
        return render(request, 'mainpage/login.html')

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
        else:
            redirect('/login/')
        return redirect('/')
