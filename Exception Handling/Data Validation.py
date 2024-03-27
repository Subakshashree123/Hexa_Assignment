class InvalidDataException(Exception):
    pass

def validate_email(email):
    if '@' not in email or '.' not in email.split('@')[1]:
        raise InvalidDataException("Invalid email address format")
def register_user(email):
    try:
        validate_email(email)
        print("Registration successful")
    except InvalidDataException as e:
        print(f"Registration failed: {str(e)}")