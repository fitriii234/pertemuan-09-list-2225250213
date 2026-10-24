# ==================================================
# PERTEMUAN 09 | AGREGASI NILAI
# ==================================================

def main():
    nilai = [60, 70, 80]

    jumlah_data = len(nilai)
    total_nilai = sum(nilai)
    rata_rata = total_nilai / jumlah_data if jumlah_data else 0

    print("=" * 48)
    print("              AGREGASI NILAI")
    print("=" * 48)

    print(f"Daftar nilai : {nilai}")
    print(f"Jumlah data  : {jumlah_data}")
    print(f"Total nilai  : {total_nilai}")
    print(f"Rata-rata    : {rata_rata:.2f}")

    print("=" * 48)


if __name__ == "__main__":
    main()