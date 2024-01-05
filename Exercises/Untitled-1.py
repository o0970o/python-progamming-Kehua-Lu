import re
from colorama import Fore, Style, init

# Aktivera colorama
init(autoreset=True)

def hitta_och_markera_korrekta_tal(text):
    # Använd ett reguljärt uttryck för att hitta alla korrekta tal i texten
    pattern = r'\b(\d)(\d*?)\1\b'
    matches = re.finditer(pattern, text)

    for match in matches:
        korrekt_tal = match.group()
        start_index = match.start()
        end_index = match.end()

        # Byt textfärg till röd för den markerade delsträngen
        markerad_text = (
            text[:start_index]
            + Fore.RED
            + Style.BRIGHT
            + text[start_index:end_index]
            + Style.RESET_ALL
            + text[end_index:]
        )

        # Skriv ut hela strängen med markerad delsträng
        print(markerad_text)

if __name__ == "__main__":
    text = input("Ange en textsträng: ")
    hitta_och_markera_korrekta_tal(text)
