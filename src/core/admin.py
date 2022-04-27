from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from core.models import User

class UserAdmin(BaseUserAdmin):

    readonly_fields = [
        'date_joined',
        'last_login'
    ]

    add_form = UserCreationForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_merchant', 'user_permissions', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)

    def has_permission(self,request):
        return request.user.is_superuser or request.user.is_merchant

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_inline_instances(self, request, obj=None):
        return obj and super(UserAdmin, self).get_inline_instances(request, obj) or []

    def save_model(self, request, user, form, change):

        super(UserAdmin, self).save_model(request, user, form, change)

admin.site.register(User, UserAdmin)
