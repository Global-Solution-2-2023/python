import json
from time import sleep

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

    print(f'\n{f"Skills relacionadas a {skill}:":^50}')

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


        try:
            # Input da escolha da skill
            skill_classe_input_cadastro = int(input('\nQual Classe você deseja escolher? (1 por vez) '))

            # Se não estiver fora das opções oferecidas

            if cont_skill >= skill_classe_input_cadastro > 0:
                # nome da classe escolhida
                nome_classe_escolhida = skills_classes_disponiveis[skill_classe_input_cadastro - 1]

                cont = 0

                for nome_classe, nome_subclasse in classe.items(): # nome_classe -> Nome da Classe (ex: Corredor)  |  Subclasse da Classe com intervalo de nivel e nome (ex: "1 - 10": "Base firme")
                    cont+=1
                    print(cont)
                    sleep(0.5)
                    print(f"\nNome classe do loop: {nome_classe}")
                    sleep(0.5)
                    print(f"Nome classe escolhida: {nome_classe_escolhida}\n")
                    sleep(0.5)
                    
                    # Se a classe escolhida for igual ao nome da classe atual no loop ALTERAR ISSO, ESTA DANDO ERRO
                    if nome_classe_escolhida == nome_classe:

                        # Adicionar classe escolhida na lista de classes escolhidas
                        skills_classes_escolhidas[skill].update({nome_classe : {"Nivel": 1,"Subclasse": next(iter(nome_subclasse.values()))},})

                        # Remover classe escolhida na lista de classes disponíveis
                        skills_classes_disponiveis.remove(nome_classe) 


                        print(f'\nClasse {nome_classe} adicionada com sucesso!')

                        # Ir para a pergunta de continuar escolhendo ou não 
                        validar_cadastro_skill_continuar = False

                        # Contador para saber quantas skills foram scolhidas
                        cont_skill_escolhida += 1

                        if cont_skill_escolhida == 1:
                            skills_classes_disponiveis.remove('Nao Praticante')
                        
                        print(skills_classes_disponiveis)

                        break

                    # Se o tamanho das skills escolhidas for igual a quantidade de skills, excluindo a "não praticante"
                    if len(skills_classes_disponiveis) == 0:
                        print(f'\nTodas as Classes de {skill} foram selecionadas\n')
                        validar_cadastro_skill = True
                        break
                    
                    # Se a skill escolhida fo igual a classe "não praticante"
                    elif skill_classe_input_cadastro == cont_skill:

                        # Adicionar classe escolhida na lista de classes escolhidas
                        skills_classes_escolhidas[skill].update({"Nao Praticante":"Nao praticante (ainda)"}) 

                        print(f'\nClasse {skills_classes_disponiveis[-1]} adicionada com sucesso!')

                        validar_cadastro_skill = True
                        break
            
            elif skill_classe_input_cadastro == cont_skill  + 1 and cont_skill_escolhida > 0:
                print('\nOpção Não Desejo Escolher Mais selecionada com sucesso!\n')
                validar_cadastro_skill = True

            else:
                raise ValueError

        except:
            # Erro
            print('\nErro! Digite uma opção válida!\n')
        
        while not validar_cadastro_skill_continuar:
            
            try:
                # Continuar escolha? 
                continuar_skill_input = int(input(f'\nVocê ainda pode escolher mais {len(skills_classes_disponiveis)} skills.\nDeseja escolher mais uma skill? [1 - Sim | 2 - Não] '))

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

print('\n')

for k, v in skills_classes_escolhidas.items():
    sleep(1)
    print()
    print(f'----------- {k} -----------')
    for k2, v2 in v.items():
        sleep(1)
        print(f'\n{k2}:')

        sleep(1)
        if isinstance(v2, dict):
            for k3, v3 in v2.items():
                print(f'- {k3}: {v3}')
                sleep(1)
        else:
            print(f'- {v2}')
        print()

