# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di berbagai wilayah. Meskipun perusahaan telah mengalami pertumbuhan pesat, saat ini mereka menghadapi tantangan serius terkait pengelolaan sumber daya manusia, khususnya dalam hal retensi karyawan.

Tingkat attrition rate perusahaan telah melebihi 10%, yang berarti lebih dari 1 dari setiap 10 karyawan keluar dari perusahaan dalam kurun waktu tertentu. Kondisi ini menciptakan ketidakstabilan dalam operasional, meningkatnya biaya perekrutan dan pelatihan, serta hilangnya produktivitas dan pengetahuan institusional.

Manajer HR menyadari bahwa penyebab dari attrition ini bersifat kompleks dan tidak bisa dilihat dari satu sisi saja. Oleh karena itu, perusahaan ingin memanfaatkan pendekatan berbasis data untuk:

    * Mengidentifikasi faktor-faktor yang paling berpengaruh terhadap keputusan karyawan untuk keluar dari perusahaan.

    * Membangun sistem pemantauan yang dapat digunakan oleh tim HR untuk melakukan intervensi secara lebih cepat dan strategis.

    * (Opsional) Memprediksi kemungkinan karyawan untuk keluar di masa depan, guna mendukung program retensi secara proaktif.

Melalui pendekatan ini, perusahaan berharap dapat menekan tingkat attrition secara signifikan serta meningkatkan stabilitas dan kepuasan kerja di dalam organisasi.

### Permasalahan Bisnis

    * Departemen HR kesulitan dalam mengidentifikasi karakteristik dan faktor-faktor utama yang menyebabkan karyawan mengundurkan diri dari perusahaan.
    * Perusahaan belum memiliki sistem pemantauan yang efektif untuk mendeteksi dan mengantisipasi risiko attrition secara real-time.

### Cakupan Proyek

    * Melakukan identifikasi terhadap faktor-faktor utama yang berkontribusi terhadap tingginya tingkat attrition karyawan.
    * Mengembangkan dashboard interaktif yang mudah digunakan untuk membantu tim HR memantau indikator attrition.
    * Membangun model prediksi dengan tingkat akurasi yang memadai untuk mendukung upaya retensi karyawan secara proaktif (Opsional).

### Persiapan

* Download Sumber Data
    * Sumber data: https://drive.google.com/file/d/1G2JqEJgHtKng9kPtYkUz6deDpn80BMDD/view?usp=sharing
    * Dependensi: https://drive.google.com/file/d/1rlYZ8lF1Oeqo4V89MuwaW3k1IRuXoxNm/view?usp=sharing
    * File untuk melakukan prediksi (prediction.zip): https://drive.google.com/file/d/1kdzmrbqPcOhu27rdgvDTVVjzeZVadah_/view?usp=sharing
    * Setelah file terunduh, lakukan ekstrak file untuk format .zip (prediction.zip) lalu simpan semua file yang telah terunduh di lokasi tempat virtual environment berada (D:\Project\ML\Employee-Attrition-Analysis-and-Prediction), untuk cara membuat virtual environment akan dijelaskan setelah ini.

* Membuat, Mengaktifkan Virtual Environment, Menginstal Dependensi, dan Menjalankan kode untuk Melakukan Prediksi (prediction.py)
    * Jalankan perintah berikut di terminal laptop/PC kalian:
        ```
        cd D:\Project\ML
        ```
    * Buat virtual environment
        ```
        python -m venv Employee-Attrition-Analysis-and-Prediction
        ```
    * Aktifkan virtual environment
        ```
        .\Employee-Attrition-Analysis-and-Prediction\Scripts\Activate.ps1
        ```
    * Install dependensi
        ```
        pip install -r requirements.txt
        ```
    * Menjalankan kode untuk melakukan prediksi (prediction.py)
        ```
        Python prediction.py
        ```
    * Menonaktifkan environment
        ```
        deactivate
        ```

