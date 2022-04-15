from django.contrib import admin

from UrlReduce.encurter.models import UrlLog, UrlRedirect

@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'dated', 'updated',)
    #prepopulated_fields = {'slug': ('destiny',)}

@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):
    list_display = ('origin', 'host', 'user_agent', 'ip', 'updated', 'url_redirect')

    def has_change_permission(self, request, obj=None) -> bool:
        return False


    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request, obj=None) -> bool:
        return False
