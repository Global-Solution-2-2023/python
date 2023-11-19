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

# print('[1] - LUTA')
# print('[2] - CORREDOR')
# print('[3] - ACADEMIA')

# escolha_usuario = int(input('Qual classe você gostaria de ver as missões?'))

# match escolha_usuario:
#     case 1:
#         escolha_usuario = 'luta'
#     case 2:
#         escolha_usuario = 'corredor'
#     case 3:
#         escolha_usuario = 'academia'

# missoes = dados_py["missoes"]

# for k1, v1 in missoes.items():
#     print()
#     if k1 == escolha_usuario:
#         sleep(1)
#         print(f"Classe: {k1}")

#         for k2, v2 in v1.items():
#             sleep(1)
#             print()
#             print(f'Missão {k2}')

#             for k3, v3 in v2.items():
#                 sleep(1)
#                 print()
#                 print(f'- {k3}: {v3}')

skills_db = dados_py["Skills"]

validar_cadastro_skill = False
validar_cadastro_skill_continuar = True

print()
print(f'{f"Agora é hora de escolher as suas Skills!":^50}')
print()

for skill, classe in skills_db.items():

    skills_classe_escolhidas = []
    skill_classes_disponiveis = []

    for nome_classe in classe.keys():
        # Adicionando classes na lista de classes disponíveis
        skill_classes_disponiveis.append(nome_classe)

    print(f'{f"Skills relacionadas a {skill}:":^50}')

    if skill == "Saude Fisica":


        while not validar_cadastro_skill:

            cont_skill = 0
            print()

            for nome_classe in range(0, len(skill_classes_disponiveis)):

                # Contador para printar número das skills
                cont_skill += 1
                print(f'[{cont_skill}] - {skill_classes_disponiveis[cont_skill-1]}')

            try:
                # Input da escolha da skill
                skill_classe_input_cadastro = int(input('\nQual Classe você deseja escolher? (1 por vez) '))

                # Se não estiver fora das opções oferecidas

                if cont_skill >= skill_classe_input_cadastro > 0:
                    cont_skill_escolhida = 0

                    for nome_classe in classe.keys():


                        # Se a classe escolhida pelo input dentro da lista de classes disponíveis for igual ao nome da classe atual no loop
                        if skill_classes_disponiveis[skill_classe_input_cadastro - 1] == nome_classe:

                            # Adicionar classe escolhida na lista de classes escolhidas
                            skills_classe_escolhidas.append(nome_classe)

                            # Remover classe escolhida na lista de classes disponíveis
                            skill_classes_disponiveis.remove(nome_classe)

                            print(f'\nClasse {nome_classe} adicionada com sucesso!')

                            # Ir para a pergunta de continuar escolhendo ou não 
                            validar_cadastro_skill_continuar = False

                            break

                            # Contador para saber quantas skills foram scolhidas
                            cont_skill_escolhida += 1
                        
                        # Se o tamanho das skills escolhidas for igual a quantidade de skills, excluindo a "não praticante"
                        if len(skill_classes_disponiveis) - 1 == 1:
                            print(f'\nTodas as Classes de {skill} foram selecionadas\n')
                            validar_cadastro_skill = True
                            break
                        
                        # Se a skill escolhida fo igual a classe "não praticante"
                        elif skill_classe_input_cadastro == cont_skill:
                            print('NAO PRATICANTE ESCOLHIDO')
                            validar_cadastro_skill = True
                            break
                
                else:
                    raise ValueError

            except:
                # Erro
                print('\nErro! Digite uma opção válida!\n')

    	    
            while not validar_cadastro_skill_continuar:
                
                try:
                    # Continuar escolha? 
                    continuar_skill_input = int(input('\nDeseja escolher mais uma skill? [1 - Sim | 2 - Não] '))

                    # Se estiver fora das opções oferecidas
                    match continuar_skill_input:
                        case 1: # escolher mais skill
                            validar_cadastro_skill_continuar = True
                        
                        case 2:
                            validar_cadastro_skill_continuar = True
                            validar_cadastro_skill = True

                        case _:
                            raise ValueError

                except:
                    # Erro
                    print('\nErro! Digite uma opção válida!\n')

                match continuar_skill_input:
                    case 1:

                        continue

                    case 2:
                        break

