from dataclasses import dataclass


@dataclass
class InvalidTestData:
    username: str | None
    password: str | None
    expected_error: str

@dataclass
class ValidTestData:
    username: str
    password: str

INVALID_LOGIN_DATA = [
    InvalidTestData(
        username="standard_user",
        password="wrong_pass",
        expected_error="Epic sadface: Username and password do not match any user in this service"
    ),
    InvalidTestData(
        username=None,
        password="wrong_pass",
        expected_error="Epic sadface: Username is required"
    ),
    InvalidTestData(
        username="locked_out_user",
        password="secret_sauce",
        expected_error="Epic sadface: Sorry, this user has been locked out."
    )
]

STANDARD_LOGIN = ValidTestData(username="standard_user", password="secret_sauce")