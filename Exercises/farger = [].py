farger = []

while True:
    farg = input("Ange en färg (lämna tom för att avsluta): ")
    if not farg:
        break  # Avsluta loopen om användaren inte anger någon färg
    farger.append(farg)

# Skriv ut listan med färger
print("Färger i listan:")
for farg in farger:
    print(farg)

# Skriv ut antalet färger i listan
print("Antal färger i listan:", len(farger))
