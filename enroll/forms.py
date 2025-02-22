from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm
from enroll.models import customer


class signupform(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
    )
    password2 = forms.CharField(
        label=("Password_confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model=User
        fields=["username","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }
class login_form(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control"}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control"}),
    )

class password_change(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),widget=forms.PasswordInput(attrs={"class":"form-control"}),)
    new_password1 = forms.CharField(label=("new password"),widget=forms.PasswordInput(attrs={"class":"form-control"}),)
    new_password2 = forms.CharField(label=("confirm password"),widget=forms.PasswordInput(attrs={"class":"form-control"}),)


    # old_password =forms.CharField(label=("Old Password"),widget=forms.PasswordInput(attrs={"class":"form-control"}))
    # new_password1 =forms.CharField(label=("new Password"),widget=forms.PasswordInput(attrs={"class":"form-control"}))
    # new_password2 =forms.CharField(label=("conform Password"),widget=forms.PasswordInput(attrs={"class":"form-control"}))

class setpasswordconfirm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        strip=False,
        
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
    )

class profileform(forms.ModelForm):
    class Meta:
        model=customer
        fields=["name","phone","email","city","state","pincode"]
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "phone":forms.NumberInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "city":forms.TextInput(attrs={'class':'form-control'}),
            "sate":forms.TextInput(attrs={'class':'form-control'}),
            "pincode":forms.NumberInput(attrs={'class':'form-control'}),

        }