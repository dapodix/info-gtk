import attr


@attr.dataclass(slots=True)
class IjazahTerakhir:
    nama: str
    jurusan: str
    perguruan: str
