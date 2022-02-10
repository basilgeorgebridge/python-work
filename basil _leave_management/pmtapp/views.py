from django.shortcuts import render ,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from pmtapp.models import UserProfile
from pmtapp.models import UserApplyLeave
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
# Create your views here.    
def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if(user.is_superuser):
                auth_login(request, user)
                messages.success(request, ('login successfully'))
                return redirect("/admins/")
            else:
               auth_login(request, user)
               messages.success(request, ('login successfully'))
               return redirect("/user/")
        else:
            messages.info(request,('login error'))
            return redirect("/") 
    else: 
        messages.info(request,('login error'))   
        return render(request,'users/login.html')

def forgot_password (request):
    return render(request,'users/forgotpass.html')


# USER

@login_required
def user_profile (request):
    userdet = UserProfile.objects.all()
    context = {'udet':userdet} 
    return render(request,'users/profile.html',context)

def user_apply_leave(request):
    if request.method == 'POST':
        userId = request.user.id
        leavetype = request.POST.get("lvtype")
        fromdate = request.POST.get("lv-from")
        to = request.POST.get("lv-to")
        daytype = request.POST.get("day")
        session = request.POST.get("half")
        reason = request.POST.get("reason")
        leave = UserApplyLeave(user_id=userId ,leavetype=leavetype, fromdate=fromdate, to=to, daytype=daytype, session=session, reason=reason)
        leave.save()
        messages.success(request, 'You have successfully Applied for the leave')
        return redirect('/leavestatus/')
    return render(request,'users/applyleave.html')

def leave_status (request):
    leavedet = UserApplyLeave.objects.all()
    context={'lv':leavedet}
    return render(request,'users/leavestatus.html',context)

def leave_status_delete(request,id):
    datas = UserApplyLeave.objects.get(id=id)
    datas.delete()
    return redirect("/leavestatus/")

def leave_status_edit(request,id):
    lvedit = UserApplyLeave.objects.get(id=id)
    return render(request,'users/edit_leavestatus.html',{'lvedt':lvedit})

def change(request,user_id):
    update = User.objects.get(id=user_id)
    update.password = request.POST.get("conpswd")
    update.save()
    return redirect("/user/")

# def leave_status_update(request, id):
#     update = UserApplyLeave.objects.filter(id=id).first()
#     update.leavetype = request.POST.get("leavetype")
#     update. fromdate = request.POST.get("leavefrom")
#     update.to = request.POST.get("leaveto")
#     update.daytype = request.POST.get("leaveday")
#     update.session = request.POST.get("leavehalf")
#     update.reason = request.POST.get("leavereason")   
#     update.save()
#     return render(request,'users/leavestatus.html',{'id':id})   

def change_password(request):
    return render(request,'users/chngpswd.html',)

def applying_leave_details(request,id):
    leavedet = UserApplyLeave.objects.get(id=id)
    return render(request,'users/applylvdetails.html',{'leavedet':leavedet})

# def change_passwordUser(request):
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(data=request.POST, user=request.user)
# 		if form.is_valid():
# 			form.save()
# 			update_session_auth_hash(request, form.user)
# 			messages.success(request, ('You Have Edited Your Password...'))
# 			return redirect('home')
# 	else:
# 		form = PasswordChangeForm(user=request.user)
	
# 	context = {'form': form}
# 	return render(request, 'authenticate/change_password.html', context)

def logout_user (request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('/login/')

# ADMIN

@login_required
def admin_profile(request):
    admindet = UserProfile.objects.all()
    context = {'udet':admindet} 
    return render(request,'admins/ad_profile.html',context)

def admin_leave_request (request):
    leavedet = UserApplyLeave.objects.all()
    context={'lv':leavedet}
    return render(request,'admins/ad_leaverequest.html',context)

def admin_change_password(request):
    return render(request,'admins/ad_chngpswd.html',)

def logout_admin (request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('/login/')


# def (request):
#     return render(request,'users/.html')




         
