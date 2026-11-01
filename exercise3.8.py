places = ["Tokyo", "Paris", "Cairo", "Hawaii", "New York"]

print("Original order:")
print(places)

print("\nAlphabetical order (sorted):")
print(sorted(places))

print("\nOriginal order check:")
print(places)

print("\nReverse-alphabetical order (sorted):")
print(sorted(places, reverse=True))

print("\nOriginal order check:")
print(places)

print("\nReversed order (reverse):")
places.reverse()
print(places)

print("\nBack to original order (reverse):")
places.reverse()
print(places)

print("\nPermanent alphabetical order (sort):")
places.sort()
print(places)

print("\nPermanent reverse-alphabetical order (sort):")
places.sort(reverse=True)
print(places)