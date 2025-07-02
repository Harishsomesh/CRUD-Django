from django.shortcuts import render,redirect,get_object_or_404
from .models import user

def userinfo(request):
    if request.method=='POST': 
        data=request.POST
        user_name=data.get('user_name')
        user_mail=data.get('user_mail')
        user_number=data.get('user_number')

        user.objects.create(
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
    return redirect('/')

def update(request,id):
    User=get_object_or_404(user,id=id)
    if request.method=="POST":
        data=request.POST
        user_name=data.get('user_name')
        user_mail=data.get('user_mail')
        user_number=data.get('user_number')
        User.user_name= user_name
        User.user_mail=user_mail
        User.user_number=user_number
        User.save()
        return redirect('/')
    queryset=user.objects.all()
    context={'userinfo':queryset}
    print(context)

    return render(request,'Userinformation\edit.html',context)



# Create your views here.
