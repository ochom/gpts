from django.contrib import admin

# Register your models here.
from contact.models import Contact


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'created']


admin.site.register(Contact, ContactsAdmin)