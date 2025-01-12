# Calcul de la Somme d'Étalonnage

Ce projet contient un script Python permettant de calculer la somme d'étalonnage à partir d'un fichier hébergé sur Google Drive. Le script télécharge le fichier, traite son contenu et calcule la somme en extrayant et combinant le premier et le dernier chiffre de chaque ligne.

## Comment ça fonctionne ?
Le script effectue les étapes suivantes :
1. Télécharge un fichier à partir d'une URL Google Drive.
2. Lit le contenu du fichier ligne par ligne.
3. Extrait le premier et le dernier caractère numérique (chiffres) de chaque ligne.
4. Combine ces chiffres pour former un nombre à deux chiffres et l’ajoute à un total cumulatif.
5. Affiche la somme totale des valeurs d'étalonnage.

### Exemple :
Pour un fichier contenant les lignes suivantes :
1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet


Les valeurs d'étalonnage sont :
- `12` (à partir de `1` et `2`)
- `38` (à partir de `3` et `8`)
- `15` (à partir de `1` et `5`)
- `77` (à partir de `7` et `7`)

**Somme totale = 12 + 38 + 15 + 77 = 142.**

## Prérequis
- Python 3.6 ou une version ultérieure
- Bibliothèque `requests` (pour effectuer les requêtes HTTP)

## Installation
1. Clonez le dépôt :

   git clone https://github.com/your-username/calculate-somme-etalonnage.git
Accédez au répertoire du projet :

cd calculate-somme-etalonnage
Installez la bibliothèque nécessaire :

pip install requests