
import numpy as np

# Simulerad data: Pichu och Pikachu (längd, bredd)
pichu_data = np.array([[20, 34], [19, 33], [18, 32], [19, 35], [21, 33]])
pikachu_data = np.array([[25, 32], [24.2, 31.5], [22, 34], [20.5, 34], [23, 33]])

# Funktion för att avgöra klassen för en testpunkt baserat på majoritetsröstning bland de närmaste punkterna
def classify_test_point(test_point, k=10):
    try:
        # Konvertera användarens input till en numpy-vektor
        test_point = np.array(test_point)
        
        # Kontrollera om det är ett negativt tal
        if np.any(test_point < 0):
            raise ValueError("Testpunktens koordinater får inte vara negativa.")
        
        # Beräkna avståndet mellan testpunkten och alla Pichu- och Pikachu-punkter
        distances_pichu = np.linalg.norm(pichu_data - test_point, axis=1)
        distances_pikachu = np.linalg.norm(pikachu_data - test_point, axis=1)
        
        # Kombinera avstånden och sortera dem för att få de närmaste punkterna
        all_distances = np.concatenate((distances_pichu, distances_pikachu))
        sorted_indices = np.argsort(all_distances)
        nearest_indices = sorted_indices[:k]
        
        # Räkna majoritetsröstningen
        votes_pichu = np.sum(nearest_indices < len(pichu_data))
        votes_pikachu = k - votes_pichu
        
        # Avgör klassen baserat på majoritetsröstningen
        if votes_pichu > votes_pikachu:
            return "Testpunkten tillhör Pichu"
        elif votes_pikachu > votes_pichu:
            return "Testpunkten tillhör Pikachu"
        else:
            return "Det är en oavgjord majoritetsröstning mellan Pichu och Pikachu."
    
    except ValueError as e:
        return str(e)
    except Exception as e:
        return "Ett fel uppstod: " + str(e)

# Låt användaren mata in en testpunkt
try:
    test_point = input("Ange en testpunkt som ett kommaseparerat par av längd och bredd (t.ex., 22,33): ").split(',')
    test_point = [float(coord.strip()) for coord in test_point]
    
    result = classify_test_point(test_point)
    print(result)
except ValueError as e:
    print("Felaktig input:", e)
except KeyboardInterrupt:
    print("\nAvslutade programmet.")
except Exception as e:
    print("Ett fel uppstod:", e)