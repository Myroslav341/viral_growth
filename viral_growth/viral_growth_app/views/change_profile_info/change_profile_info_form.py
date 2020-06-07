from django import forms


class ChangeProfileInfoForm(forms.Form):
    profile_info = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message-text',
            }
        )
    )
