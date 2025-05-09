# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju, perusahaan multinasional dengan lebih dari 1.000 karyawan, menghadapi tantangan tingginya attrition rate (>10%). Untuk mengatasinya, manajer HR meminta analisis faktor-faktor penyebab serta pembuatan dashboard bisnis guna memantau dan mengelola tingkat attrition secara lebih efektif.

### Permasalahan Bisnis

Apa saja faktor kunci yang berkontribusi terhadap tingginya tingkat keluarnya karyawan (attrition) di perusahaan Jaya Jaya Maju?

### Cakupan Proyek

* Melakukan identifikasi terhadap faktor-faktor utama yang berkontribusi terhadap tingginya tingkat attrition karyawan.
* Mengembangkan dashboard interaktif yang mudah digunakan untuk membantu tim HR memantau indikator attrition.
* Membangun model prediksi dengan tingkat akurasi yang memadai untuk mendukung upaya retensi karyawan secara proaktif (Opsional).

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment Jika Belum Membuat Container Metabase Sebelumnya:
```
docker pull metabase/metabase:latest
docker run -p 3000:3000 --name metabase metabase/metabase
```

Setup environment Jika Sudah Membuat Container Metabase Sebelumnya:
```
docker start metabase
```

Credentials Metabase:
* Email: yanuarginting@gmail.com
* Password: GloryGloryManUtd123

## Business Dashboard

Dashboard dibangun menggunakan Metabase dan mencakup:

* Age Group vs. Attrition Rate
* Gender vs. Attrition Rate
* Marital Status vs. Attrition Rate
* Education Field vs. Attrition Rate
* Department vs. Attrition Rate
* Job Level vs. Attrition Rate
* Job Role vs. Attrition Rate
* Monthly Income Group vs. Attrition Rate
* Overtime vs. Attrition Rate
* Business Travel vs. Attrition Rate
* Distance From Home Group vs. Attrition Rate
* Job Satisfaction vs. Attrition Rate
* Environment Satisfaction vs. Attrition Rate
* Relationship Satisfaction vs. Attrition Rate

## Conclusion

* **Age Group**: Kelompok usia Young (17-30 tahun) (28.51%) memiliki attrition tertinggi. Menunjukkan generasi muda cenderung lebih cepat pindah kerja.
* **Gender**: Laki-laki memiliki attrition rate sedikit lebih tinggi (18.58%) dibanding perempuan (16.20%).
* **Marital Status**: Karyawan Single (27.42%) lebih rentan keluar dibanding Married (14.65%) dan Divorced (9.26%).
* **Education Field**: Latar belakang Technical Degree (26.58%) dan Marketing (22.68%) memiliki attrition tinggi.
* **Department**: Sales (21.77%) lebih tinggi dibanding R&D (15.79%) dan HR (15.62%).
* **Job Level**: Level 1 (28.61%) adalah yang paling rentan. Semakin tinggi level, semakin rendah attrition rate.
* **Job Role**: Posisi Sales Representative (44.90%) dan Laboratory Technician (28.40%) adalah yang paling rentan keluar.
* **Monthly Income Group**: Karyawan dengan penghasilan rendah (kurang dari sama dengan $2900) (30.70%) punya attrition tinggi. Income tinggi lebih stabil (10.53%).
* **Over Time**: Attrition rate sangat tinggi pada yang kerja lembur (32.71%) vs. yang tidak (11.32%).
* **Business Travel**: Semakin sering bepergian, semakin tinggi attrition (Frequent: 23.30%).
* **Distance from Home**: Semakin jauh dari kantor semakin tinggi attrition (Far (lebih dari 13km): 22.81%).
* **Job Satisfaction**:  Kepuasan dalam bekerja rendah (level 1) → attrition tinggi (21.23%).
* **Environment Satisfaction**: Kepuasan dalam lingkungan kerja rendah (level 1) → attrition sangat tinggi (29.95%).
* **RelationshipSatisfaction**: Level 1 juga paling tinggi (22.56%).

### Rekomendasi Action Items (Optional)

##### 🎯 **Retention for Young & Entry-level Employees**
* Buat program onboarding dan mentoring yang lebih baik.
* Sediakan jalur karier dan pelatihan skill jelas.
* Tawarkan growth opportunity yang lebih cepat dan transparan.
##### 💸 **Review Compensation & Overtime Policy**
* Tinjau kembali struktur gaji untuk kelompok penghasilan rendah.
* Kurangi lembur berlebih. Dorong work-life balance.
* Perbaiki manajemen beban kerja pada role yang rawan seperti Sales & Lab Technician.
##### 🚪 **Improve Work Conditions**
* Tingkatkan lingkungan kerja dan kepuasan melalui survei karyawan dan feedback rutin.
* Pastikan manajer memahami pentingnya hubungan interpersonal di tempat kerja.
##### 📍 **Address Commute and Travel Issues**
* Untuk karyawan yang tinggal jauh, pertimbangkan opsi hybrid/remote atau tunjangan transportasi.
* Evaluasi frekuensi perjalanan dinas dan beban tugasnya.
##### 📊 **Monitor High-Risk Groups**
* Fokus monitoring dan retensi pada:
    * Job Level 1
    * Sales Rep dan Tech roles
    * Single employees
    * Income rendah dan jarak jauh