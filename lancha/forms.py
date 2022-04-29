from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from lancha.models import Student

from crispy_forms.layout import Layout, Submit, Row, Column,Fieldset


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'roll')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # get or post
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-5'),
                Column('roll', css_class='form-group col-md-5'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Product')
        )
