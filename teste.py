import json
from time import sleep

with open("dados.json", "r") as dados_json:
    dados_py = json.load(dados_json)

skills_db = dados_py["Skills"]
skills_classes_escolhidas = {}

for skill, classe in skills_db.items():
    cont = 0

    for nome_classe, nome_subclasse in classe.items():
        cont+=1
        print(cont)
        print()
        print(nome_classe)
        print(nome_subclasse)
        print()