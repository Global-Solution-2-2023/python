import json
from time import sleep

with open("dados.json", "r") as dados_json:
    dados_py = json.load(dados_json)

# usuarios = dados_py["usuarios"]

# for k1, v1 in usuarios.items():
#     print()
#     print(f'Usuário: {k1}')

#     for k2, v2 in v1.items():
#         print()
#         print(f'{k2}: {v2}')

print('[1] - LUTA')
print('[2] - CORREDOR')
print('[3] - ACADEMIA')

escolha_usuario = int(input('Qual classe você gostaria de ver as missões?'))

match escolha_usuario:
    case 1:
        escolha_usuario = 'luta'
    case 2:
        escolha_usuario = 'corredor'
    case 3:
        escolha_usuario = 'academia'

missoes = dados_py["missoes"]

for k1, v1 in missoes.items():
    print()
    if k1 == escolha_usuario:
        sleep(1)
        print(f"Classe: {k1}")

        for k2, v2 in v1.items():
            sleep(1)
            print()
            print(f'Missão {k2}')

            for k3, v3 in v2.items():
                sleep(1)
                print()
                print(f'- {k3}: {v3}')
