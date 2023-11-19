# --------------------- Instruções ---------------------
'''
- Implementar um menu de opções com as principais funcionalidades oferecidas pelo sistema.
- Realizar validações nas entradas de dados do usuário.
- Aplicar adequadamente o tratamento de exceções.
- Utilizar estruturas de decisão e repetição.
- Utilizar funções com passagem de parâmetros e retorno.
- Utilizar dicionários e arquivos como bancos de dados.
'''

# --------------------- Imports ---------------------

import json
import funcoes as f
import random
from time import sleep

# ---------- Dados ---------- #

menu_inicial = {
    1 : "Login",
    2 : "Cadastro",
    0 : "Sair"
}

menu_principal = {
    1 : "Personagem",
    2 : "Missões",
    3 : "Ajuda",
    0 : "Sair"
}

menu_missoes = {}

menu_personagem = {
    1 : "Informações da Conta",
    2 : "Skills",
    0 : "Voltar para Menu Principal",
}

menu_ajuda = {
    1 : "Para que serve uma vida saudável?",
    2 : "Pergunta 2",
    3 : "Pergunta 3",
    4 : "Pergunta 4",
    5 : "Pergunta 5",
    0 : "Voltar para o Menu Principal"
}

respostas_ajuda = ["Para ter mais saúde.", "Resposta 2", "Resposta 3", "Resposta 4", "Resposta 5"]


# --------------------- Programa Principal ---------------------

# ---------- Variáveis ---------- 

tamanho_do_programa = f.tamProg('Aplicativo Programa X')
usuario_logado = 'admin'

# ------ Variáveis de controle dos while ------

# Menus
encerrar_programa = False
encerrar_menu_inicial = True
encerrar_menu_personagem = False
encerrar_menu_personagem_informacoes = False
encerrar_menu_missoes = False
encerrar_menu_ajuda = False

# Validação
validar_login = False
validar_cadastro_info = False
validar_cadastro_skill = False

# Constantes
with open("dados.json", "r") as dados_json:
    dados_py = json.load(dados_json)

skills_db = dados_py["Skills"]
missoes_db = dados_py["Missoes"]
nivel_min = 1
nivel_max = 30

# ---------- Loop do Programa ---------- 

