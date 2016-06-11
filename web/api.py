from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from web.models import users, banIp, signLog, script, task
import json
from django.db import IntegrityError
from ipware.ip import get_ip
import re
from django.conf import settings
from django.utils.timezone import now, make_naive
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
def login(request):
    print (request.POST)
    res = {}
    if(request.POST):
        if ('login' in request.POST and 'password' in request.POST):
            print ('check')
            loginStr = request.POST.get('login', '')
            password = request.POST.get('password','')
            if (re.findall(r'@', loginStr)):    # email login
                user = users.objects.filter(email = loginStr)
                if (user):
                    username = user[0].username
                else:
                    res = {'status': False, 'message': 'unknow email'}
                    username = ''
            else:
                username = loginStr
            print (username, password)
            if (username and password):
                ip = get_ip(request)
                if not ip:
                    ip = ''

                user = authenticate(username = username, password = password)
                if (user is not None):
                    if (user.is_active):
                        if not user.ban:
                            user.loginTimes = user.loginTimes + 1;
                            user.lastLoginIp = ip
                            user.save()
                            auth_login(request, user)
                            res = {'status' : True, 'message': 'login success'}
                            return HttpResponseRedirect('../home')
                        else:
                            res = {'status': False, 'message': 'forbidden user'}
                    else:
                        res = {'status': False, 'message': 'not active user'}
                else:
                    res = {'status': False, 'message': 'username:password not match'}
            else:
                res = {'status': False, 'message': 'not allow data'}
        else:
            res = {'statue': False, 'message':'No need data'}
    else:
        res = {'statue': False, 'message':'No post'}
    return HttpResponse(json.dumps(res))

def regist(request):
    print (request.POST)
    res = {}
    if(request.POST):
        if ('email' in request.POST and 'username' in request.POST and 'password' in request.POST):
            print ('check')
            email = request.POST.get('email', '')
            username = request.POST.get('username', '')
            password = request.POST.get('password' , '')
            if settings.DEBUG == False:
                email = re.findall(r'^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9]+$', request.POST.get('email', ''))
                username = re.findall(r'^[A-Za-z0-9\.\-_]{4,}$', request.POST.get('username',''))
                password = re.findall(r'(?=.*((?=[\x21-\x7e]+)[^A-Za-z0-9]))^(?=.*\d)(?=.*[a-zA-Z]).{10,}', request.POST.get('password',''))

            if (email and username and password):
                if settings.DEBUG == False:
                    email = email[0]
                    username = username[0]
                    password = password[0]
                ip = get_ip(request)
                if not ip:
                    ip = ''
                if (users.objects.filter(email = email)):   # check email
                    res = {'status': False, 'message': 'email exists'}
                else:   # self check success, try to create user
                    try:
                        user = users.objects.create_user(username, email, password, registIp = ip)
                        res = {'status': True, 'message': 'Regist success'}
                        auth_login(request, user)
                        return HttpResponseRedirect('../home')
                    except IntegrityError as e:
                        res = {'status': False, 'message': 'username exists'}
                    except Exception as e:
                        if settings.DEBUG:
                            res = {'status': False, 'message': str(e)}
                        else:
                            res = {'status': False, 'message': 'not know error'}
            else:
                res = {'status': False, 'message': 'not allow data, not allow data, may be format check failed'}
        else:
            res = {'status': False, 'message': 'No need data'}
    else:
        res = {'statue': False, 'message':'No post'}
    return HttpResponse(json.dumps(res))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('../index')

def submit(request):
    print (request.POST)
    if request.user.is_authenticated():
        name = request.POST.get('name', '')
        target = request.POST.get('target', '')
        intro = request.POST.get('intro', '')
        scriptFile = request.FILES['scriptFile']
        if (name and target and intro and scriptFile):
            exists = script.objects.filter(name = name, target = target, author = request.user)
            if (exists):
                exists.intro = intro
                exists.FILE = scriptFile
                exists.time = make_naive(now())
                exists.save()
            else:
                newScript = script(name = name, target = target, intro = intro, FILE = scriptFile, time = make_naive(now()), author = request.user)
                newScript.save()
            res = {'status': True, 'message': 'upload success'}
        return HttpResponse('submit success' + str(make_naive(now())))
    else:
        return HttpResponseRedirect('login')
