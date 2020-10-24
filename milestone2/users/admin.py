from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

User = get_user_model()


@admin.register(User)
class UserAdmin(OrigUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
    'id', 'first_name', 'last_name', 'email', 'is_active','is_staff'
    )
