from django.contrib import admin

from common.admin import get_list_fields_names
from common.models import Address, Image
from event.models import Event
from event.models.category import Category, AccessibilityCategory
from merchant.models import Merchant

"""
    In order to use the admin, the Django admin must be overwritten to filter the information 
    displayed for the merchant

"""


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_merchant:
            if db_field.name == "address":
                kwargs['queryset'] = Address.objects.filter(user=request.user)
            if db_field.name == "merchant":
                kwargs['queryset'] = Merchant.objects.filter(user=request.user)

        return super(EventAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if request.user.is_merchant and db_field.name == "is_exclusive":
            return
        return super(EventAdmin, self).formfield_for_dbfield(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(EventAdmin, self).get_queryset(request)
        if request.user.is_merchant:
            return queryset.filter(merchant__user=request.user)
        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Category)


@admin.register(AccessibilityCategory)
class AccessibilityCategoryAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(AccessibilityCategory)
