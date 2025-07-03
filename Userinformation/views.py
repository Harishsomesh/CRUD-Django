from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def userinfo(request):
    if request.method=='POST': 
        data=request.POST
        print(data,type(data))
        id=data.get('id')
        user_name=data.get('user_name')
        user_mail=data.get('user_mail')
        user_number=data.get('user_number')

        user.objects.create(
            id=id,
            user_name=user_name,
            user_mail=user_mail,
            user_number=user_number,
        )

        return redirect('/')
    queryset=user.objects.all()
    context={'userinfo':queryset}
    # print(context)

    return render(request,'Userinformation\index.html',context)

def delete(request,id):
    User=get_object_or_404(user,id=id)
    User.delete()
    print(user)
    return redirect('/')



def update(request,id):
    User=get_object_or_404(user,id=id)
    if request.method=="POST":
        data=request.POST
        User.user_name= data.get('user_name')
        User.user_mail=data.get('user_mail')
        User.user_number=data.get('user_number')
        User.save()
        return redirect('/')
    queryset=user.objects.all()
    context={'userinfo':queryset,'user':User}
    print(context)

    return render(request,'Userinformation\edit.html',context)



# Create your views here.
