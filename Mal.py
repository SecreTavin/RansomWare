import os

#arquivos a criptografar

username = os.getenv("USERNAME")
folders = [
    os.path.join(r"C:\Users" , username, "Documents")
    os.path.join(r"C:\Users" , username, "Pictures")
    os.path.join(r"C:\Users" , username, "Videos")
    os.path.join(r"C:\Users" , username, "Downloads")
    os.path.join(r"C:\Users" , username, "AppData", "Local")
    os.path.join(r"C:\Users" , username, "AppData", "Roaming")
    ]
arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        arquivos.append(root)
        arquivos.append(dirs)
        arquivos.append(files)

print(arquivos)


