from rest_framework import permissions
from products.models import Product
from . permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser, 
        IsStaffEditorPermission,
    ]


class UserQuerySetMixin:
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        user = self.request.user
        lookup_data[self.user_field] = user

        if user.is_authenticated:
            qs = super().get_queryset(*args, **kwargs)
            return qs.filter(**lookup_data)
        
        return Product.objects.none()
    