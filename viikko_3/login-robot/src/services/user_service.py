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

        if not username or not password:
            raise UserInputError("Username and password are required")

        if re.match('^[a-z]{3,}$', username):
            print('Username OK')
        else:
            raise UserInputError('Invalid username')

        if re.match('(.{0,}|^)[^a-zA-Z](.{0,}|$)', password) and len(password) >= 8:
            print('Password OK')
        else:
            raise UserInputError('Invalid password')


        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


# Käyttäjätunnuksen on oltava merkeistä a-z koostuva vähintään 3 merkin
# pituinen merkkijono, joka ei ole vielä käytössä. Vinkki: säännölliset
#  lausekkeet ja ^[a-z]+$
# Salasanan on oltava pituudeltaan vähintään 8 merkkiä ja se ei saa 
# koostua pelkästään kirjaimista. Vinkki: säännölliset lausekkeet ja
#  [^a-z]