from django import forms
from . import utility

# class LoginForm(forms.Form):
#     username = forms.CharField(required=False, label="Username", max_length=100)
#     password = forms.CharField(required=False, label="Password", max_length=100, widget=forms.PasswordInput)
#
# class WifiSelectForm(forms.Form):
#
#     CHOICES = utility.getWifiChoices()
#     print(CHOICES)
#     wifi_name = forms.ChoiceField(choices=CHOICES)
#     print(wifi_name.choices)
#     wifi_password = forms.CharField(required=False, label="Password", max_length=100, widget=forms.PasswordInput)
