from django.contrib import admin

from UrlReduce.encurter.models import UrlRedirect

@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'dated', 'updated',)
    #prepopulated_fields = {'slug': ('destiny',)}
