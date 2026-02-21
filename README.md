# 🌙 Dream Journal - Aplikasi Catatan Mimpi

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Aplikasi web untuk mencatat dan menganalisis mimpi Anda. Dilengkapi dengan fitur CRUD lengkap, sistem tags, pencarian, dan statistik mimpi.

## ✨ Fitur

- 📝 **CRUD Operations** - Create, Read, Update, Delete mimpi
- 🔍 **Search** - Cari mimpi berdasarkan judul, deskripsi, atau tags
- 🏷️ **Tags System** - Kategorisasi mimpi dengan tags
- 📊 **Statistics** - Lihat statistik mimpi berdasarkan tipe
- 🎨 **Modern UI** - Desain gradient yang menarik dengan animasi
- 📱 **Responsive** - Tampilan optimal di desktop dan mobile
- 😊 **Mood Tracking** - Catat mood setelah bangun dari mimpi
- 🎭 **Dream Types** - Klasifikasi berbagai tipe mimpi

## 🚀 Teknologi

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3 (Vanilla)
- **Design**: Gradient UI, Glassmorphism

## 📋 Prerequisites

- Python 3.8 atau lebih tinggi
- MySQL 8.0 atau lebih tinggi
- pip (Python package manager)

## 🛠️ Instalasi

1. **Clone repository**
```bash
git clone https://github.com/username/dream-journal.git
cd dream-journal
```

2. **Buat virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install flask flask-mysqldb
```

4. **Setup Database**
- Buka MySQL dan jalankan script `schema.sql`
```bash
mysql -u root -p < schema.sql
```

5. **Konfigurasi Database**
- Edit file `app.py` sesuai dengan konfigurasi MySQL Anda:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'dream_journal'
```

6. **Jalankan Aplikasi**
```bash
python app.py
```

7. **Buka Browser**
```
http://localhost:5000
```

## 📁 Struktur Project

```
dream-journal/
│
├── app.py                  # File Flask utama
├── schema.sql              # Schema database MySQL
├── .gitignore             # Git ignore file
├── README.md              # Dokumentasi project
│
├── templates/              # Folder template HTML
│   ├── index.html         # Halaman utama
│   ├── add.html           # Form tambah mimpi
│   ├── edit.html          # Form edit mimpi
│   ├── view.html          # Detail mimpi
│   └── search.html        # Hasil pencarian
│
└── static/                # Folder static files
    └── style.css          # File CSS styling
```

## 🎯 Cara Penggunaan

### Menambah Mimpi Baru
1. Klik tombol "➕ Tambah Mimpi Baru"
2. Isi form dengan detail mimpi Anda:
   - Judul mimpi
   - Deskripsi lengkap
   - Tanggal mimpi
   - Mood setelah bangun
   - Tipe mimpi
   - Tags (opsional)
3. Klik "💾 Simpan Mimpi"

### Mencari Mimpi
1. Gunakan search bar di halaman utama
2. Masukkan kata kunci (judul, deskripsi, atau tags)
3. Tekan "Cari"

### Mengedit/Menghapus Mimpi
1. Klik "Lihat Detail" pada card mimpi
2. Pilih "✏️ Edit" untuk mengedit atau "🗑️ Hapus" untuk menghapus

## 🎨 Screenshot

### Halaman Utama
Menampilkan semua mimpi yang pernah dicatat dengan statistik

### Form Tambah Mimpi
Form lengkap untuk mencatat detail mimpi

### Detail Mimpi
Tampilan detail mimpi dengan semua informasi

## 🔧 Kustomisasi

### Mengubah Warna Theme
Edit file `static/style.css` pada bagian gradient:
```css
background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
```

### Menambah Tipe Mimpi
Edit file `templates/add.html` dan `templates/edit.html` pada bagian select dream_type

### Menambah Mood Options
Edit file templates pada bagian select mood

## 🤝 Kontribusi

Kontribusi selalu welcome! Silakan:
1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 To-Do List

- [ ] Export mimpi ke PDF
- [ ] Grafik analisis mimpi per bulan
- [ ] Upload gambar untuk mimpi
- [ ] Share mimpi ke social media
- [ ] Dark mode toggle
- [ ] Multi-language support

## 📄 License

Project ini menggunakan MIT License - lihat file [LICENSE](LICENSE) untuk detail

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Desain terinspirasi dari modern web apps
- Icons dari emoji Unicode
- Gradient color palette dari [UI Gradients](https://uigradients.com)

## 📧 Contact

Punya pertanyaan atau saran? Silakan buat issue atau hubungi saya di [email@example.com](mailto:email@example.com)

---
⭐ Jika project ini membantu Anda, berikan star di GitHub!
