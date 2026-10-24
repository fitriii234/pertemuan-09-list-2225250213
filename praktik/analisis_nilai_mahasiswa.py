# ============================================================
# PERTEMUAN 09
# PRAKTIK ANALISIS NILAI MAHASISWA
# ============================================================

BATAS_KELULUSAN = 60


def analisis_nilai(nilai_mahasiswa):
    """Mengolah dan menganalisis kumpulan nilai mahasiswa."""

    if not nilai_mahasiswa:
        return None

    nilai_lulus = [
        nilai for nilai in nilai_mahasiswa
        if nilai >= BATAS_KELULUSAN
    ]

    nilai_tidak_lulus = [
        nilai for nilai in nilai_mahasiswa
        if nilai < BATAS_KELULUSAN
    ]

    return {
        "jumlah_mahasiswa": len(nilai_mahasiswa),
        "total_nilai": sum(nilai_mahasiswa),
        "rata_rata": sum(nilai_mahasiswa) / len(nilai_mahasiswa),
        "nilai_minimum": min(nilai_mahasiswa),
        "nilai_maksimum": max(nilai_mahasiswa),
        "nilai_lulus": nilai_lulus,
        "nilai_tidak_lulus": nilai_tidak_lulus,
        "jumlah_lulus": len(nilai_lulus),
        "jumlah_tidak_lulus": len(nilai_tidak_lulus),
    }


def tampilkan_hasil(hasil):
    """Menampilkan hasil analisis nilai mahasiswa."""

    print("=" * 56)
    print("             ANALISIS NILAI MAHASISWA")
    print("=" * 56)

    if hasil is None:
        print("Data nilai belum tersedia.")
        print("=" * 56)
        return

    print(f"Jumlah mahasiswa     : {hasil['jumlah_mahasiswa']}")
    print(f"Total nilai          : {hasil['total_nilai']}")
    print(f"Rata-rata nilai      : {hasil['rata_rata']:.2f}")
    print(f"Nilai minimum        : {hasil['nilai_minimum']}")
    print(f"Nilai maksimum       : {hasil['nilai_maksimum']}")

    print("-" * 56)
    print("HASIL PENYARINGAN KELULUSAN")
    print("-" * 56)

    print(f"Batas kelulusan      : {BATAS_KELULUSAN}")
    print(f"Daftar nilai lulus   : {hasil['nilai_lulus']}")
    print(f"Daftar tidak lulus   : {hasil['nilai_tidak_lulus']}")
    print(f"Jumlah lulus         : {hasil['jumlah_lulus']}")
    print(f"Jumlah tidak lulus   : {hasil['jumlah_tidak_lulus']}")

    print("=" * 56)


def main():
    nilai_mahasiswa = [60, 70, 80, 55, 90, 65, 75]

    hasil = analisis_nilai(nilai_mahasiswa)
    tampilkan_hasil(hasil)


if __name__ == "__main__":
    main()