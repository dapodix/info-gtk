#!/usr/bin/env python
from .version import __version__
from .base import BaseInfoGtk
from .auth import AuthInfoGtk
from logging import getLogger
from requests import Session


class InfoGtk(AuthInfoGtk):
    def __init__(self, email: str, password: str):
        self.logger = getLogger(self.__class__.__name__)
        self._email = email
        self._password = password
        self.session = Session()

    def _dashboard(self, retry=0) -> str:
        res = self.session.get(self.BASE_URL + "dashboard")
        if not res.ok:
            self.logger.info("Dashboard failed")
            if retry > 0:
                return self.login(self._email, self._password, retry)
            return ""
        self.logger.info("Dashboard success")
        return res.text
