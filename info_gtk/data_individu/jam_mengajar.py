import attr
from typing import Optional


@attr.dataclass(slots=True)
class JamMengajarInduk:
    jam_mengajar: int
    jam_linier: int


@attr.dataclass(slots=True)
class JamMengajarNonInduk:
    jam_mengajar: Optional[int]
    jam_linier: Optional[int]


@attr.dataclass(slots=True)
class JamMengajar:
    sekolah_induk: JamMengajarInduk
    sekolah_non_induk: JamMengajarNonInduk
    total_mengajar: int
    total_linier: int
