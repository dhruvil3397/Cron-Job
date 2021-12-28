from import_export import resources
from .models import UserProfile


class UserResource(resources.ModelResource):
    class Meta:
        model = UserProfile