guests = ["Alicia", "Adena", "Amanta"]

# Undangan awal
print(f"Dear {guests[0]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[1]}, it would be a pleasure to have you join us for dinner.")
print(f"Dear {guests[2]}, your presence at dinner tonight would be an absolute honor.")

# Tamu yang tidak bisa hadir
cant_make_it = guests[1]
print(f"\nUnfortunately, {cant_make_it} cannot make it to dinner.")

# Mengganti tamu dengan orang baru
guests[1] = "Calya"

# Undangan babak kedua
print("\nSecond set of invitations:")
print(f"Dear {guests[0]}, I would be deeply honored to invite you to dinner.")
print(f"Dear {guests[1]}, it would be a pleasure to have you join us for dinner.")
print(f"Dear {guests[2]}, your presence at dinner tonight would be an absolute honor.")