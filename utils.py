from email_validator import validate_email, EmailNotValidError


def email_validator(value):
    try:
        validated_email = validate_email(value).email
        return validated_email
    except EmailNotValidError as e:
        raise ValueError(f"{value} is not a valid email address: {str(e)}")
