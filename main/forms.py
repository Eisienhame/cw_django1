from django import forms
from main.models import Mailing, Client

class FormStyleMixin:
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Mailing
        fields = "__all__"


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Client
        fields = "__all__"
