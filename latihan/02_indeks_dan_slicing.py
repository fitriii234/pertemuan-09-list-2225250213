# ==================================================
# PERTEMUAN 09 | INDEKS DAN SLICING
# ==================================================

def main():
    nilai = [60, 70, 80, 90, 85]

    print("=" * 48)
    print("          INDEKS DAN SLICING LIST")
    print("=" * 48)

    print(f"Daftar nilai       : {nilai}")
    print(f"Elemen pertama     : {nilai[0]}")
    print(f"Elemen terakhir    : {nilai[-1]}")
    print(f"Tiga elemen awal   : {nilai[:3]}")
    print(f"Elemen indeks 1-3  : {nilai[1:4]}")

    print("=" * 48)


if __name__ == "__main__":
    main()