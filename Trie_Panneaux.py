import csv
import os
import shutil

def read_csv_with_selection(file_path):
    try:
        # Ouvrir le fichier CSV
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Compter le nombre de lignes
            line_count = sum(1 for row in reader)
            print(f"Nombre de lignes dans le fichier : {line_count}")
            result = line_count

    except Exception as e:
        print(f"Erreur : {e}")

    return result


def create_directory(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            print(f"Dossier '{directory_name}' créé")
        else:
            print(f"Le dossier '{directory_name}' existe déjà.")
    except Exception as e:
        print(f"Erreur création dossier : {e}")


def delete_rows_invalid(csv_file, image_folder):
    try:
        # Lire le fichier CSV
        with open(csv_file, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        # Vérifier chaque ligne
        valid_rows = []
        for row in rows:
            if len(row) > 0:  # Vérifier si la ligne n'est pas vide
                image_name = row[0]  # Nom de l'image dans la première colonne
                image_path = os.path.join(image_folder, image_name)
                if os.path.isfile(image_path):  # Vérifier si l'image existe
                    valid_rows.append(row)

        # Réécrire le fichier CSV avec les lignes valides
        with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(valid_rows)

        print("Les lignes invalides ont été supprimées.")
    except Exception as e:
        print(f"Erreur : {e}")



# Exemple d'utilisation
file_path = '_classes2.csv'
image_folder = r'C:\Users\malam\Documents\2 - ECOLE\HENALLUX VIRTON\M1 - INGENIEUR INDUSTRIEL AUTOMATION\13 - SYSTEMES INTELLIGENTS\Self-Driving Cars.v6-version-4-prescan-416x416.multiclass\train'
csv_file = '_classes2.csv'
result = read_csv_with_selection(file_path)
# create_directory("Carcrash_Trie")
delete_rows_invalid(csv_file, image_folder)
