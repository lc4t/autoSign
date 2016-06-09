from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {'title':'auto sign index'})

def regist(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    return render_to_response('regist.html', {'title':'regist'})
    #     if form.is_valid():
    #         human = True
    #         message = 'code was true, no input'
    #         if ('username' in request.POST and 'password' in request.POST and 'email' in request.POST):
    #             username = filterUsername(request.POST.get('username',''))
    #             password = filterPassword(request.POST.get('password',''))
    #             email    = filterEmail(request.POST.get('email',''))
    #             try:
    #                 if (username and password and email):
    #                     user = User.objects.create_user(username, email, password)
    #                     messageType = 'success'
    #                     message = 'code was true,user can add'
    #                     user = authenticate(username=username, password=password)
    #                     login(request, user)
    #                     return HttpResponseRedirect('/home/')
    #                 else:
    #                     # print (username,password,email)
    #                     message = 'Please check your input,May not in permission'
    #             except:
    #                 message = 'code was true, user can not add'
    #     else:
    #         message = 'code was wrong'
    # else:
    #     form = CaptchaTestForm()
    #     messageType = 'info'
    #     message = 'No input'
    # return render_to_response('register.html', {'captcha':form, 'messageType':messageType,'message':message},context_instance=RequestContext(request))
    #


def login(request):
    return render_to_response('login.html', {'title':'login'})
#     message = None
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('/home/')
#     if request.POST:
#         form = CaptchaTestForm(request.POST)
#         if form.is_valid():
#             human = True
#             if ('username' in request.POST and 'password' in request.POST):
#                 username = filterUsername(request.POST.get('username',''))
#                 password = filterPassword(request.POST.get('password',''))
#                 user = authenticate(username=username, password=password)
#                 if user is not None:# no this user
#                     if user.is_active:
#                         login(request, user)
#                         return HttpResponseRedirect('/home/') #login success
#                     else:# user not active
#                         message = 'username' + ' is not active.'
#                 else:#password wrong
#                     message = 'username and password are not match.'
#             else:#no username,password value
#                 message = 'What are you doing?'
#     else:
#         form = CaptchaTestForm()
#     return render_to_response('login.html',{'captcha':form,'message':message},context_instance=RequestContext(request))
