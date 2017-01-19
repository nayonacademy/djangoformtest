from apps.models import *
from django import forms
from django.core.exceptions import ValidationError
print("forms is :", forms)

class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ['name', 'address', 'profession']

    def clean_name(self):
        data = self.cleaned_data['name']
        if data == 'nayon':
            raise forms.ValidationError('Fill the name field you going in wrong way')
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        if len(data) < 4:
            raise forms.ValidationError("Your address should be greater than 4")
        if data == ' ':
            raise forms.ValidationError('Address Field should not be empty')
        return data