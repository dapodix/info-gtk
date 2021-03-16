import attr
from bs4 import Tag

from . import IjazahTerakhir
from . import JamMengajar
from . import SekolahInduk, LokasiSekolahInduk
from . import StatusKepegawaian
from . import TugasTambahan


@attr.dataclass(slots=True)
class DataIndividu:
    update_terakhir: str
    nuptk: str
    nama: str
    tanggal_lahir: str
    nik: int
    email: str
    tanggal_pensiun: str
    jenis_ptk: str
    status_kepegawaian: StatusKepegawaian
    ijazah_terakhir: IjazahTerakhir
    sekolah_induk: SekolahInduk
    lokasi_sekolah_induk: LokasiSekolahInduk
    tugas_tambahan: TugasTambahan
    jumlah_jam_mengajar: JamMengajar
    total_jjm_linier_tambahan: str

    @classmethod
    def from_fit_individu(cls, tag: Tag) -> "DataIndividu":
        # #fit_individu
        pass
