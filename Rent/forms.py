from django import forms
from django.contrib.auth.models import User
from Rent import models


class AdminSignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password','is_superuser','is_staff']
        widgets = {
            'password': forms.PasswordInput()
        }

class ExecutiveUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class ExecutiveForm(forms.ModelForm):
    class Meta:
        model = models.Executive
        fields = ['address', 'mobile', 'status']


class AgreementForm(forms.ModelForm):
    class Meta:
        model = models.Agreement
        fields = ['agreementid','name','address','monthrent','hownername','contractperiod','startdate','increment','incrementamount']





class RentForm(forms.ModelForm):

    btsid = forms.ModelChoiceField(models.Agreement.objects.all().filter(status=True),
                                   empty_label="Select a BTS", to_field_name="id")
    class Meta:
        model = models.Rent
        fields = ['todate','totalmonth','totalrent']

