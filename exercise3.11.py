# Program: intentional_error.py
# Deskripsi: Menghasilkan IndexError secara sengaja lalu memperbaikinya.

languages = ["Python", "JavaScript", "Rust"]

# Baris di bawah ini sengaja dibuat untuk memicu IndexError karena list hanya memiliki index 0, 1, dan 2:
# print(languages[3])  # IndexError: list index out of range

# Memperbaiki error dengan menggunakan index yang valid (misal index 2 atau index terakhir -1):
print("Mengakses elemen dengan index yang valid:")
print(f"Index 2: {languages[2]}")
print(f"Index terakhir (-1): {languages[-1]}")