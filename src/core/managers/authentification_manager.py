from django.utils import timezone
from secrets import token_urlsafe

from rest_framework import exceptions

from common.mails import send_reset_password_mail
from core.models import User


class AuthenticationManager:
    """
    Manage authentication that handles successive unsuccessful connection attempts
    """
    error_message = {
        "disable_account": "Le compte a été désactivé, veuillez consulter vos mails"
    }

    def __init__(self, form_email):
        """
        Get current user who tries to log in with given form email
        """
        try:
            self.current_user = User.objects.get(email=form_email)
        except User.DoesNotExist:
            self.current_user = None

    def reset_password(self, temporary_password):
        self.current_user.set_password(temporary_password)
        self.current_user.save()

    def save_reset_password_token(self):
        self.current_user.reset_password_token = token_urlsafe(16)
        self.current_user.reset_password_token_end_validity_date = timezone.now() + timezone.timedelta(minutes=15)
        self.current_user.save()

    def manage_user_bad_credentials(self):
        """
        Check number of tries for current user, if it is more than three,
        we disable the current user and send an email to change the password
        """
        if self.current_user is None:
            return
        
        self.current_user.connection_attempt += 1
        self.current_user.save()

        if not self.current_user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_message['disable_account']
            )

        if self.current_user.connection_attempt >= 3:
            self.current_user.is_active = False

            temporary_password = token_urlsafe(12)
            self.reset_password(temporary_password)
            self.save_reset_password_token()
            self.current_user.save()

            send_reset_password_mail(self.current_user,
                                     "InVisible : Plusieurs tentatives infructueuses de connexion",
                                     temporary_password,
                                     change_password=False)
            raise exceptions.AuthenticationFailed(
                self.error_message['disable_account']
            )
