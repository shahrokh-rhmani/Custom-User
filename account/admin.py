from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreatonForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreatonForm
    form = CustomUserChangeForm
    model = UserAdmin


admin.site.register(CustomUser, CustomUserAdmin)
