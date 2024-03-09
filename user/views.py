from django.shortcuts import render,redirect

from django.contrib.auth.models import auth
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from user.models import Userprofileinfo
from user.forms import userFrom,UserprofileinfoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# def home(request):
#     # userform=userFrom()
#     # profileform=UserprofileinfoForm()
#     register=True
#     if request.method=="POST":
#         userform=userFrom(request.POST)
#         profileform=UserprofileinfoForm(request.POST,request.FILES)
        
#         if userform.is_valid() :
#             username=userform.cleaned_data['username']
#             if User.objects.filter(username=username).exists():
           
#                 user=userform.save()
#                 user.set_password(user.password)
#                 user.save()

#                 profile=profileform.save(commit=False)
#                 profile.user=user

#                 # if request.FILES:
#                 #     profile.profileimage=request.FILES['profileimage']
#                 profile.save()


#                 login(request,user)
#                 register=False

#             else:
#                 print(User.objects.filter(username=username))
#                 return HttpResponse("Username already exists")
#         else:
#                 print(userform.cleaned_data["confirm_password"])
#                 return HttpResponse("error Occured ")
    
#     return render(request,'register.html',{"user":userform,"profileform":profileform,'register':register})
@login_required
def home(request):

    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        if not User.objects.filter(username=username).exists():
            if password==confirmpassword:
                user=User.objects.create_user(username=username,password=password,email=email)
                login(request,user)
            else:
                return HttpResponse("register failed")
        else:
            return HttpResponse("user exits")

    return render(request,'main.html')
@login_required
def logoutuser(request):
    auth.logout(request)
    return redirect("user:home")

from django.http import JsonResponse

def loginuser(request):
    print(type(request))
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print(request)
            next_url=request.GET.get("next")
            print(next_url)

            return JsonResponse({'success': True,'status':'100','url':1})
        else:
            return JsonResponse({'success': False, 'error_message': 'Invalid username or password'})

    return render(request, 'main.html', {'show_login_modal': True})


@login_required
def com(request):
    return HttpResponse("hello")