from django import forms
from ...library.helpers import generate_template_choices


class ChangeProfileTemplateForm(forms.Form):
    template = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'custom-select',
                'id': 'inputGroupSelect',
            }
        ),
        choices=generate_template_choices(),
    )
