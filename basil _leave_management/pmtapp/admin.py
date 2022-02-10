from django.contrib import admin
from .models import UserProfile
from .models import UserApplyLeave

# Register your models here.
admin.site.register(UserProfile) #reflects in admin of django
admin.site.register(UserApplyLeave)



