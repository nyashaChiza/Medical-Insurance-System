from django.conf import settings
from certificates.models import Certificate
from mailmerge import MailMerge


CERTIFICATE_TEMPLATE = settings.CERTIFICATE_TEMPLATE

class CertificateGenerator:
    def __init__(self, certificate: Certificate):
        self.certificate = certificate
        self.path = settings.BASE_DIR / 'media/certificates/'
    
    
    def generate(self):
        certificate = MailMerge(CERTIFICATE_TEMPLATE)
        
        try:
            certificate.merge(
                serviceNumber = str(self.certificate.hash)[:6],
                name = self.certificate.service_provider.name,
                position = self.certificate.title,
                key = str(self.certificate.hash),
                date = self.certificate.created,
                issuer = self.certificate.issuer
            )
            
            path = f"{self.path}{self.certificate.title}.docx"
            certificate.write(path)
            
            Certificate.objects.filter(id=self.certificate.id).update(path=path)
            return True
                
        except Exception as e:
            settings.LOGGER.error(e)
            return False        
        
    def get_path(self):
        return self.certificate.path
            