while not encerrar_programa:

    print()
    f.linha(tamanho_do_programa//2, '=-')
    print(f'\n\033[32m{"Aplicativo Programa X":^{tamanho_do_programa}}\033[m\n')
    f.linha(tamanho_do_programa//2, '=-')
    print()

    # # SIMULAR NIVEL DO ADMIN NA SKILL 
    # # ----- Leitura do arquivo JSON -----
    # with open("dados.json", "r") as dados_json:
    #     dados_py = json.load(dados_json)

    # usuarios_db = dados_py["Usuarios"]

    # # Calcular nível da Skill Corredor do usuário admin
    # nivel_admin_corredor = random.randint(nivel_min, nivel_max)

    # usuarios_db["admin"]["Skills"]["Corredor"]["Nivel"] = nivel_admin_corredor

    # if nivel_admin_corredor <= 10:
    #     usuarios_db["admin"]["Skills"]["Corredor"]["Subclasse"] = 'Passo inicial'
    # elif 10 < nivel_admin_corredor <= 20:
    #     usuarios_db["admin"]["Skills"]["Corredor"]["Subclasse"] = 'Ritmo Crescente'
    # else:
    #     usuarios_db["admin"]["Skills"]["Corredor"]["Subclasse"] = 'Vento nas coxas'

    # # ----- Dump para o arquivo JSON -----
    # with open("dados.json", "w") as dados_json:
    #     json.dump(dados_py, dados_json)


    # ----- Login | Cadastro -----

    while not encerrar_menu_inicial:

        escolha_inicial = f.printMenu("Inicial", menu_inicial)

        match escolha_inicial:
            case 1: # Login

                while not validar_login:

                    f.aviso('    Login    ', tresPontos='')

                    print(f'\033[36m{f"Login":^{tamanho_do_programa}}\033[m')
                    f.linha()
                    print()
                    usuario_input_login = input('\033[33mDigite o seu usuário: \033[m')
                    print()
                    senha_input_login = input('\033[33mDigite a sua senha: \033[m')
                    print()
                    f.linha()

                    # Verificar os inputs
                    for usuario, valores in usuarios_db.items():

                        # se o usuario do json e a senha do json for igual aos inputs
                        if valores['Usuario'] == usuario_input_login and valores['Senha'] == senha_input_login:
                            print()
                            f.aviso(' Login concluído com sucesso!', tresPontos='')
                            usuario_logado = usuario_input_login
                            encerrar_menu_inicial = True 
                            validar_login = True

                        else:
                            print()
                            f.aviso(' Erro no login. Tente novamente.', tresPontos='')
            
            case 2: # Cadastro

                # ----- Leitura do arquivo JSON -----
                with open("dados.json", "r") as dados_json:
                    dados_py = json.load(dados_json)

                usuarios_db = dados_py["Usuarios"]

                f.aviso('    Cadastro    ', tresPontos='')

                # ----- Cadastro das informações de login do usuário -----

                while not validar_cadastro_info:

                    print()
                    print(f'\033[36m{f"Insira suas informações pessoais":^{tamanho_do_programa}}\033[m')
                    f.linha()
                    print()
                    email_input_cadastro = input('\033[33mEmail: \033[m')
                    print()
                    usuario_input_cadastro= input('\033[33mUsuário: \033[m')
                    print()
                    senha_input_cadastro = input('\033[33mSenha: \033[m')
                    print()
                    f.linha()

                    # Verificar se o usuário já existe
                    usuario_existente = False

                    for usuario, valores in usuarios_db.items():

                        # Verificação de email e usuário
                        if valores['Email'] == email_input_cadastro:
                            print()
                            f.aviso(' Erro! Email já cadastrado', tresPontos='')
                            usuario_existente = True
                            break

                        elif valores['Usuario'] == usuario_input_cadastro:
                            print()
                            f.aviso(' Erro! Usuário já cadastrado', tresPontos='')
                            usuario_existente = True
                            break

                    if not usuario_existente:

                        print()
                        f.aviso(' Cadastro das suas informações realizado com sucesso!', tresPontos='')

                        validar_cadastro_info = True

                while not validar_cadastro_skill:

                    f.linha()
                    
                    
                    f.linha()

                # Novo usuário que será adicionado
                novo_usuario = {
                    "Email": email_input_cadastro,
                    "Usuario": usuario_input_cadastro,
                    "Senha": senha_input_cadastro,
                    "Skills": "",
                    "Missoes em Andamento": ""
                }

                usuarios_db[usuario_input_cadastro] = novo_usuario

                # ----- Dump para o arquivo JSON -----
                with open("dados.json", "w") as dados_json:
                    json.dump(dados_py, dados_json)


            case 0: # Sair do programa
                encerrar_programa = True
                encerrar_menu_inicial = True

    if not encerrar_programa: # se usuário não quiser sair no Menu Inicial

        usuario_logado_db = dados_py["Usuarios"][usuario_logado] # Carregar dados json do usuário logado

        print()
        print(f'\033[33m{f"Seja bem-vindo {usuario_logado}!":^{tamanho_do_programa}}\033[m')
        print()

        # Menu Principal
        escolha_principal = f.printMenu("Principal", menu_principal)

        match escolha_principal:
            case 1: # Personagem

                while not encerrar_menu_personagem:
                    escolha_personagem = f.printMenu("Personagem", menu_personagem)

                    # Se quiser voltar para o Menu Principal
                    if escolha_personagem == 0:
                        encerrar_menu_personagem = True
                    
                    # Se não
                    else:

                        encerrar_menu_personagem_informacoes = {}

                        escolha_informacoes = f.printMenu("Informações da Conta", encerrar_menu_personagem_informacoes)

                        while not encerrar_menu_personagem_informacoes:

                            print()

            case 2: # Missões
                missoes_em_andamento_db = usuario_logado_db["Missoes em Andamento"]

                cont_menu_missoes = 0

                # Para cada Classe em Missoes em Andamento
                for missoes_classes in missoes_em_andamento_db.keys(): 
                    # Numero de missoes:
                    cont_menu_missoes += 1
                    # Adicionar cada Classe no Menu Missoes
                    menu_missoes[cont_menu_missoes] = missoes_classes

                # Adicionar opção de Voltar para o Menu Principal
                menu_missoes[0] = "Voltar para Menu Principal"

                while not encerrar_menu_missoes:

                    escolha_missoes = f.printMenu("Missões", menu_missoes)

                    # Se quiser voltar para o Menu Principal
                    if escolha_missoes == 0:
                        encerrar_menu_missoes = True
                    
                    # Se não
                    else:
            
                        for missao_nome_classe, missao_info_total in missoes_em_andamento_db.items():
                            sleep(1)

                            f.aviso(f"     {missao_nome_classe}    ",tresPontos='')


                            for missao_numero, missao_info in missao_info_total.items():

                                sleep(1)
                                print(f'\n\033[35m{f"Missão {missao_numero}":^{tamanho_do_programa}}\033[m')
                                f.linha()
                                
                                for missao_info_chave, missao_info_valor in missao_info.items():
                                    sleep(1)

                                    if isinstance(missao_info_valor, dict): # Recompensa
                                        print(f'\n\033[32m{missao_info_chave}:\033[m')
                                            
                                        for recompensa_chave, recompensa_valor in missao_info_valor.items():
                                            sleep(1)
                                            print(f'- \033[31m{recompensa_chave}\033[m: {recompensa_valor}')
                                    
                                    elif isinstance(missao_info_valor, list): # Descrição
                                        print(f'\n\033[32m{missao_info_chave}:\033[m\n')

                                        for frase in missao_info_valor:
                                            print(f'{frase}')

                                    else:
                                        print(f'\n\033[32m{missao_info_chave}\033[m: {missao_info_valor}')

                                print()
                                f.linha()

                                sleep(2)

            case 3: # Ajuda
                
                while not encerrar_menu_ajuda:
                    escolha_ajuda = f.printMenu("Ajuda", menu_ajuda )

                    print()
                    f.linha()
                    print()
                    print(respostas_ajuda[escolha_ajuda-1])
                    print()
                    f.linha()
                    sleep(1.5)

            case 0: # Sair
                encerrar_programa = True
                break

        encerrar_menu_personagem = False
        encerrar_menu_personagem_informacoes = False
        encerrar_menu_missoes = False
        # with open("dados.json", "r") as dados_json:
        #     dados_py = json.load(dados_json)
        # ----- Dump para o arquivo JSON -----
        # with open("dados.json", "w") as dados_json:
        #     json.dump(dados_py, dados_json)

f.aviso(' Encerrando','Programa')
