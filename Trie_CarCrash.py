import csv
import os
import shutil

def read_csv_with_selection(file_path):
    try:
        # Ouvrir le fichier CSV
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            # Lire l'en-tête
            header = next(reader)
            print("Colonnes disponibles :")
            for idx, column_name in enumerate(header):
                print(f"{idx}: {column_name}")

            # Lire et analyser les données pour trouver les colonnes avec '1'
            print("\nAnalyse du fichier CSV :")
            result = []
            for row_idx, row in enumerate(reader):
                columns_with_ones = [idx for idx, value in enumerate(row) if value == '1']
                result.append(columns_with_ones)
                print(f"Ligne {row_idx}: {columns_with_ones}")
            
            print("\nRésultat final :")
            print(result)

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


def copy_images_to_directory(image_folder, result, output_directory):
    try:
        for row_idx, columns in enumerate(result):
            for col_idx in columns:
                image_name = f"C_{row_idx+1:06}_{col_idx}.jpg"  # Décalage de 1 pour les lignes et colonnes
                source_path = os.path.join(image_folder, image_name)
                destination_path = os.path.join(output_directory, image_name)
                
                if os.path.exists(source_path):
                    shutil.copy(source_path, destination_path)
                    print(f"Image '{image_name}' copiée dans '{output_directory}'.")
                else:
                    print(f"Image '{image_name}' introuvable dans '{image_folder}'.")
    except Exception as e:
        print(f"Erreur lors de la copie des images : {e}")



# Exemple d'utilisation
file_path = 'Crash_Table.csv'
result = read_csv_with_selection(file_path)
# create_directory("Carcrash_Trie")
copy_images_to_directory(
    "c:/Users/malam/Documents/2 - ECOLE/HENALLUX VIRTON/M1 - INGENIEUR INDUSTRIEL AUTOMATION/13 - SYSTEMES INTELLIGENTS/Carcash/CrashBest", 
    result, 
    "c:/Users/malam/Documents/2 - ECOLE/HENALLUX VIRTON/M1 - INGENIEUR INDUSTRIEL AUTOMATION/13 - SYSTEMES INTELLIGENTS/Carcash/Crashcar_Trie"
)
