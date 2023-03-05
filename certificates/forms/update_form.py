
from django.forms import ModelForm

from certificates.models import Certificate

class UpdateCertficateForm(ModelForm):
    
    class Meta:
        model = Certificate
        exclude = ['hash']

    # def __init__(self, *args, **kwargs):
    #     super(CreateCertficateForm, self).__init__(*args, **kwargs)
    #     self.fields['programme_type'].widget.attrs['class'] = 'form-select js-select2' 