Setup environment Jika Belum Membuat Container Metabase:
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

* Over Time & Age Group vs. Attrition
* Over Time & Monthly Income Group vs. Attrition
* Over Time & Business Travel vs. Attrition
* Over Time & Job Satisfaction vs. Attrition
* Age Group & Monthly Income Group vs. Attrition
* Gender & Marital Status vs. Attrition
* Education Field & Department vs. Attrition
* Education Field & Job Role vs. Attrition (Top 20)
* Job Level & Education vs. Attrition

* Over Time & Age Group vs. Attrition Rate
* Over Time & Monthly Income Group vs. Attrition Rate
* Over Time & Business Travel vs. Attrition Rate
* Over Time & Job Satisfaction vs. Attrition Rate
* Age Group & Monthly Income Group vs. Attrition Rate
* Gender & Marital Status vs. Attrition Rate
* Education Field & Department vs. Attrition Rate
* Education Field & Job Role vs. Attrition Rate (Top 20)
* Job Level & Education vs. Attrition Rate

## Conclusion

Berdasarkan hasil analisis multivariate yang mengaitkan berbagai kombinasi fitur karyawan terhadap attrition rate, ditemukan bahwa kelompok karyawan dengan karakteristik tertentu secara konsisten menunjukkan risiko attrition yang jauh lebih tinggi. Berikut ini adalah karakteristik umum dari karyawan yang cenderung melakukan attrition:
### 👤 Profil Karyawan dengan Risiko Attrition Tinggi
1. Usia muda (kategori: Young), terutama dengan penghasilan rendah.
2. Sering lembur (OverTime = Yes), khususnya jika digabung dengan:
     * Kepuasan kerja rendah (JobSatisfaction rendah).
     * Penghasilan rendah (MonthlyIncomeGroup: Low).
     * Frekuensi perjalanan kerja tinggi (BusinessTravel = Travel_Frequently).
3. Status lajang (terutama Male - Single).
4. Berada pada level pekerjaan rendah (JobLevel = 1) dan pendidikan menengah ke bawah.
5. Mismatch antara latar belakang pendidikan dan job role, misalnya:
     * Technical Degree - Sales Representative
     * Other - Sales Representative
     * Life Sciences - Sales Representative
6. Berada di departemen Sales atau Human Resources dengan latar pendidikan yang tidak linear.
### 🧠 Alasan di Balik Kesimpulan
1. OverTime dan JobSatisfaction:
     * Lembur yang terus menerus memperburuk kualitas hidup kerja, apalagi jika tidak dibarengi dengan kompensasi atau kepuasan kerja memadai.
2. Usia Muda dan Gaji Rendah:
     * Karyawan muda lebih terbuka terhadap peluang baru. Jika penghasilan tidak sesuai harapan, mereka lebih mudah mengambil keputusan untuk pindah.
3. Status Marital:
     * Karyawan lajang biasanya lebih mobile dan fleksibel dalam keputusan karier, dibandingkan yang sudah menikah atau punya tanggungan.
4. Mismatch Pendidikan - Peran:
     * Ketidaksesuaian ini berpotensi menimbulkan stress, kurangnya keterampilan teknis, atau frustrasi karena tidak bisa berkembang.
5. Level Jabatan Awal:
     * Minimnya jenjang karier, pembinaan, dan gaji sering menjadi penyebab frustrasi di kalangan entry-level.

### Rekomendasi Action Items (Optional)

1. **Kurangi beban lembur**, khususnya untuk karyawan muda dan berpenghasilan rendah.
2. **Evaluasi ulang kompensasi** bagi kelompok risiko tinggi seperti “Young - Low Income”.
3. **Tingkatkan kepuasan kerja** melalui engagement program dan career development.
4. **Perhatikan kecocokan antara latar belakang pendidikan dan job role** saat merekrut.
5. **Berikan insentif atau jalur karier jelas** bagi karyawan level bawah untuk meningkatkan retensi.