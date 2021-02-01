from django.contrib import admin

# Register your models here.
from mail_list.models import MailList


class MailListsAdmin(admin.ModelAdmin):
    list_display = ['email', 'created']


admin.site.register(MailList, MailListsAdmin)
