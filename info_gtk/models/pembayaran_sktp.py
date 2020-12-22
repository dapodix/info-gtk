from dataclasses import dataclass


@dataclass
class PeriodePembayaran:
    tw: int
    bulan: str


@dataclass
class BankPenyalur:
    nomor_rekening: str
    nama_pemegang_rekening: str
    nama_bank: str
    cabang_bank: str


@dataclass
class PembayaranSktp:
    no: int
    periode: PeriodePembayaran
    bank_penyalur: BankPenyalur
