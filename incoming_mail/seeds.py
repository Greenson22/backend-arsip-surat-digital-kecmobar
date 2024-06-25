from .models import IncomingLetter, Recipient, Source
from datetime import date
import random as r

class IncomingLetterSeed:
     def __init__(self):
          self.recipients = Recipient.objects.all()
          self.sources = Source.objects.all()

     def generate_data(self, amount):
          for i in range(amount):
               surat_masuk = IncomingLetter(
                    letter_number='2024/BKN/'+str(i),
                    letter_date=date(2024, 6, 15),
                    received_date=date.today(),
                    recipient=self.recipients[r.randint(0, len(self.recipients)-1)], 
                    source=self.sources[r.randint(0, len(self.sources)-1)],
                    file_url='https://contoh.url/surat.pdf',
                    subject=subjects[r.randint(0, len(subjects)-1)]
               )
               surat_masuk.save()
          print("Data incomingmail berhasil digenerate sebanyak "+str(amount))

subjects = [
    "Permohonan Izin Keramaian untuk Festival Durian Terlezat se-Kecamatan",
    "Usulan Pembentukan Tim Patroli Keamanan Anti Begal Berbasis Ojek Online",
    "Laporan Penemuan Fosil Purba di Belakang Kandang Ayam Warga",
    "Permohonan Bantuan Pembuatan Sumur Bor untuk Atasi Krisis Air Bersih",
    "Pengaduan Jalan Berlubang yang Bikin Shockbreaker Motor Pada Patah",
    "Proposal Lomba Mancing Mania di Sungai Dekat Kantor Camat",
    "Permohonan Izin Pentas Seni Budaya Tradisional untuk Lestarikan Kearifan Lokal",
    "Laporan Warga Resah Adanya Gangster Cilik yang Suka Tawuran",
    "Usulan Program Pelatihan Membuat Kerajinan Tangan dari Bahan Daur Ulang",
    "Permohonan Bantuan Bibit Tanaman Produktif untuk Ketahanan Pangan",
    "Pengaduan Polusi Udara dari Pabrik Tahu yang Bikin Sesak Napas",
    "Proposal Pembangunan Taman Bacaan untuk Tingkatkan Minat Baca Masyarakat",
    "Permohonan Izin Pertandingan Sepak Bola Antar RT untuk Mempererat Silaturahmi",
    "Laporan Pohon Tumbang di Jalan Raya yang Menghambat Lalu Lintas",
    "Usulan Pembentukan Kelompok Sadar Wisata untuk Promosikan Potensi Kecamatan",
    "Permohonan Bantuan Perbaikan Jembatan Rusak yang Ancam Keselamatan Warga",
    "Pengaduan Sampah Menumpuk di Kali yang Sebabkan Banjir Saat Hujan Deras",
    "Proposal Workshop Kewirausahaan untuk Tingkatkan Ekonomi Kreatif",
    "Permohonan Izin Pagelaran Wayang Kulit Semalam Suntuk di Lapangan Kecamatan",
    "Laporan Warga Resah dengan Maraknya Balap Liar di Jalanan Sepi",
    "Usulan Pembentukan Pos Ronda untuk Tingkatkan Keamanan Lingkungan",
    "Permohonan Bantuan Alat Pertanian Modern untuk Tingkatkan Produktivitas Petani",
    "Pengaduan Lampu Jalan Padam yang Bikin Rawan Kejahatan di Malam Hari",
    "Proposal Pelatihan Keterampilan Digital untuk Generasi Muda",
    "Permohonan Izin Pameran Produk UMKM Lokal untuk Dukung Ekonomi Masyarakat",
    "Laporan Warga Kesulitan Dapat Sinyal Internet untuk Belajar Online",
    "Usulan Program Bank Sampah untuk Mengurangi Volume Sampah di Lingkungan",
    "Permohonan Bantuan Perbaikan Saluran Irigasi yang Rusak Akibat Banjir",
    "Pengaduan Kebisingan dari Tempat Karaoke yang Ganggu Istirahat Warga",
    "Proposal Pelatihan Bahasa Asing untuk Tingkatkan Daya Saing Warga",
    "Permohonan Izin Bazar Kuliner untuk Promosikan Makanan Khas Daerah",
    "Laporan Warga Kehilangan Ternak Akibat Dicuri Orang Tak Dikenal",
    "Usulan Program Beasiswa Pendidikan untuk Anak Berprestasi dari Keluarga Kurang Mampu",
    "Permohonan Bantuan Rehabilitasi Rumah Tidak Layak Huni",
    "Pengaduan Air Bersih Keruh dan Berbau yang Mengganggu Kesehatan Warga",
    "Proposal Pelatihan Budidaya Ikan Lele untuk Tingkatkan Pendapatan Masyarakat",
    "Permohonan Izin Pendirian Koperasi Simpan Pinjam untuk Bantu Modal Usaha Warga",
    "Laporan Warga Resah dengan Maraknya Penipuan Online",
    "Usulan Program Penyuluhan Kesehatan Reproduksi untuk Remaja",
    "Permohonan Bantuan Pembangunan Tempat Pemakaman Umum yang Layak",
    "Pengaduan Jalan Berdebu yang Ganggu Pernapasan Warga",
    "Proposal Pelatihan Budidaya Tanaman Hidroponik untuk Efisiensi Lahan",
    "Permohonan Izin Penyelenggaraan Pasar Malam untuk Hiburan Warga",
    "Laporan Warga Kesulitan Mendapatkan Pelayanan Kesehatan di Puskesmas"
]