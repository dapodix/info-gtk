from info_gtk import __version__, InfoGtk


def test_version():
    assert __version__ == "0.1.0"


def test_info_gtk(email: str, password: str):
    info_gtk = InfoGtk(email, password)
    assert info_gtk.is_login is True
