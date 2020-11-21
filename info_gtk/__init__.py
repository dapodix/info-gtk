__version__ = "0.1.0"

from logging import getLogger
from requests import Session


class InfoGtk:
    def __init__(self, email: str, password: str):
        self.logger = getLogger(self.__class__.__name__)
        self._email = email
        self._password = password
        self.session = Session()
        self.BASE_URL = "https://info.gtk.kemdikbud.go.id/"

    def login(self, email: str = None, password: str = None, retry=0) -> bool:
        email = email or self._email
        password = password or self._password
        self.session.get(self.BASE_URL)
        self.logger.info("Getting login page")
        res = self.session.get(self.BASE_URL + "/?s=999&pesan=")
        if not res.ok:
            self.logger.info("Getting login page failed")
            if retry > 0:
                return self.login(email, password, retry)
            return False
        # Capthca
        data = {
            "userid": self._email,
            "password": self._password,
            "submit": "Login",
            "mod": "cek_guru",
            "metode": "Account",
            "s": "990",
        }
        self.logger.info("Trying to login")
        res = self.session.post(self.BASE_URL, data=data)
        if not res.status_code == 302:
            self.logger.info("Login failed")
            if retry > 0:
                return self.login(email, password, retry)
            return False
        self.logger.info("Login success")
        return res.status_code == 302

    def logout(self) -> bool:
        res = self.session.get(self.BASE_URL + "auth/logout")
        return res.ok

    def dashboard(self, retry=0) -> str:
        res = self.session.get(self.BASE_URL + "dashboard")
        if not res.ok:
            self.logger.info("Dashboard failed")
            if retry > 0:
                return self.login(self._email, self._password, retry)
            return ""
        self.logger.info("Dashboard success")
        return res.text
