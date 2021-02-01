from django import forms

from mail_list.models import MailList


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = MailList
        fields = ['email', ]
