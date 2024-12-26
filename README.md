# Tugas Final Mata Kuliah Pengembangan Web Praktik IX

Mengimplementasi konsep dasar web menggunakan framework Flask

### Instalasi
Clone github
```shell
git clone https://github.com/aldoarnando/TUBES-PWEB-PRAKTIK-IX
```
Instalasi Modul
```shell
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Cara Commit Push dan Branch
Buat Branch Baru (misal mengerjakan landing page).
```shell
git branch landing-page
```
Pindah ke Branch baru
```shell
git checkout nama branch baru
```
Push Code ke Projek
```shell
git add .
git commit "menyelesaikan landing page"
git push -u origin landing-page
```
Note: jangan ngonding di branch main harus buat branch baru terlebih dahulu

### Cara menjalankan program
import database stuntcheck.sql
Ubah file .env.example menjadi .env
Buat GROC_API_KEY di GROC documentation
Atur GROC_API_KEY di file .env 
```shell
flask run
```