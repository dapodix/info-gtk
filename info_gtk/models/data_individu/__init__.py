from dataclasses import dataclass
from .status_kepegawaian import StatusKepegawaian
from .ijazah_terakhir import IjazahTerakhir
from .sekolah_induk import SekolahInduk, LokasiSekolahInduk
from .tugas_tambahan import TugasTambahan
from .jam_mengajar import JamMengajar, JamMengajarInduk, JamMengajarNonInduk


@dataclass
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


__all__ = [
    "StatusKepegawaian",
    "IjazahTerakhir",
    "SekolahInduk",
    "LokasiSekolahInduk",
    "TugasTambahan",
    "JamMengajar",
    "JamMengajarInduk",
    "JamMengajarNonInduk",
    "DataIndividu",
]
