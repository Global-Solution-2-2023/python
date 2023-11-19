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

# ---------- Dados ---------- #

menu_inicial = {
    1 : "Login",
    2 : "Cadastro",
    0 : "Sair"
}

menu_principal = {
    1 : "Personagem",
    2 : "Skills",
    3 : "Missões",
    4 : "Ajuda",
    5 : "Configurações",
    0 : "Sair"
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
usuario_logado = ''

# Variáveis de controle dos while
encerrar_programa = False
encerrar_menu_inicial = False
validar_login = False
validar_cadastro_info = False
validar_cadastro_skill = False

# Constantes

nivel_min = 1
nivel_max = 30


# ---------- Loop do Programa ---------- 

while not encerrar_programa:

    print()
    f.linha(tamanho_do_programa//2, '=-')
    print(f'{"Aplicativo Programa X":^{tamanho_do_programa}}')
    f.linha(tamanho_do_programa//2, '=-')
    print()

    # ----- Leitura do arquivo JSON -----
    with open("dados.json", "r") as dados_json:
        dados_py = json.load(dados_json)

    usuarios_db = dados_py["Usuarios"]

    # Calcular nível da Skill Corredor do usuário admin
    nivel_admin_corredor = random.randint(nivel_min, nivel_max)

    usuarios_db["admin"]["Skills"]["Corredor"]["Nivel"] = nivel_admin_corredor

    if nivel_admin_corredor <= 10:
        usuarios_db["admin"]["Skills"]["Corredor"]["Subclasse"] = 'Passo inicial'
    elif 10 < nivel_admin_corredor <= 20:
        usuarios_db["admin"]["Skills"]["Corredor"]["Subclasse"] = 'Ritmo Crescente'
    else:
        usuarios_db["admin"]["Skills"]["Corredor"]["Subclasse"] = 'Vento nas coxas'

    # ----- Dump para o arquivo JSON -----
    with open("dados.json", "w") as dados_json:
        json.dump(dados_py, dados_json)


    # ----- Login | Cadastro -----

    while not encerrar_menu_inicial:

        escolha_inicial = f.printMenu("Inicial", menu_inicial)

        match escolha_inicial:
            case 1: # Login

                while not validar_login:

                    f.aviso('    Login    ', tresPontos='')

                    f.linha(tamanho_do_programa)
                    print()
                    usuario_input_login = input('Digite o seu usuário: ')
                    print()
                    senha_input_login = input('Digite a sua senha: ')
                    print()
                    f.linha(tamanho_do_programa)

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

                skills_db = dados_py["Skills"]

                f.aviso('    Cadastro    ', tresPontos='')

                # ----- Cadastro das informações de login do usuário -----

                while not validar_cadastro_info:

                    f.linha(tamanho_do_programa)
                    print()
                    print(f'{f"Insira suas informações pessoais":^{tamanho_do_programa}}')
                    print()
                    email_input_cadastro = input('Email: ')
                    print()
                    usuario_input_cadastro= input('Usuário: ')
                    print()
                    senha_input_cadastro = input('Senha: ')
                    print()
                    f.linha(tamanho_do_programa)

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

                    f.linha(tamanho_do_programa)
                    
                    
                    f.linha(tamanho_do_programa)

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
        # Menu Principal
        escolha_principal = f.printMenu("Principal", menu_principal)

        match escolha_principal:
            case 1: # Personagem
                escolha_personagem = f.printMenu("Personagem",)

            case 2: # Skills
                escolha_skills = f.printMenu("Skills", menu_skills)
                

            case 3: # Missões
                escolha_missoes = f.printMenu("Missões",)
                

            case 4: # Ajuda
                escolha_ajuda = f.printMenu("Ajuda", menu_ajuda )
                

            case 5: # Configurações
                escolha_configuracoes = f.printMenu("Configurações",)
                
            case 0: # Sair
                encerrar_programa = True
                break


        # ----- Dump para o arquivo JSON -----
        with open("dados.json", "w") as dados_json:
            json.dump(dados_py, dados_json)

f.aviso(' Encerrando','Programa')
