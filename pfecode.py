import requests

def calculate_somme_étalonnage(file_url):
    response = requests.get(file_url)
    response.raise_for_status()
    lines = response.text.splitlines()
    total = 0

    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])

    return total

file_id = "12iJW2aaHCdOGBXw_PZPnnzzxbUf3JE8u"
file_url = f"https://drive.google.com/uc?id={file_id}&export=download"

try:
    print("La somme des valeurs d'étalonnage est :", calculate_somme_étalonnage(file_url))
except Exception as e:
    print("Erreur :", e)
