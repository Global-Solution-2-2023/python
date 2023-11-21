import json
from time import sleep

# with open("dados.json", "r") as dados_json:
#     dados_py = json.load(dados_json)

# skills_db = dados_py["Skills"]
# skills_classes_escolhidas = {}

# for skill, classe in skills_db.items():
#     cont = 0

#     for nome_classe, nome_subclasse in classe.items():
#         cont+=1
#         print(cont)
#         print()
#         print(nome_classe)
#         print(nome_subclasse)
#         print()

# with open("dados.json", "r") as dados_json:
#     dados_py = json.load(dados_json)

# usuario_logado = "admin"

# usuario_logado_db = dados_py["Usuarios"][usuario_logado]
# missoes_db = usuario_logado_db["Missoes em Andamento"]

# for missao_nome_classe, missao_info_total in missoes_db.items():
#     sleep(1)
#     print(f'{missao_nome_classe}')


#     for missao_numero, missao_info in missao_info_total.items():
#         sleep(1)
#         print(f'\nMissão {missao_numero}')
        
#         for missao_info_chave, missao_info_valor in missao_info.items():
#             sleep(1)

#             if isinstance(missao_info_valor, dict):
#                 print(f'\n{missao_info_chave}:')
                    
#                 for recompensa_chave, recompensa_valor in missao_info_valor.items():
#                     print(f'- {recompensa_chave}: {recompensa_valor}')
                
#             else:
#                 print(f'\n{missao_info_chave}: {missao_info_valor}')
                    

a = {1:"z", 2: "y", "gb":{3.1: "b"}}

# a[0] = 8

# b = {"aaa":{1: {"k":"l"}}}

if a["gb"].values() == 3.1:
    print("Sim")