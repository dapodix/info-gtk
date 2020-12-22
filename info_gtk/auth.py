from . import BaseInfoGtk


class AuthInfoGtk(BaseInfoGtk):
    def login(self, email: str = None, password: str = None, retry=0) -> bool:
        email = email or self._email
        password = password or self._password
        self._logger.debug("Getting login page")
        res = self._session.get(self.BASE_URL + "/?s=999&pesan=")
        if not res.ok:
            self._logger.debug("Getting login page failed")
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
        self._logger.debug("Trying to login")
        res = self._session.post(self.BASE_URL, data=data, allow_redirects=False)
        if not res.status_code == 302:
            self._logger.debug("Login failed")
            if retry > 0:
                return self.login(email, password, retry)
            return False
        self._logger.debug("Login success")
        return res.status_code == 302

    def logout(self) -> bool:
        res = self._session.get(self.BASE_URL + "auth/logout")
        return res.ok
