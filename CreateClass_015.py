class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f'Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm'

def main():
    try:
        panjang = float(input("Masukan panjang persegi panjang: "))
        lebar = float(input("Masukan lebar persegi panjang: "))

        # Memeriksa apakah panjang dan lebar positif
        if panjang <= 0 or lebar <= 0:
            print("Nilai panjang dan lebar tidak boleh negatif atau nol.")
            return

        PP = PersegiPanjang(panjang, lebar)

        print(PP)  # Menampilkan informasi objek
        print(f"Keliling: {PP.keliling()} cm")
        print(f"Luas: {PP.luas()} cm²")
        
    except ValueError:
        print("Nilai tidak valid, silakan masukkan angka.")

# Menjalankan fungsi main
if __name__ == "__main__":
    main()