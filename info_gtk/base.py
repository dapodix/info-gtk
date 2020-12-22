from dataclasses import dataclass, field
from logging import Logger
from requests import Session


@dataclass
class BaseInfoGtk(object):
    session: Session = field(default_factory=Session)
    logger: Logger = field(default_factory=Logger)
    BASE_URL: str = field(default="https://info.gtk.kemdikbud.go.id/")
    _email: str = field(default="")
    _password: str = field(default="")
