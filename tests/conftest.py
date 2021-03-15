import os
from pytest import fixture

from info_gtk import InfoGtk


@fixture
def email() -> str:
    return os.environ.get("EMAIL", "")


@fixture
def password() -> str:
    return os.environ.get("PASSWORD", "")


@fixture
def info_gtk(email: str, password: str) -> InfoGtk:
    return InfoGtk(email, password)
