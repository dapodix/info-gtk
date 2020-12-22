from dataclasses import dataclass


@dataclass
class TunjanganProfesiGuru:
    nomor_sktp: str
    tanggal_penerbitan_sktp: str
    pembayaran_tpg_periode: str
    format_bayar: str
    nama_penerima: str
    nip: str
    nuptk: str
    nrg: str
    kab_kota: str
    provinsi: str
    rekening_bank: str
