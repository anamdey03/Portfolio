from .models import Contact
from django import forms


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'comments',
        ]