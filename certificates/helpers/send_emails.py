

from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.mail import send_mail
import pytz

from certificates.models import Certificate

utc=pytz.UTC

def validate_alert(certificate: Certificate):
    return utc.localize(datetime.now()) > certificate.valid_until()

def send_reminder(certificate: Certificate):
    try:
        if validate_alert(certificate):
            recipient = settings.DEFAULT_ALERT_RECIPIENT
            sender = settings.GMAIL_HOST
            message = f"We are informing you that the certificate {certificate.title} for {certificate.service_provider} has expire, please process a new request."
            send_mail(
                "Certificate Expiry Alert",
                message,
                sender,
                [recipient],
                fail_silently=False,
            )

            settings.LOGGER.success('email sent successfully')
            return True
        return False
    except Exception as e:
        settings.LOGGER.error(e)
        return False


def send_reminders():
    certificates = Certificate.objects.all()
    
    for certificate in certificates:
        status = send_reminder(certificate)
        settings.LOGGER.info(f'certificate:{certificate} status:{status}')
        