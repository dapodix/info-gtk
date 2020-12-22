from dataclasses import dataclass


@dataclass
class Profile:
    nama: str
    ttl: str
    pendidikan: str
    sekolah_induk: str
    email: str
    email_terverifikasi: bool
    alamat: str
