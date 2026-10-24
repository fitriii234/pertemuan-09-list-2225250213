# ==================================================
# PERTEMUAN 09 | MANIPULASI LIST
# ==================================================

def main():
    nilai = [60, 70, 80]

    print("=" * 48)
    print("             MANIPULASI LIST")
    print("=" * 48)

    print(f"List awal          : {nilai}")

    nilai.append(90)
    print(f"Setelah append     : {nilai}")

    nilai.insert(1, 65)
    print(f"Setelah insert     : {nilai}")

    nilai[0] = 75
    print(f"Setelah perubahan  : {nilai}")

    nilai.remove(80)
    print(f"Setelah remove     : {nilai}")

    print("=" * 48)


if __name__ == "__main__":
    main()