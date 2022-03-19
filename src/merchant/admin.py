from django.contrib import admin

from common.admin import get_list_fields_names
from merchant.models import Merchant


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Merchant)
