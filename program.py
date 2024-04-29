import os
import shutil
folder_name = "JECRC"
os.makedirs(folder_name, exist_ok=True)
source_folder = "JECRC"
files_to_move = os.listdir("d:\Data Science ML & AI")
for file_name in files_to_move:
    if file_name.endswith((".jpg", ".jpeg", ".png")):
        shutil.move(os.path.join(source_folder, file_name), os.path.join(folder_name, file_name))
    elif file_name.endswith(".txt"):
        shutil.move(os.path.join(source_folder, file_name), os.path.join(folder_name, file_name))
    elif file_name.endswith(".pdf"):
        shutil.move(os.path.join(source_folder, file_name), os.path.join(folder_name, file_name))
image_folder = "image_folder"
text_folder = "text_folder"
pdf_folder = "pdf_folder"
os.makedirs(image_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)
files_in_JECRC = os.listdir(folder_name)
for file_name in files_in_JECRC:
    if file_name.endswith((".jpg", ".jpeg", ".png")):
        shutil.move(os.path.join(folder_name, file_name), os.path.join(image_folder, file_name))
    elif file_name.endswith(".txt"):
        shutil.move(os.path.join(folder_name, file_name), os.path.join(text_folder, file_name))
    elif file_name.endswith(".pdf"):
        shutil.move(os.path.join(folder_name, file_name), os.path.join(pdf_folder, file_name))

print("Files moved successfully.")
