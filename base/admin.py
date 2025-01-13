from django.contrib import admin
from base.models import CompanyUser, Leaves

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(CompanyUser, AuthorAdmin)
admin.site.register(Leaves, AuthorAdmin)
