print("\n+--------------------------------+")
print("   | JIHAN ALYA NAFLAH |            ")
print("       | 2409116082 |               ")
print(" | SISTEM INFORMASI - C |           ")
print("+--------------------------------+\n")


while True:
        harga_barang =int(input("Masukkan harga barang: "))
        jumlah_pembelian = int(input("Masukkan jumlah pembelian : "))
        total_harga_barang = harga_barang * jumlah_pembelian
        print(f"Total harga barang: Rp {total_harga_barang:.2f}")


        if total_harga_barang > 250000: 
            diskon = total_harga_barang * 0.25
            total_harga_setelah_diskon = total_harga_barang - diskon 
            print("Selamat Anda Mendapatkan Diskon")
            print(f"Diskon 25%: Rp {diskon:.2f}")
            print(f"Total harga setelah diskon: Rp {total_harga_setelah_diskon:.2f}")
        else:
            print("Total", total_harga_barang)
        pilihan = input("Apakah anda ingin menghitung lagi? (y/t): ")
        if pilihan == 't': 
                    print("TERIMA KASIH")
                    break


