from django import forms


class ChangeProfileBioForm(forms.Form):
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message-text',
            }
        )
    )
