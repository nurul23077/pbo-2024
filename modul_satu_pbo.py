# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/

# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;

# Test Pull Request dari Elyas
class test_dua:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

#modul_satu_pbo.py

class Mahasiswa:
    def __init__(self, name, npm, jurusan):
        self.name = name
        self.npm = npm
        self.jurusan = jurusan
        self.nilai = []

    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai.append({"mata_kuliah": mata_kuliah, "nilai": nilai})

    def rata_rata_nilai(self):
        if not self.nilai:
            return 0
        total_nilai = sum([item["nilai"] for item in self.nilai])
        return total_nilai / len(self.nilai)

    def tampilkan_info(self):
        print(f"Nema: {self.name}")
        print(f"NPM: {self.npm}")
        print(f"Jurusan: {self.jurusan}")
        print("Nilai:")
        for item in self.nilai:
            print(f"  {item['mata_kuliah']}: {item['nilai']}")
        print(f"Rata-rata Nilai: {self.rata_rata_nilai():.2f}")


#modul_satu_pbo_Diki.py

class informasi:
    def __init__ (self, nama, npm, kelas, jurusan, hobi, umur, alamat):
        self.n=nama
        self.npm=npm
        self.k=kelas
        self.j=jurusan
        self.h=hobi
        self.u=umur
        self.a=alamat

    def panggil (self):
        print(f"Nama Saya {self.n}, Npm Saya {self.npm}, Kelas {self.k}, Jurusan {self.j}, Hobi Saya {self.h}, Umur Saya {self.u}, Alamat saya di {self.a}")

def nilai1():
    return nilai(int(input("Masukan Nilai Anda : ")))

def nilai(nilai):
    if nilai >=80:
        print("A")
    elif nilai >=70:
        print("B")
    elif nilai >=60:
        print("C")
    elif nilai >=50:
        print("D")
    else:
        print("E")
    return nilai1()
