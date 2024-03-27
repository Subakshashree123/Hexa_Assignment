class AuthenticationException(Exception):
    pass

class AuthorizationException(Exception):
    pass

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationService:
    def authenticate_user(self, username, password):
        if username == "admin" and password == "password":
            print("User authenticated successfully")
            return User(username, password)
        else:
            raise AuthenticationException("Authentication failed: Invalid username or password")

class AuthorizationService:
    def authorize_user(self, user, role):
        if user.username == "admin" and role == "admin":
            print("User authorized successfully")
        else:
            raise AuthorizationException("Authorization failed: Insufficient privileges")