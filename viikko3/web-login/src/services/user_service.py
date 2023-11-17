from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        username_not_only_letters = False
        username_short = False
        username_taken = False
        password_has_only_letters = False
        password_short = False
        password_conf_no_match = False


        if not username or not password:
            raise UserInputError("Username and password are required")
        if not re.match("^[^0-9]+$", username):
            username_not_only_letters = True
        if len(username) < 3:
            username_short = True
        if self._user_repository.find_by_username(username):
            username_taken = True
        if re.match("^[^\d]+$", password):
            password_has_only_letters = True
        if len(password) < 8:
            password_short = True
        if password != password_confirmation:
            password_conf_no_match = True

        if (
            username_short
            and not password_has_only_letters
            and not password_short
            and not password_conf_no_match
        ):
            raise UserInputError("Password is valid but username is too short")
        if (
            password_has_only_letters
            and not username_short
            and not username_taken
            and not username_not_only_letters
        ):
            raise UserInputError("Username is valid but password can't contain only letters")
        if password_conf_no_match:
            raise UserInputError("Password doesn't match to password confirmation")

user_service = UserService()
