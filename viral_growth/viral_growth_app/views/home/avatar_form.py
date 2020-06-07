from django import forms


class AvatarForm(forms.Form):
    avatar = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'custom-file-input',
                'id': 'avatar_upload',
                'aria-describedby': 'inputGroupFileAddon01'
            }
        )
    )
