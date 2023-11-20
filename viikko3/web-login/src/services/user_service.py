from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import string


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
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        atoz = list(string.ascii_lowercase)
        if len(username) > 2:
            for key in username:
                if key not in atoz:
                    raise UserInputError("Username can only contain letters a-z")
        else:
            raise UserInputError("Username is too short")

        if len(password) > 7:
            i = len(password)
            for key in password:
                if key in atoz:
                    i -= 1
                    if i == 0:
                        raise UserInputError("Password can't only contain letters a-z")
        else:    
            raise UserInputError("Password is too short")
        
        if password != password_confirmation:
            raise UserInputError("Passwords don't match")

user_service = UserService()
