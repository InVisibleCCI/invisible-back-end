from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import exceptions

from common.mails import send_reset_password_mail
from core.models import User


class AuthenticationManager:
    """
    Manage authentication that handles successive unsuccessful connection attempts
    """
    error_message = {
        "disable_account" : "Le compte a été désactivé, veuillez consulter vos mails"
    }



    def __init__(self, form_email):
        """
        Get current user who tries to log in with given form email
        """
        try:
            self.current_user = User.objects.get(email=form_email)
        except User.DoesNotExist:
            self.current_user = None

    def manage_user_bad_credentials(self):
        """
        Check number of tries for current user, if it is more than three,
        we disable the current user and send an email to change the password
        """
        if self.current_user is None:
            pass
        self.current_user.connection_attempt += 1
        self.current_user.save()

        if not self.current_user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_message['disable_account']
            )

        if self.current_user.connection_attempt >= 3 :
            self.current_user.is_active = False
            self.current_user.save()
            token = PasswordResetTokenGenerator().make_token(self.current_user)
            send_reset_password_mail(self.current_user,
                                     "InVisible : Plusieurs tentatives infructueuses de connexion",
                                     token)
            raise exceptions.AuthenticationFailed(
                self.error_message['disable_account']
            )
