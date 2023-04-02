from django.conf import settings
from certificates.models import Certificate
import docx2txt

class CertificateValidator:
    def __init__(self, path):
        self.path = path
        self.status = None
        self.hash = None
    
    def set_hash(self):
        try:      
            text = docx2txt.process(self.path)
            self.hash = text[:36]
        except:
            self.hash = None
            
            
        
    def get_certificate(self):
        if self.set_hash():
            return None
        
        return Certificate.objects.filter(hash=self.hash).first()
        
        
def validate(path:str):
    try:
        validator = CertificateValidator(path)
    except:
        return None
    return validator.get_certificate()

    