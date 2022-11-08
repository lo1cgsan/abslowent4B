from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'required': 'required', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    nazwa = forms.CharField(label="Twój login", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    haslo = forms.CharField(label="Hasło", required=True, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))


