#!/usr/bin/env python
from .version import __version__  # NOQA
from .base import BaseInfoGtk  # NOQA
from .auth import AuthInfoGtk
from logging import getLogger
from requests import Session


class InfoGtk(AuthInfoGtk):
    def __init__(self, email: str, password: str):
        self._logger = getLogger(self.__class__.__name__)
        self._email = email
        self._password = password
        self._session = Session()
