# Hand-Tracking

# **Hand Tracking untuk Game Subway Surfers**

🎮 **Deskripsi Proyek**  
Proyek ini adalah sistem **Hand Tracking** yang memungkinkan kamu memainkan game **Subway Surfers** menggunakan gerakan tangan. Dengan program ini, kamu bisa mengontrol karakter di game hanya dengan isyarat tangan tanpa perlu menggunakan keyboard atau mouse.



## **Fitur Utama**
- ✌️ **Double Tap untuk Skateboard**: Tunjukkan **jari telunjuk dan jari tengah** ke kamera untuk otomatis melakukan double tap dan memunculkan skateboard.  
- 👊 **Gerakan untuk Kontrol**: Gunakan isyarat berikut:
  - **Kepalkan tangan** dan geser **ke kiri atau kanan** untuk menggeser karakter.
  - **Kepalkan tangan** dan geser **ke atas** untuk melompat.
  - **Kepalkan tangan** dan geser **ke bawah** untuk bergulir.



## **Teknologi yang Digunakan**
- **Python**  
- **OpenCV**: Untuk menangkap dan memproses video dari kamera.  
- **MediaPipe**: Untuk deteksi dan pelacakan tangan.  
- **PyAutoGUI**: Untuk mensimulasikan input keyboard dan mouse ke komputer.  



## **Cara Instalasi**
1. Clone repositori ini ke komputer kamu:
   ```bash
   git clone https://github.com/username/subway_surfers_hand_tracking.git
   cd subway_surfers_hand_tracking
   ```

2. Install dependensi yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan program:
   ```bash
   python hand_tracking.py
   ```

4. Pastikan game **Subway Surfers** sudah berjalan.



## **Cara Penggunaan**
1. **Double Tap (Skateboard)**: Tunjukkan **jari telunjuk dan jari tengah** ke kamera.  
2. **Geser Karakter**:  
   - Kepalkan tangan, lalu geser **ke kiri** untuk berpindah ke jalur kiri.  
   - Geser **ke kanan** untuk berpindah ke jalur kanan.  
3. **Melompat atau Bergulir**:  
   - Geser tangan **ke atas** untuk melompat.  
   - Geser tangan **ke bawah** untuk bergulir.  



## **Struktur Proyek**
```
subway_surfers_hand_tracking/
├── hand_tracking.py                # File utama program
├── README.md                       # Dokumentasi proyek
├── requirements.txt                # Dependensi yang diperlukan
```


## **Pengembangan Selanjutnya**
- **Optimasi sensitivitas gerakan** untuk hasil yang lebih responsif.  
- **Penambahan gestur khusus** untuk fitur tambahan di game.  
- **Dukungan untuk game lain** yang berbasis kontrol gerak.  


## **Kontak**
📧 Jika ada pertanyaan atau saran, silakan hubungi saya melalui email:  
**contact@ccharles.my.id**

README ini menyesuaikan dengan nama file utama kamu yaitu `hand_tracking.py`. Semoga bermanfaat! 🚀
