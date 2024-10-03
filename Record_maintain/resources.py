from import_export import resources
from .models import employee

class employeeresource(resources.ModelResource):
    class Meta:
        model=employee
        fields = ('Empid','Name','Mobile','Email','Role')