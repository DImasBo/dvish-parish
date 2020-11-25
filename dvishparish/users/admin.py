from django.contrib.auth.models import Group, Permission
from .models import BankOffice, Premia, Bonus
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from dvishparish.users.forms import UserChangeForm, UserCreationForm

from rolepermissions.admin import RolePermissionsUserAdminMixin
from rolepermissions.roles import assign_role

User = get_user_model()

def make_user_manager(modeladmin, request, queryset):
    for user in queryset:
        assign_role(user, 'manager')

make_user_manager.short_description = "назначити менеджером"

class UserInline(admin.TabularInline):
    model = User
    extra = 0
    fields = ['email', 'name']


@admin.register(BankOffice)
class BankOfficeAdmin(admin.ModelAdmin):
    list_display = ["id", "city", "address"]
    list_filter = ['city']
    inlines = [
        UserInline
    ]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin, RolePermissionsUserAdminMixin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("salary", "bankoffice")}),) + tuple(
        auth_admin.UserAdmin.fieldsets
    )
    actions = [
        make_user_manager,
    ]
    add_fieldsets =((None, {'classes': ('wide',), 
            'fields': ('username', 'password1', 'password2')}),)
    list_display = ["username", "is_superuser", "is_staff"]
    search_fields = ["username"]
    list_filter = ['groups']
