from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        username_not_only_letters = False
        username_short = False
        username_taken = False
        password_has_only_letters = False
        password_short = False
    
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

        if (
            username_taken
            and not password_has_only_letters
            and not password_short
        ):
            raise UserInputError("Password is valid but username is taken")
        if (
            username_short
            and not password_has_only_letters
            and not password_short
        ):
            raise UserInputError("Password is valid but username is too short")
        if (
            username_not_only_letters
            and not username_short 
            and not password_has_only_letters
            and not password_short
        ):
            raise UserInputError("Password is valid but username can only contain letters")
        if (
            password_short
            and not username_short 
            and not username_not_only_letters
            and not username_taken
        ):
            raise UserInputError("Username is valid but password is too short")
        if (
            password_has_only_letters
            and not password_short
            and not username_short 
            and not username_not_only_letters
            and not username_taken
        ):
            raise UserInputError("Username is valid but password can't only contain letters")
