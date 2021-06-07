from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Tasks

#
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Tasks
#         fields = '__all__'


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column('text', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('url', css_class='form-group col-md-4 mb-0'),
            ),
            Submit('submit', 'Save Changes')

        )

    class Meta:
        model = Tasks
        fields = ('title', 'text', 'url')
