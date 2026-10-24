# ==================================================
# PERTEMUAN 09 | FILTER KELULUSAN
# ==================================================

def main():
    nilai_mahasiswa = [55, 60, 70, 80, 90]
    batas_kelulusan = 60

    nilai_lulus = [
        nilai for nilai in nilai_mahasiswa
        if nilai >= batas_kelulusan
    ]

    nilai_tidak_lulus = [
        nilai for nilai in nilai_mahasiswa
        if nilai < batas_kelulusan
    ]

    print("=" * 48)
    print("              FILTER KELULUSAN")
    print("=" * 48)

    print(f"Daftar nilai       : {nilai_mahasiswa}")
    print(f"Batas kelulusan    : {batas_kelulusan}")
    print(f"Nilai lulus        : {nilai_lulus}")
    print(f"Nilai tidak lulus  : {nilai_tidak_lulus}")
    print(f"Jumlah mahasiswa lulus : {len(nilai_lulus)}")
    print(f"Jumlah belum lulus     : {len(nilai_tidak_lulus)}")

    print("=" * 48)


if __name__ == "__main__":
    main()