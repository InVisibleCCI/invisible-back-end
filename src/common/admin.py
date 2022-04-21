from django.contrib import admin

from common.models import Image, Address
from core.models import User


def get_list_fields_names(class_, exclude=None):
    """
    From a class given in parameter returns a list of strings corresponding to the different properties
    :param class_: Class to analyze
    :param: exlude : List of property to exclude from list field names
    :return List of string of fields name

    """

    if exclude is None:
        exclude = []
    exclude_fields_names = ['id', 'created', 'updated', 'deleted_at'] + exclude
    fields = [f.name for f in class_._meta.get_fields() if
              ((not hasattr(f, 'multiple') or not f.multiple) and f.name not in exclude_fields_names)]

    if hasattr(class_(), 'created'):
        fields = ['id', 'created'] + fields
    else:
        fields = ['id'] + fields

    if hasattr(class_(), 'updated'):
        fields += ['updated']

    return fields


"""
    In order to use the admin, the Django admin must be overwritten to filter the information 
    displayed for the merchant

"""


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Image)

    def get_queryset(self, request):
        queryset = super(ImageAdmin, self).get_queryset(request)
        if request.user.is_merchant:
            return queryset.filter(merchant__user=request.user)
        return queryset


"""
    In order to use the admin, the Django admin must be overwritten to filter the information 
    displayed for the merchant

"""


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Address, exclude=['latitude', 'longitude'])

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_merchant:
            if db_field.name == "user":
                kwargs['queryset'] = User.objects.filter(id=request.user.id)

        return super(AddressAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super(AddressAdmin, self).get_queryset(request)
        if request.user.is_merchant:
            return queryset.filter(user=request.user)
        return queryset
