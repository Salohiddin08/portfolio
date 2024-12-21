from django.contrib import admin
from .models import Project, Contact

from django.contrib import admin


admin.site.register([Project, Contact])
# from .models import ContactView

# @admin.register(ContactView)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'created_at')
#     search_fields = ('name', 'email')
#     list_filter = ('created_at',)

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title', 'description')


