from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from wheeldeal.mixins.BootstrapMixins.FormControlMixin import FormControlMixin
from wheeldeal.profiles.models import UserProfile

UserModel = get_user_model()


class SignInForm(FormControlMixin, forms.Form):
    user = None
    email = forms.CharField(
        max_length=50,
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput,
    )

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Email and/or Password not valid!')

    def save(self):
        return self.user


class SignUpForm(FormControlMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')
