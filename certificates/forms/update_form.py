
from django.forms import ModelForm

from certificates.models import Certificate

class UpdateCertficateForm(ModelForm):
    
    class Meta:
        model = Certificate
        exclude = ['hash', 'path']

    def __init__(self, *args, **kwargs):
        super(UpdateCertficateForm, self).__init__(*args, **kwargs)
        self.fields['service_provider'].widget.attrs['class'] = 'form-select js-select2' 