from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from core.models import Hackaton


class HackatonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HackatonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Crear'))

    class Meta:
        model = Hackaton
        exclude = ('created', 'updated', 'user')