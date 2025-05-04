# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan kini memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Sebagai perusahaan yang sudah cukup besar, Jaya Jaya Maju menghadapi tantangan dalam mengelola sumber daya manusia (SDM) yang berdampak pada tingkat pergantian karyawan yang cukup tinggi.

### Permasalahan Bisnis
Walaupun perusahaan sudah berkembang pesat, Jaya Jaya Maju masih menghadapi masalah serius terkait attrition rate (rasio karyawan yang keluar). Tingkat pergantian karyawan ini telah melebihi 10%, yang dapat memengaruhi stabilitas operasional perusahaan.

Beberapa permasalahan yang perlu diidentifikasi dan diselesaikan adalah:

1. Tingginya Attrition Rate: Prosentase karyawan yang keluar terlalu tinggi, yang mengganggu kelangsungan operasional dan meningkatkan biaya rekrutmen serta pelatihan.

2. Faktor Penyebab Pergantian Karyawan: Perusahaan perlu mengetahui faktor-faktor spesifik yang mempengaruhi keputusan karyawan untuk meninggalkan perusahaan, seperti usia, jenis kelamin, departemen, peran pekerjaan, status pernikahan, dan lainnya.

3. Keterlibatan Karyawan: Perusahaan belum sepenuhnya memahami hubungan antara tingkat keterlibatan karyawan dengan pergantian karyawan.

4. Program Retensi yang Kurang Efektif: Strategi untuk mempertahankan karyawan mungkin belum optimal, dan perlu adanya evaluasi terhadap program retensi yang ada.

### Cakupan Proyek
Proyek ini bertujuan untuk membantu manajer HR Jaya Jaya Maju dalam mengidentifikasi faktor-faktor yang mempengaruhi tingginya attrition rate dan memberikan wawasan yang bisa digunakan untuk memperbaiki program retensi karyawan. Berikut adalah cakupan proyeknya:

1. Pengumpulan dan Persiapan Data: Mengumpulkan data karyawan yang relevan, seperti usia, jenis kelamin, departemen, jabatan, status pernikahan, dan status pergantian (attrition).
2. Analisis Faktor-faktor yang Mempengaruhi Attrition: Menggunakan analisis data untuk mengidentifikasi faktor-faktor yang paling berpengaruh terhadap tingkat pergantian karyawan.
3. Pembuatan Business Dashboard: Membuat dashboard interaktif di Metabase untuk memvisualisasikan data karyawan, seperti attrition rate berdasarkan usia, jenis kelamin, jabatan, departemen, dan faktor-faktor lainnya.
4. Rekomendasi Program Retensi: Berdasarkan hasil analisis, memberikan rekomendasi yang dapat membantu perusahaan mengurangi tingkat pergantian karyawan, seperti peningkatan program kesejahteraan, pengembangan karir, dan kebijakan kerja fleksibel.

### Persiapan
Sumber Data: [Link Sumber Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup Lingkungan:
a. Menyiapkan Environment Conda:
Buat Environment Conda Baru:
1. Jalankan perintah untuk membuat environment baru dengan Python versi 3.12:
```
conda create --name myenv python=3.12
```

2. Aktifkan Environment Conda:

Untuk pengguna MacOS:
```
conda activate myenv
```
Untuk pengguna Windows:
```
conda activate myenv
```

3. Install Requirements:
Install semua dependensi yang terdaftar dalam file requirements.txt:
```
pip install -r requirements.txt
```

b. Menyiapkan Metabase:
1. Pull Image Docker Metabase:
Untuk mengunduh versi terbaru dari Metabase menggunakan Docker, jalankan perintah:
```
docker pull metabase/metabase:v0.46.4
```

2. Jalankan Metabase dengan Docker:
Untuk menjalankan Metabase di port 3000, gunakan perintah:
```
docker run -p 3000:3000 --name metabase metabase/metabase
```

3. Akses Metabase:
Buka browser dan akses Metabase pada alamat berikut:
```
http://localhost:3000/setup
```

4. Ikuti petunjuk untuk menyelesaikan proses setup Metabase.


c. Menyiapkan Database (Supabase):
1. Buat Akun dan Login ke Supabase:
- Daftarkan akun dan masuk ke dasbor Supabase melalui [tautan ini](https://supabase.com/dashboard/sign-in).
3. Buat Proyek Baru:
- Klik New Project untuk memulai proyek baru di Supabase.
5. Salin URI Database:
- Salin URI yang tersedia di pengaturan database Supabase Anda.
6. Kirim Dataset menggunakan SQLAlchemy:
Gunakan SQLAlchemy untuk mengirim dataset ke database dengan kode berikut:
```
from sqlalchemy import create_engine
URL = "postgresql://postgres.zwnbxcaeqrgvrwicwjrt:qXg1oUaAjmFE93oN@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
engine = create_engine(URL)
df.to_sql('employee', engine)
```

Dengan langkah-langkah ini, Anda dapat menyiapkan environment, Metabase, dan Supabase untuk mulai bekerja dengan data dan membuat dashboard interaktif.

## Business Dashboard
Dashboard ini dirancang untuk memberikan wawasan kepada tim HR mengenai faktor-faktor yang mempengaruhi keputusan karyawan untuk mengundurkan diri. Dengan visualisasi interaktif, dashboard ini memungkinkan tim HR untuk:
1. Melihat jumlah total karyawan dan karyawan aktif.
2. Menganalisis rata-rata usia karyawan yang keluar dan mengidentifikasi kelompok usia yang lebih rentan terhadap pergantian.
3. Menghitung attrition rate dan menganalisis distribusi pergantian berdasarkan usia, jenis kelamin, departemen, status pernikahan, dan peran pekerjaan.
4. Membantu tim HR untuk mengidentifikasi area dengan tingkat pergantian tinggi dan fokus pada strategi retensi yang lebih efektif.

![Business_Dashboard_1](auric_21_dashboard_1.png)
![Business_Dashboard_2](auric_21_dashboard_2png)

## Conclusion
Dengan menggunakan dashboard ini, tim HR Jaya Jaya Maju dapat melakukan analisis yang lebih mendalam terhadap attrition dan mengambil langkah-langkah yang lebih tepat untuk mengurangi tingkat pergantian karyawan. Dengan informasi ini, HR dapat:
- Fokus pada departemen atau kelompok usia tertentu yang memiliki tingkat pergantian tinggi.
- Merancang program retensi yang lebih spesifik berdasarkan faktor-faktor seperti usia, jenis kelamin, dan status pernikahan.
- Meningkatkan keterlibatan karyawan dengan merancang kebijakan yang dapat mengurangi kelelahan atau meningkatkan kepuasan kerja.

### Rekomendasi Action Items (Optional)

1. Meningkatkan Program Retensi di Departemen dengan Tingkat Pergantian Tinggi
- Fokus pada Research & Development dan Sales, karena keduanya memiliki tingkat pergantian yang lebih tinggi.
2. Pengembangan Kebijakan Fleksibel untuk Kelompok Usia Tertentu
- Jika kelompok usia tertentu lebih sering mengundurkan diri, pertimbangkan untuk memberikan program pengembangan karir atau kebijakan kesejahteraan yang lebih fokus.
3. Program Kesejahteraan untuk Meningkatkan Retensi
- Untuk mengurangi attrition, perusahaan bisa menawarkan manfaat tambahan seperti keseimbangan kerja-hidup yang lebih baik atau jam kerja fleksibel.


