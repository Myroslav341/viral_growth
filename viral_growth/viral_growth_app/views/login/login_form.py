from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            {
                'id': "password",
                'class': "form-control",
                'type': "password",
            }
        )
    )
