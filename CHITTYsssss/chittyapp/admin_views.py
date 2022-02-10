from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from chittyapp.forms import AddMembersForm
from chittyapp.forms import EditMembersForm
from chittyapp.models import UserProfile 
from django.views.generic import View
from django.urls import reverse

# view functions

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password = password)
        if form.is_valid():
            if user is not None:
                if(user.is_superuser):
                    auth_login(request, user)
                    messages.success(request, ('login successfully'))
                    return redirect(reverse("adminindex"))
                else:
                    messages.info(request, "invalid credentials")
                    return redirect(reverse("login"))
        else:
            messages.info(request, "invalid credentials")
    else:
        form = AuthenticationForm()
    context = {'form':form}    
    return render(request,'login.html',context)

def logout(request):
    messages.info(request, "logout successfully")
    return render(request,'login.html')


@login_required   
def adminindex(request):
    return render (request,'admin/adminindex.html')

@login_required
def userindex(request):
    name = User.objects.all()
    image = UserProfile.objects.all()
    context = {'username':name , 'image':image}
    return render (request,'user/userindex.html',context)

@login_required
def password_change(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        return render(request,'admin/change-password.html',{'form':form})


@login_required
def add_members(request):
    form = AddMembersForm(request.POST, request.FILES,)
    if request.method == "POST":
        if form.is_valid():
           form.save()
           img = form.cleaned_data.get("idproof")
           messages.success(request,"Data has been added")
           return redirect("/members/view/",{'img':img})
        else:
            messages.info(request,"Check your Data") 
    context = {'form':form,}
    return render(request,'admin/add-members.html',context)

@login_required
def view_members(request):
    users = UserProfile.objects.all().prefetch_related('user')
    context = {'users':users}
    return render(request,'admin/view-members.html',context)

@login_required
def detailed_view_members(request,pk):
    users = UserProfile.objects.filter(id=pk).select_related('user')
    context = {'users':users}
    return render(request,'admin/detailed-view-members.html',context)

@login_required
def edit_members(request,pk):
    users = User.objects.get(id=pk)
    form = EditMembersForm( instance = users)
    if request.method == 'POST':
        form =  EditMembersForm(request.POST, instance = users )
        if form.is_valid():
            form.save()
            return redirect(reverse("/members/view/"))
    context = {"form" : form, "users" : users,}
    return render(request, "admin/edit-members.html", context)
    
@login_required
def user_password_change(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    return render(request,'admin/change-user-password.html',{'form':form})