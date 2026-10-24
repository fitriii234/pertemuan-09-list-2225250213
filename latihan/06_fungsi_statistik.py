# ==================================================
# PERTEMUAN 09 | FUNGSI STATISTIK
# ==================================================

def hitung_statistik(data):
    if not data:
        return None

    return {
        "jumlah_data": len(data),
        "total": sum(data),
        "rata_rata": sum(data) / len(data),
        "minimum": min(data),
        "maksimum": max(data),
    }


def main():
    nilai = [60, 70, 80]
    hasil = hitung_statistik(nilai)

    print("=" * 48)
    print("             FUNGSI STATISTIK")
    print("=" * 48)

    print(f"Daftar nilai  : {nilai}")

    if hasil is not None:
        print(f"Jumlah data   : {hasil['jumlah_data']}")
        print(f"Total nilai   : {hasil['total']}")
        print(f"Rata-rata     : {hasil['rata_rata']:.2f}")
        print(f"Nilai minimum : {hasil['minimum']}")
        print(f"Nilai maksimum: {hasil['maksimum']}")
    else:
        print("Data belum tersedia.")

    print("=" * 48)


if __name__ == "__main__":
    main()