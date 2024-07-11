from .models import IncomingLetter
from datetime import date
import random as r

class IncomingLetterSeed:
     def generate_data(self, amount):
          for i in range(amount):
               surat_masuk = IncomingLetter(
                    letter_number='2024/BKN/'+str(i),
                    letter_date=date(2024, 6, 15),
                    received_date=date.today(),
                    recipient=nama_indonesia[r.randint(0, len(nama_indonesia)-1)]+' '+marga_manado[r.randint(0, len(marga_manado)-1)], 
                    source=sumber_surat[r.randint(0, len(sumber_surat)-1)],
                    file='incoming_letter/contoh.pdf',
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

nama_indonesia = [
    "Aisyah", "Amir", "Ani", "Bambang", "Budi", "Citra", "Dewi", "Dian", "Eka",
    "Fajar", "Fitri", "Galih", "Hani", "Irfan", "Joko", "Kartika", "Lestari",
    "Maya", "Nadia", "Nurul", "Putri", "Rahmat", "Rini", "Siti", "Tono", "Udin",
    "Vina", "Wati", "Yani", "Zaki", "Agus", "Ayu", "Bagus", "Candra", "Dedi",
    "Endah", "Fatimah", "Guntur", "Hasan", "Intan", "Junaedi", "Kusuma", "Linda",
    "Murni", "Nia", "Oki", "Parto", "Ratih", "Susi", "Tuti", "Umar", "Vera",
    "Wahyu", "Yuli", "Zaenal", "Ahmad", "Bella", "Cici", "Dinda", "Eko",
    "Farah", "Gilang", "Hendra", "Indah", "Joko", "Kiki", "Lia", "Melati",
    "Nanda", "Okta", "Pandu", "Rani", "Sari", "Tina", "Umi", "Vinda", "Wulan",
    "Yanti", "Zainal", "Ali", "Bunga", "Citra", "Dimas", "Euis", "Feri",
    "Gina", "Heru", "Ika", "Joko", "Kurnia", "Lita", "Mira", "Nova", "Olla",
    "Putra", "Ratih", "Santi", "Tono", "Ujang", "Vika", "Winda", "Yuni",
    "Zaenab", "Andi", "Caca", "Deden", "Eni", "Ferry", "Gita", "Herman",
    "Iis", "Jaja", "Kiki", "Lilis", "Mega", "Neni", "Opa", "Pipit", "Raden",
    "Siska", "Teguh", "Ucup", "Vivi", "Wiwin", "Yusuf", "Zainuddin", "Anto",
    "Cici", "Deden", "Endang", "Feri", "Galih", "Heri", "Iin", "Jajang",
    "Kartika", "Lili", "Melia", "Neneng", "Onah", "Pipin", "Raden", "Sasa",
    "Tejo", "Umi", "Vina", "Wawan", "Yuyun", "Zainab"
]

marga_manado = [
    "Abutan", "Adam", "Agou", "Agow", "Akay", "Akil", "Aling", "Alouw", "Alui", 
    "Amoi", "Ampow", "Andu", "Anes", "Angkouw", "Angow", "Anis", "Antou", "Aray", 
    "Arina", "Aruperes", "Assa", "Atuy", "Awondatu", "Awuy", "Arikalang", "Atotoy", 
    "Asseif", "Baramuli", "Batlayeri", "Bengko", "Bokong", "Bonjol", "Budiman", 
    "Buludawa", "Cakra", "Cambong", "Carundeng", "Datu", "Dendeng", "Dimpudus", 
    "Dotulong", "Dumanauw", "Elias", "Eman", "Engka", "Gerung", "Gimon", "Goni", 
    "Gunawan", "Inkiriwang", "Item", "Jems", "Kalalo", "Kalangi", "Kalempouw", 
    "Kalesaran", "Kapoyos", "Karinda", "Karisoh", "Kawatu", "Kawilarang", "Kawangitang", 
    "Keintjem", "Kilapong", "Korah", "Kowaas", "Kumentas", "Lala", "Laluyan", "Lampah", 
    "Langelo", "Langi", "Lapian", "Lasut", "Lembong", "Lengkong", "Luntungan", "Mamentu", 
    "Mandagi", "Mandey", "Mangare", "Manoppo", "Mantung", "Maramis", "Masengi", "Mawikere", 
    "Mendung", "Mewengkang", "Mokoagow", "Mokodompit", "Mokolensang", "Moningka", "Mongilong", 
    "Montalbo", "Muaya", "Nayoan", "Oley", "Ondang", "Palar", "Pangemanan", "Pantouw", 
    "Pauner", "Pelealu", "Pinontoan", "Pitoy", "Pojoh", "Polii", "Pomantouw", "Ponamon", 
    "Posumah", "Prins", "Rambi", "Rambitan", "Rantung", "Rarung", "Rembet", "Remboken", 
    "Roring", "Rotinsulu", "Rumagit", "Rumangkang", "Rumondor", "Saerang", "Sakul", "Salindeho", 
    "Sariowan", "Sengkey", "Sepang", "Siagian", "Simajuntak", "Simbar", "Sondakh", "Sompie", 
    "Supit", "Tambani", "Tambayong", "Tampi", "Tangkawarouw", "Taroreh", "Tatengkeng", "Tatumpe", 
    "Tenda", "Tengker", "Timbuleng", "Tintingon", "Tirayoh", "Tobing", "Tumbel", "Tumbelaka", 
    "Umbas", "Wajong", "Walalangi", "Walangitan", "Wantania", "Wenas", "Wongkar", "Wowor"
]

sumber_surat = [
    # Instansi Pemerintah Provinsi Sulawesi Utara
    "Dinas Pendidikan Daerah Provinsi Sulawesi Utara",
    "Dinas Kesehatan Provinsi Sulawesi Utara",
    "Dinas Pekerjaan Umum dan Penataan Ruang Provinsi Sulawesi Utara",
    "Badan Perencanaan Pembangunan Daerah Provinsi Sulawesi Utara",
    "Badan Kepegawaian Daerah Provinsi Sulawesi Utara",
    "Dinas Pemberdayaan Perempuan dan Perlindungan Anak Provinsi Sulawesi Utara",
    "Dinas Sosial Provinsi Sulawesi Utara",
    "Dinas Lingkungan Hidup Provinsi Sulawesi Utara",

    # Instansi Pemerintah Kabupaten Minahasa Selatan
    "Dinas Pendidikan dan Kebudayaan Kabupaten Minahasa Selatan",
    "Dinas Kesehatan Kabupaten Minahasa Selatan",
    "Dinas Pekerjaan Umum dan Penataan Ruang Kabupaten Minahasa Selatan",
    "Badan Perencanaan Pembangunan Daerah Kabupaten Minahasa Selatan",
    "Badan Kepegawaian Daerah Kabupaten Minahasa Selatan",
    "Dinas Pemberdayaan Perempuan dan Perlindungan Anak Kabupaten Minahasa Selatan",
    "Dinas Sosial Kabupaten Minahasa Selatan",
    "Dinas Lingkungan Hidup Kabupaten Minahasa Selatan",
    "Dinas Penanaman Modal dan Pelayanan Terpadu Satu Pintu Kabupaten Minahasa Selatan",
    "Dinas Kependudukan dan Pencatatan Sipil Kabupaten Minahasa Selatan",

    # Instansi Kecamatan Motoling Barat
    "Kantor Camat Motoling Barat",
    "Puskesmas Motoling Barat",
    "UPTD Pendidikan Kecamatan Motoling Barat",
    "UPTD Pertanian Kecamatan Motoling Barat",
    "Polsek Motoling Barat",
    "Koramil Motoling Barat",
    "Kantor Urusan Agama Kecamatan Motoling Barat",

    # Pemerintah Desa di Kecamatan Motoling Barat
    "Kantor Desa Motoling",
    "Kantor Desa Motoling Satu",
    "Kantor Desa Raanan Baru",
    "Kantor Desa Raanan Baru Dua",
    "Kantor Desa Keroit",
    "Kantor Desa Toyopon",
    "Kantor Desa Picuan",
    "Kantor Desa Tokin",
    "Kantor Desa Tondey",
    "Kantor Desa Tondey Dua",
    "Kantor Desa Molinow",
    "Kantor Desa Molinow Dua",

    # Sekolah di Kecamatan Motoling Barat
    "SD Inpres Motoling",
    "SD Inpres Motoling Satu",
    "SD Inpres Raanan Baru",
    "SD Inpres Raanan Baru Dua",
    "SD Inpres Keroit",
    "SD Inpres Toyopon",
    "SD Inpres Picuan",
    "SD Inpres Tokin",
    "SD Inpres Tondey",
    "SD Inpres Tondey Dua",
    "SD Inpres Molinow",
    "SD Inpres Molinow Dua",
    "SMP Negeri 1 Motoling Barat",
    "SMA Negeri 1 Motoling Barat",
    "SMK Negeri 1 Motoling Barat",

    # Instansi Vertikal
    "Kantor Kementerian Agama Kabupaten Minahasa Selatan",
    "Kantor Pertanahan Kabupaten Minahasa Selatan",
    "Pengadilan Negeri Amurang",
    "Kejaksaan Negeri Amurang",

    # Lembaga Swadaya Masyarakat (LSM)
    "Yayasan SHEEP Indonesia",
    "Yayasan Masarang",
    "Wahana Lingkungan Hidup Indonesia (WALHI) Sulawesi Utara",
    "Yayasan IDEP Selaras Alam",

    # Perusahaan Swasta
    "PT. Meares Soputan Mining",
    "PT. Bank Rakyat Indonesia (Persero) Tbk. Cabang Amurang",
    "PT. PLN (Persero) ULP Amurang",
    "PT. Telkom Indonesia (Persero) Tbk. Witel SulutMalut",

    # Lembaga Pendidikan Swasta
    "Universitas Kristen Indonesia Tomohon (UKIT)",
    "Sekolah Tinggi Teologia (STT) Jaffray",
    "Sekolah Menengah Kejuruan (SMK) Kristen Motoling",

    # Organisasi Masyarakat
    "Karang Taruna Kecamatan Motoling Barat",
    "Pemberdayaan Kesejahteraan Keluarga (PKK) Kecamatan Motoling Barat",
    "Kelompok Tani Nelayan Andalan (KTNA) Kecamatan Motoling Barat",
    "Majelis Ulama Indonesia (MUI) Kecamatan Motoling Barat",
    "Badan Pekerja Majelis Jemaat (BPMJ) GMIM Motoling Barat",
    "Kerukunan Keluarga Kawanua (KKK) Motoling Barat",

    # Tokoh Masyarakat (Contoh)
    "Franky Donny Wongkar, SH (Bupati Minahasa Selatan)",
    "Petra Yani Rembang (Wakil Bupati Minahasa Selatan)",
    "James Arthur Kojongian, ST., MM (Anggota DPRD Provinsi Sulawesi Utara Dapil Minahasa Selatan)",
    "Michaela Elsiana Paruntu (Anggota DPRD Provinsi Sulawesi Utara Dapil Minahasa Selatan)",
    "Frangky D. Wongkar (Camat Motoling Barat)",
    "Pdt. Lucky Rumopa (Ketua BPMJ GMIM Motoling)",

    # Warga (Contoh)
    "Bapak Jhon Rantung (Tokoh Masyarakat Desa Motoling)",
    "Ibu Meity Tampi (Ketua PKK Desa Motoling Satu)",
    "Sdr. Steven Kawatu (Ketua Karang Taruna Desa Raanan Baru)",
    "Ibu Grace Moningka (Kepala Sekolah SD Inpres Motoling)",
    "Sdr. Adrian Lengkong (Pemuda Pelopor Kecamatan Motoling Barat)",
]