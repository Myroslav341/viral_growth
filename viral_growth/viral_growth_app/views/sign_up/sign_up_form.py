from django import forms
from ...library.validators import validate_password, validate_unique_field
from ...library.constants import *
from ...models import User


class SignUpForm(forms.Form):
    email = forms.CharField(
        validators=[validate_unique_field(User, EMAIL)],
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control',
            }
        )
    )

    username = forms.CharField(
        validators=[validate_unique_field(User, USERNAME)],
        widget=forms.TextInput(
            attrs={
                'id': 'username',
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        validators=[validate_password],
        widget=forms.PasswordInput(
            {
                'id': "password",
                'class': "form-control",
                'type': "password",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            {
                'id': "confirm_password",
                'class': "form-control",
                'type': "password",
            }
        )
    )

    def is_valid(self):
        if not super().is_valid():
            return False

        if not self.data[PASSWORD] == self.data[CONFIRM_PASSWORD]:
            self.add_error(CONFIRM_PASSWORD, 'Password not match')

            return False

        return True
