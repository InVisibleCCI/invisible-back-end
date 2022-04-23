from rest_framework.pagination import LimitOffsetPagination


class OnStaminaLimitOffsetPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None, initial_queryset=None):
        if initial_queryset is None:
            return super(OnStaminaLimitOffsetPagination, self).paginate_queryset(queryset, request, view=view)

        self.count = self.get_count(initial_queryset)
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []

        return list(queryset)
