
from django.forms import ModelForm

from certificates.models import CertificateValidation

class CreateCertficateValidationForm(ModelForm):
    
    class Meta:
        model = CertificateValidation
        exclude = ["status"]

    # def __init__(self, *args, **kwargs):
    #     super(CreateCertficateValidationForm, self).__init__(*args, **kwargs)
    #     self.fields['certificate'].widget.attrs['class'] = 'form-file-input'
    #     self.fields['certificate'].widget.attrs['id'] = 'customFile' 