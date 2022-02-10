from django.urls import path
import pmtapp.views
urlpatterns = [
    path('login/', pmtapp.views.login, name='login'),
    path('user/', pmtapp.views.user_profile, name='profile'),
    path('logout/', pmtapp.views.logout_user, name='logout'),
    path('applyleave/', pmtapp.views.user_apply_leave, name='leaveapplication'),
    path('leavestatus/', pmtapp.views.leave_status, name='leavestatus'),
    path('chngpswd/', pmtapp.views.change_password, name='changepassword'),
    path('applylvdet/<int:id>/', pmtapp.views.applying_leave_details, name='applyinglvdet'),
    path('admins/', pmtapp.views.admin_profile, name='adminprofile'),
    path('delete/<int:id>/',pmtapp.views.leave_status_delete,name='delete'),
    path('edit/<int:id>/',pmtapp.views.leave_status_edit,name='edit'),
    # path('update/<int:id>/',pmtapp.views.leave_status_update,name='update'),
    path('change/<int:id>/',pmtapp.views.change,name='change'),
    
    path('admins/', pmtapp.views.admin_profile, name='ad-profile'),
    path('adleaverequest/', pmtapp.views.admin_leave_request, name='ad-leaverequest'),
    path('adchngpswd/', pmtapp.views.admin_change_password, name='ad-changepassword'),
    path('adlogout/', pmtapp.views.logout_admin, name='ad-logout'),
]