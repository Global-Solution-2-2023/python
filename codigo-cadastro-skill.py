import json
from time import sleep
import funcoes as f

with open("dados.json", "r") as dados_json:
    dados_py = json.load(dados_json)

skills_db = dados_py["Skills"]
skills_classes_escolhidas = {}

print()
print(f'{f"Agora é hora de escolher as suas Skills!":^50}')
print()

for skill, classe in skills_db.items(): # skill -> Saude X  |  classe -> { classe : } (ex: { Atleta de Academia, Corredor, Lutador })
    validar_cadastro_skill = False
    validar_cadastro_skill_continuar = True

    skills_classes_escolhidas[skill] = {}
    skills_classes_disponiveis = []
    cont_skill_escolhida = 0

    for nome_classe_adicionar in classe.keys(): # nome_classe_adicionar -> Nome da Classe (ex: Atleta de Academia, Corredor, Lutador)
        # Adicionando classes na lista de classes disponíveis
        skills_classes_disponiveis.append(nome_classe_adicionar)

    print(f'\n\033[36m{f"Skills relacionadas a {skill}":^50}\033[m')
    f.linha()

    while not validar_cadastro_skill: 

        cont_skill = 0
        print()

        for i in range(0, len(skills_classes_disponiveis)):

            # Contador para printar número das skills
            cont_skill += 1
            print(f'[{cont_skill}] - {skills_classes_disponiveis[cont_skill-1]}')

            # Opção de Sair
            if cont_skill == len(skills_classes_disponiveis) and cont_skill_escolhida > 0:
                print(f'[{cont_skill+1}] - Não Desejo Escolher Mais')

        print()  
        f.linha()

        try:
            # Input da escolha da skill
            skill_classe_input_cadastro = int(f.inputSublinhado('\nQual Classe você deseja escolher? (1 por vez) '))

            # Se não estiver fora das opções oferecidas

            if cont_skill >= skill_classe_input_cadastro > 0:
                # nome da classe escolhida
                nome_classe_escolhida = skills_classes_disponiveis[skill_classe_input_cadastro - 1]

                cont = 0

                for nome_classe, nome_subclasse in classe.items(): # nome_classe -> Nome da Classe (ex: Corredor)  |  Subclasse da Classe com intervalo de nivel e nome (ex: "1 - 10": "Base firme")
                    cont+=1
                    
                    # Se a classe escolhida for igual ao nome da classe atual no loop ALTERAR ISSO, ESTA DANDO ERRO
                    if nome_classe_escolhida == nome_classe:

                        # Adicionar classe escolhida na lista de classes escolhidas
                        skills_classes_escolhidas[skill].update({nome_classe : {"Nivel": 1,"Subclasse": next(iter(nome_subclasse.values()))},})

                        # Remover classe escolhida na lista de classes disponíveis
                        skills_classes_disponiveis.remove(nome_classe) 

                        print(f'\n\033[32m{f"Classe {nome_classe} adicionada com sucesso!":^50}\033[m')

                        # Ir para a pergunta de continuar escolhendo ou não 
                        validar_cadastro_skill_continuar = False

                        # Contador para saber quantas skills foram scolhidas
                        cont_skill_escolhida += 1

                        if cont_skill_escolhida == 1:
                            skills_classes_disponiveis.remove('Nao Praticante')

                        # Se o tamanho das skills escolhidas for igual a quantidade de skills, excluindo a "não praticante"
                        if len(skills_classes_disponiveis) == 0:
                            print(f'\n\033[32m{f"Todas as Classes de {skill} foram selecionadas.":^50}\033[m\n')
                            validar_cadastro_skill = True
                            validar_cadastro_skill_continuar = True

                        break
                    
                    # Se a skill escolhida fo igual a classe "não praticante"
                    elif skill_classe_input_cadastro == cont_skill:

                        if "Nao Praticante" in skills_classes_disponiveis:

                            # Adicionar classe escolhida na lista de classes escolhidas
                            skills_classes_escolhidas[skill].update({"Nao Praticante":"Nao praticante (ainda)"}) 

                            print(f'\n{f"Classe {skills_classes_disponiveis[-1]} adicionada com sucesso!":^50}')

                            validar_cadastro_skill = True
                            break
            
            elif skill_classe_input_cadastro == cont_skill  + 1 and cont_skill_escolhida > 0:
                print('\n\033[32mOpção Não Desejo Escolher Mais selecionada com sucesso!\033[m\n')
                validar_cadastro_skill = True

            else:
                raise ValueError

        except:
            # Erro
            print('\nErro! Digite uma opção válida!\n')
        
        while not validar_cadastro_skill_continuar:
            
            try:
                sleep(0.5)
                # Continuar escolha? 
                print(f'\nVocê ainda pode escolher mais \033[32m{len(skills_classes_disponiveis)}\033[m skills de \033[36m{skill}\033[m.')
                print('\033[33m')
                continuar_skill_input = int(input(f'Deseja escolher mais uma skill? [1 - Sim | 2 - Não] '))
                print('\033[m')
                sleep(0.5)

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
                print('\n\033[31mErro! Digite uma opção válida!\033[m\n')

print('\n')

print(skills_classes_escolhidas.items())

for k, v in skills_classes_escolhidas.items():
    sleep(1)
    print()
    print(f'----------- {k} -----------')
    for k2, v2 in v.items():
        sleep(0.3)
        print(f'\n{k2}:')

        sleep(0.3)
        if isinstance(v2, dict):
            for k3, v3 in v2.items():
                print(f'- {k3}: {v3}')
                sleep(0.3)
        else:
            print(f'- {v2}')
        print()

