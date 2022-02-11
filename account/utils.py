from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_activation_code(email, code):
    context = {
        "text_detail": "Спасибо за регистрацию",
        "email": email,
        "domain": "http://localhost:8000",
        "code": code
    }  # заголовок, тело сообщения
    msg_html = render_to_string("email.html", context)
    message = strip_tags(msg_html)
    send_mail(
        "Активация аккаунта",
        message,
        "stackoverflowadmin@gmail.com",
        [email],
        html_message=msg_html,
        fail_silently=True
    )
