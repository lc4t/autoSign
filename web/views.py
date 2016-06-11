from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.template import RequestContext
from django.db.models import Q
from web.models import script, task

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    return render_to_response('index.html', {'title':'auto sign index'})

def regist(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    return render_to_response('regist.html', {'title':'regist'} ,context_instance = RequestContext(request))

def login(request):
    return render_to_response('login.html', {'title':'login'} ,context_instance = RequestContext(request))

def home(request):
    if request.user.is_authenticated():
        return render_to_response('home.html', {'title':'Manager', 'index_class': 'am-active'})
    else:
        return HttpResponseRedirect('login')

def create(request):
    if request.user.is_authenticated():
        scripts = script.objects.filter(check = True).filter(Q(author = request.user.username) | Q(opened = True))
        return render_to_response('create.html', {'title':'Create new task', 'create_class': 'am-active', 'scripts': scripts} ,context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('login')

def createID(request, scriptID):
    if request.user.is_authenticated():
        return render_to_response('createID.html', {'title':'Create new task'} ,context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('login')

def submit(request):
    if request.user.is_authenticated():
        return render_to_response('submit.html', {'title':'Create new script', 'submit_class': 'am-active'} ,context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('login')
