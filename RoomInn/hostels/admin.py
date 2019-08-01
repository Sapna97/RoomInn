from django.contrib import admin
from hostels.models import *

class HostelImageInline(admin.TabularInline):
    model = HostelImage
    extra = 6

class HostelAdmin(admin.ModelAdmin):
    inlines = [ HostelImageInline, ]

admin.site.register(HostelProfile, HostelAdmin)

