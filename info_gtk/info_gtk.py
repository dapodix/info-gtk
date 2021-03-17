#!/usr/bin/env python

import attr
import logging
from bs4 import BeautifulSoup
from requests import Session
from typing import Optional

from . import DataIndividu
from .table_data import TableData


@attr.dataclass(slots=True)
class LoginData:
    userid: str
    password: str
    submit: str = "Login"
    mod: str = "cek_guru"
    metode: str = "Account"
    s: str = "990"


class InfoGtk:
    BASE_URL: str = "https://info.gtk.kemdikbud.go.id/"

    def __init__(self, email: str, password: str):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._email = email
        self._password = password
        self._session = Session()
        self._dashboard = ""
        self._soup: Optional[BeautifulSoup] = None
        self._data_individu: Optional[DataIndividu] = None
        self._verify = False
        self.is_login = False
        if not self.is_login:
            self.is_login = self.login(email, password)
        if not self._dashboard:
            self._dashboard = self.get_dashboard()

    @property
    def dashboard(self) -> str:
        if not self._dashboard:
            self._dashboard = self.get_dashboard()
        return self._dashboard

    @property
    def soup(self) -> BeautifulSoup:
        if self._soup:
            return self._soup
        self._soup = BeautifulSoup(self.dashboard, "html.parser")
        return self._soup

    @property
    def data_individu(self) -> DataIndividu:
        if self._data_individu:
            return self._data_individu
        table_data = TableData.make_individu(self.dashboard)
        self._data_individu = DataIndividu.from_table_datas(table_data)
        return self._data_individu

    def login(self, email: str = None, password: str = None, retry=0) -> bool:
        email = email or self._email
        password = password or self._password
        if self.is_login:
            self.logout()
        self._logger.debug("Getting login page")
        res = self._session.get(self.BASE_URL + "/?s=999&pesan=", verify=self._verify)
        if not res.ok:
            self._logger.debug("Getting login page failed")
            if retry > 0:
                return self.login(email, password, retry)
            return False
        # Capthca
        data = LoginData(
            userid=self._email,
            password=self._password,
        )
        headers = {"Referer": res.url}
        self._logger.debug("Trying to login")
        res = self._session.post(
            self.BASE_URL,
            data=attr.asdict(data),
            allow_redirects=False,
            headers=headers,
            verify=self._verify,
        )
        if not res.status_code == 302:
            self._logger.debug("Login failed")
            if retry > 0:
                return self.login(email, password, retry)
            return False
        self._logger.debug("Login success")
        return res.status_code == 302

    def get_dashboard(self) -> str:
        res = self._session.get(self.BASE_URL + "dashboard", verify=self._verify)
        if res.status_code != 404 or not res.text:
            return ""
        return res.text

    def logout(self) -> bool:
        res = self._session.get(self.BASE_URL + "auth/logout", verify=self._verify)
        return res.ok
