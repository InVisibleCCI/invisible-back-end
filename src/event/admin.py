from django.contrib import admin

from common.admin import get_list_fields_names
from event.models import Event
from event.models.category import Category, AccessibilityCategory
from merchant.models import Merchant


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Category)

@admin.register(AccessibilityCategory)
class AccessibilityCategoryAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(AccessibilityCategory)
