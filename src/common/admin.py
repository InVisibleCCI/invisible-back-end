from django.contrib import admin

from common.models import Image, Address


def get_list_fields_names(class_, exclude=None):
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


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Image)

@admin.register(Address)
class ImageAdmin(admin.ModelAdmin):
    list_display = get_list_fields_names(Address)
