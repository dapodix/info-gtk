from dataclasses import dataclass


@dataclass
class StatusNuptk:
    nuptk: str
    nama: str
    tempat_lahir: str
    tanggal_lahir: str
    nama_ibu_kandung: str
    nip: str
    nik: str
    instansi: str
    kab_kota: str
