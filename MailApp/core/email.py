from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_mail(to, subject_template, body_template, context):
    subject_text = render_to_string(subject_template, context)
    email_body = render_to_string(body_template, context)
    email = EmailMultiAlternatives('Subject', subject_text)
    email.attach_alternative(email_body, "text/html")
    email.to = to if isinstance(to, list) else [to]
    email.send()

