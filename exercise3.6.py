guests = ["Alicia", "Adena", "Amanta"]

# Undangan awal
print(f"Dear {guests[0]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[1]}, it would be a pleasure to have you join us for dinner.")
print(f"Dear {guests[2]}, your presence at dinner tonight would be an absolute honor.")

print("\nGreat news! I found a bigger dinner table, so more guests can join us!\n")

# Menambahkan tamu:
# 1. Di awal list menggunakan insert()
guests.insert(0, "Calya")

# 2. Di tengah list menggunakan insert()
guests.insert(2, "James")

# 3. Di akhir list menggunakan append()
guests.append("Louis")

# Undangan untuk semua tamu
print(f"Dear {guests[0]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[1]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[2]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[3]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[4]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[5]}, I would be deeply honored to invite you to dinner.")