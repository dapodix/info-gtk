import attr


@attr.dataclass(slots=True)
class SekolahInduk:
    nama: str
    validasi: str
    terdeteksi: str
    keterangan_validasi: str


@attr.dataclass(slots=True)
class LokasiSekolahInduk:
    provinsi: str
    kab_kota: str
    kecamatan: str
    desa_kelurahan: str
    kategori_desa_kelurahan: str
