# Membuat list bahasa pemrograman
languages = ["Python", "JavaScript", "C++", "Java", "Ruby"]

print("Initial list:")
print(languages)

# 1. Mengakses elemen menggunakan index
print(f"\nFirst language (index 0): {languages[0]}")
print(f"Last language (index -1): {languages[-1]}")

# 2. Mengubah nilai elemen
languages[4] = "Rust"
print(f"\nAfter modifying index 4: {languages}")

# 3. Menambahkan elemen dengan append()
languages.append("Go")
print(f"After append('Go'): {languages}")

# 4. Menyisipkan elemen dengan insert()
languages.insert(2, "TypeScript")
print(f"After insert(2, 'TypeScript'): {languages}")

# 5. Menghapus elemen dengan del
del languages[3]
print(f"After del languages[3]: {languages}")

# 6. Menghapus elemen dengan pop()
popped_language = languages.pop()
print(f"Popped language: {popped_language}")
print(f"After pop(): {languages}")

# 7. Menghapus elemen berdasarkan nilai dengan remove()
languages.remove("TypeScript")
print(f"After remove('TypeScript'): {languages}")

# 8. Pengurutan sementara dengan sorted()
print(f"\nTemporarily sorted with sorted(): {sorted(languages)}")
print(f"Original list preserved: {languages}")

# 9. Membalik urutan list dengan reverse()
languages.reverse()
print(f"\nReversed with reverse(): {languages}")
languages.reverse()
print(f"Back to previous order: {languages}")

# 10. Pengurutan permanen dengan sort() dan sort(reverse=True)
languages.sort()
print(f"\nPermanently sorted with sort(): {languages}")
languages.sort(reverse=True)
print(f"Permanently reverse-sorted with sort(reverse=True): {languages}")

# 11. Menghitung panjang list dengan len()
print(f"\nTotal languages in list with len(): {len(languages)}")