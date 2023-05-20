import re

def clean_text(text):
    # Suppression des caractères spéciaux et de la ponctuation
    cleaned_text = re.sub(r"[^a-zA-Z0-9À-ÿ\s]", "", text)
    
    # Conversion en minuscules
    cleaned_text = cleaned_text.lower()
    
    # Suppression des mots vides (stop words)
    stopwords = ["le", "de", "et", "la", "les"]  # Exemple de liste de mots vides
    cleaned_text = " ".join(word for word in cleaned_text.split() if word not in stopwords)
    
    # Normalisation - Lemmatisation ou racinisation (stemming)
    # Ici, nous n'ajoutons pas de code spécifique pour la lemmatisation ou la racinisation,
    # mais vous pouvez utiliser des bibliothèques comme NLTK ou SpaCy pour ces tâches.
    
    return cleaned_text

# Fonction pour nettoyer le fichier
def clean_file(file_path, output_file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    cleaned_lines = [clean_text(line) for line in lines]
    
    # Écriture des lignes nettoyées dans le fichier de sortie
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.writelines(cleaned_lines)

# Exemple d'utilisation
file_path = "fra.txt"
output_file_path = "cleaned_fra.txt"

clean_file(file_path, output_file_path)