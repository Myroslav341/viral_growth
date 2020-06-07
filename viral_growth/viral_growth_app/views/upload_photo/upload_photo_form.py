from django import forms


class UploadPhotoForm(forms.Form):
    photo = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'custom-file-input',
                'id': 'photo_upload',
                'aria-describedby': 'inputGroupFileAddon01'
            }
        )
    )
