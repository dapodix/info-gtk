from __future__ import annotations
from bs4 import Tag
from dataclasses import dataclass
from .ijazah_terakhir import IjazahTerakhir
from .jam_mengajar import JamMengajar, JamMengajarInduk, JamMengajarNonInduk
from .sekolah_induk import SekolahInduk, LokasiSekolahInduk
from .status_kepegawaian import StatusKepegawaian
from .tugas_tambahan import TugasTambahan


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

    @classmethod
    def from_fit_individu(cls, tag: Tag) -> DataIndividu:
        # #fit_individu
        pass


__all__ = [
    "IjazahTerakhir",
    "JamMengajar",
    "JamMengajarInduk",
    "JamMengajarNonInduk",
    "SekolahInduk",
    "LokasiSekolahInduk",
    "StatusKepegawaian",
    "TugasTambahan",
    "DataIndividu",
]
