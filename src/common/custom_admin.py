import admin as admin


class InVisibleAdmin(admin.ModelAdmin):
    def has_permission(self):
        return self.request.user.is_staff or self.request.user.groups.filter('Merchant')
