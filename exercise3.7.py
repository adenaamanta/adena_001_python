guests = ["Calya", "Alicia", "James", "Adena", "Amanta", "Louis"]

print("Initial invitations were sent to 6 guests.")

print("\nUnfortunately, the new dinner table won't arrive in time, so I can invite only two people for dinner.\n")

# Menghapus tamu satu per satu menggunakan pop() hingga tersisa dua nama
popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I'm sorry that I can't invite you to dinner.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I'm sorry that I can't invite you to dinner.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I'm sorry that I can't invite you to dinner.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I'm sorry that I can't invite you to dinner.")

# Pesan kepada dua tamu yang masih tersisa
print(f"\nDear {guests[0]}, you are still invited to dinner!")
print(f"Dear {guests[1]}, you are still invited to dinner!")

# Menghapus dua tamu terakhir menggunakan del sehingga list kosong
del guests[1]
del guests[0]

# Memastikan list benar-benar kosong
print("\nFinal guest list:")
print(guests)