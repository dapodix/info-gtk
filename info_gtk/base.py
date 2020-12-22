from dataclasses import dataclass, field
from logging import getLogger, Logger
from requests import Session


def make_logger(name="info-gtk") -> Logger:
    return getLogger(name)


@dataclass
class BaseInfoGtk(object):
    BASE_URL: str = field(default="https://info.gtk.kemdikbud.go.id/")
    _session: Session = field(default_factory=Session)
    _logger: Logger = field(default_factory=make_logger)
    _email: str = field(default="")
    _password: str = field(default="")
