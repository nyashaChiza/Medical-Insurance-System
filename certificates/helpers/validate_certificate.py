from django.conf import settings
from certificates.models import Certificate
import docx2txt

class CertificateValidator:
    def __init__(self, path):
        self.path = path
        self.status = None
        self.hash = None
    
    def set_hash(self):      
        text = docx2txt.process(self.path)
        settings.LOGGER.debug(text)
        self.hash = 'hash'
            
        
    def get_certificate(self):
        self.set_hash()
        return Certificate.objects.filter(hash=self.hash).first()
        
        
def validate(path:str):
    validator = CertificateValidator(path)
    return validator.get_certificate()

    