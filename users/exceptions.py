from rest_framework.exceptions import APIException


class UsernameExistsException(APIException):
    default_code = "username_exists"
    status_code = 400
    default_detail = "This username is already taken"