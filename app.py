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
usuario_logado = 'admin1'

# ------ Variáveis de controle dos while ------

# Menus
encerrar_programa = False
encerrar_menu_inicial = True
encerrar_menu_personagem = False
encerrar_menu_skills = False
encerrar_menu_informacoes = False
encerrar_menu_informacoes_email = False
encerrar_menu_informacoes_usuario = False
encerrar_menu_informacoes_senha = False

encerrar_menu_missoes = False
encerrar_menu_ajuda = False

# Validação
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
    print(f'\n\033[32m{"Aplicativo Programa X":^{tamanho_do_programa}}\033[m\n')
    f.linha(tamanho_do_programa//2, '=-')
    print()

    # ----- Login | Cadastro -----

    while not encerrar_menu_inicial:

        escolha_inicial = f.printMenu("Inicial", menu_inicial)

        match escolha_inicial:
            case 1: # Login

                # ----- Leitura do arquivo JSON -----
                with open("dados.json", "r") as dados_json:
                    dados_py = json.load(dados_json)

                usuarios_db = dados_py["Usuarios"]

                while not validar_login:

                    f.aviso('    Login    ', tresPontos='')

                    print(f'\033[36m{f"Login":^{tamanho_do_programa}}\033[m')
                    f.linha()
                    print()
                    usuario_input_login = f.tratarErroStr('Digite o seu usuário: ')
                    print()
                    senha_input_login = f.tratarErroStr('\033[33mDigite a sua senha: \033[m')
                    print()
                    f.linha()

                    # Verificar os inputs
                    for usuario, valores in usuarios_db.items():

                        # se o usuario do json e a senha do json for igual aos inputs
                        if valores["Informacoes do Login"]['Usuario'] == usuario_input_login and valores["Informacoes do Login"]['Senha'] == senha_input_login:
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
                    email_input_cadastro = f.tratarErroStr('\033[33mEmail: \033[m')
                    print()
                    usuario_input_cadastro = f.tratarErroStr('\033[33mUsuário: \033[m')
                    print()
                    senha_input_cadastro = f.tratarErroStr('\033[33mSenha: \033[m')
                    print()
                    f.linha()

                    # Verificar se o usuário já existe
                    usuario_existente = False

                    if f.validarEmail(email_input_cadastro):

                        for usuario, valores in usuarios_db.items():

                            # Verificação de email e usuário
                            if valores["Informacoes do Login"]['Email'] == email_input_cadastro:
                                print()
                                f.aviso(' Erro! Email já cadastrado', tresPontos='')
                                usuario_existente = True
                                break

                            elif valores["Informacoes do Login"]['Usuario'] == usuario_input_cadastro:
                                print()
                                f.aviso(' Erro! Usuário já cadastrado', tresPontos='')
                                usuario_existente = True
                                break

                        if not usuario_existente:

                            print()
                            f.aviso(' Cadastro das suas informações realizado com sucesso!', tresPontos='')

                            validar_cadastro_info = True
                    else:
                        f.aviso(' Erro! Digite um email válido.', tresPontos='')

                while not validar_cadastro_skill:

                    f.linha()
                    
                    
                    f.linha()

                # Novo usuário que será adicionado
                novo_usuario = {
                    "Informacoes do Login": {
                        "Email": email_input_cadastro,
                        "Usuario": usuario_input_cadastro,
                        "Senha": senha_input_cadastro
                    },
                    "Skills": "",
                    "Missoes em Andamento": ""
                }

                usuarios_db[len(usuarios_db)+1] = novo_usuario

                # ----- Dump para o arquivo JSON -----
                with open("dados.json", "w") as dados_json:
                    json.dump(dados_py, dados_json)

            case 0: # Sair do programa
                encerrar_programa = True
                encerrar_menu_inicial = True

    if not encerrar_programa: # se usuário não quiser sairdo programa no Menu Inicial

        # ----- Leitura do arquivo JSON -----
        with open("dados.json", "r") as dados_json:
            dados_py = json.load(dados_json)

        usuarios_db = dados_py["Usuarios"]

        for id_usuario_loop, usuario_dados in usuarios_db.items():
            for k, v in usuario_dados.items():
                if k == "Informacoes do Login" and v["Usuario"] == usuario_logado:
                    if v["Usuario"] == usuario_logado:
                        usuario_logado_db = dados_py["Usuarios"][id_usuario_loop] # Carregar dados json do usuário logado
                        id_usuario = id_usuario_loop
                        break

        usuario_logado_bem_vindo = usuario_logado_db["Informacoes do Login"]["Usuario"]

        print()
        print(f'\033[33m{f"Seja bem-vindo {usuario_logado_bem_vindo}!":^{tamanho_do_programa}}\033[m')
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
                        f.aviso("Voltando para o Menu", "Principal")
                    
                    # Se não
                    else:

                        match escolha_personagem:

                            case 1: # Informações
                        
                                # Adicionar os dados do Usuario (JSON) no Menu
                                menu_personagem_informacoes = {}
                                cont = 0
                                for k in usuario_logado_db["Informacoes do Login"].keys():
                                    cont += 1
                                    menu_personagem_informacoes[cont] = f"{k}"
                                menu_personagem_informacoes[0] = "Voltar para o Menu Personagem"

                                while not encerrar_menu_informacoes:

                                    # ----- Leitura do arquivo JSON -----
                                    with open("dados.json", "r") as dados_json:
                                        dados_py = json.load(dados_json)

                                    usuario_logado_db = dados_py["Usuarios"][id_usuario]

                                    # Informações do Login 
                                    email_atual = usuario_logado_db["Informacoes do Login"]["Email"]
                                    usuario_atual = usuario_logado_db["Informacoes do Login"]["Usuario"]
                                    senha_atual = usuario_logado_db["Informacoes do Login"]["Senha"]

                                    escolha_informacoes = f.printMenu("Informações de Login", menu_personagem_informacoes)

                                    match escolha_informacoes:
                                        
                                        case 1: # Email

                                            while not encerrar_menu_informacoes_email:

                                                email_existente = False

                                                f.linha()
                                                print(f"\n\033[36m{f'Email: {email_atual}':^{tamanho_do_programa}}\033[m")
                                                print('\033[33m')
                                                
                                                email_input_alterar = f.tratarErroStr("Digite o seu novo email: ")
                                                print('\033[m')
                                                f.linha()

                                                if f.validarEmail(email_input_alterar):

                                                    if email_input_alterar == email_atual:
                                                        print("\n\033[31mNão é possível alterar o email com o mesmo nome.\033[m\n")

                                                    else:

                                                        for usuario, valores in usuarios_db.items():
                                                            if valores["Informacoes do Login"]['Email'] == email_input_alterar:
                                                                print()
                                                                print("\n\033[31mEmail já existente.\033[m\n")
                                                                email_existente = True

                                                        if not email_existente:

                                                            # ----- Leitura do arquivo JSON -----
                                                            with open("dados.json", "r") as dados_json:
                                                                dados_py = json.load(dados_json)

                                                            usuario_logado_db = dados_py["Usuarios"][id_usuario]

                                                            usuario_logado_db["Informacoes do Login"]["Email"] = email_input_alterar

                                                            # ----- Dump para o arquivo JSON -----
                                                            with open("dados.json", "w") as dados_json:
                                                                json.dump(dados_py, dados_json)

                                                            encerrar_menu_informacoes_email = True

                                                            print(f"\n\033[32mEmail alterado com sucesso!\033[m")
                                                else:
                                                    print("\n\033[31mDigite um email válido.\033[m\n")

                                        case 2: # Usuario

                                            while not encerrar_menu_informacoes_usuario:

                                                usuario_existente = False

                                                f.linha()
                                                print(f"\n\033[36m{f'Usuário: {usuario_atual}':^{tamanho_do_programa}}\033[m")
                                                print('\033[33m')
                                                usuario_input_alterar = f.tratarErroStr("Digite o seu novo usuário: ")
                                                print('\033[m')
                                                f.linha()

                                                if usuario_input_alterar == usuario_atual:
                                                    print("\n\033[31mNão é possível alterar o usuário com o mesmo nome.\033[m\n")

                                                else:

                                                    for usuario, valores in usuarios_db.items():
                                                        if valores["Informacoes do Login"]['Usuario'] == usuario_input_alterar:
                                                            print()
                                                            print("\n\033[31mUsuário já existente.\033[m\n")
                                                            usuario_existente = True

                                                    if not usuario_existente:

                                                        # ----- Leitura do arquivo JSON -----
                                                        with open("dados.json", "r") as dados_json:
                                                            dados_py = json.load(dados_json)

                                                        usuario_logado_db = dados_py["Usuarios"][id_usuario]

                                                        usuario_logado_db["Informacoes do Login"]["Usuario"] = usuario_input_alterar

                                                        # ----- Dump para o arquivo JSON -----
                                                        with open("dados.json", "w") as dados_json:
                                                            json.dump(dados_py, dados_json)

                                                        encerrar_menu_informacoes_usuario = True

                                                        usuario_logado = usuario_input_alterar

                                                        print(f"\n\033[32mUsuário alterado com sucesso!\033[m")
                                                
                                        case 3: # Senha

                                            while not encerrar_menu_informacoes_usuario:

                                                f.linha()
                                                print(f"\n\033[36m{f'Senha: {senha_atual}':^{tamanho_do_programa}}\033[m")
                                                print('\033[33m')
                                                senha_input_alterar1 = f.tratarErroStr("Digite a sua nova senha: ")
                                                print()
                                                senha_input_alterar2 = f.tratarErroStr("Digite novamente a sua nova senha: ")
                                                print('\033[m')
                                                f.linha()

                                                if senha_input_alterar1 == senha_input_alterar2:
                                                    if senha_input_alterar1 != senha_atual:

                                                        # ----- Leitura do arquivo JSON -----
                                                        with open("dados.json", "r") as dados_json:
                                                            dados_py = json.load(dados_json)

                                                        usuario_logado_db = dados_py["Usuarios"][id_usuario]

                                                        usuario_logado_db["Informacoes do Login"]["Senha"] = senha_input_alterar1

                                                        # ----- Dump para o arquivo JSON -----
                                                        with open("dados.json", "w") as dados_json:
                                                            json.dump(dados_py, dados_json)

                                                        encerrar_menu_informacoes_usuario = True

                                                        print(f"\n\033[32mSenha alterada com sucesso!\033[m")
                                                    
                                                    else:
                                                        print(f"\n\033[31mA sua nova senha não pode ser a mesma da atual\033[m\n")

                                                else:
                                                    print(f"\n\033[31mAs senhas não coincidem.\033[m\n")

                                        case 0:
                                            f.aviso("Voltando para o Menu", "Personagem")

                                            break

                                    encerrar_menu_informacoes_email = False
                                    encerrar_menu_informacoes_usuario = False
                                    encerrar_menu_informacoes_senha = False

                            case 2: # Skills

                                # Adicionar os dados do Usuario (JSON) no Menu
                                menu_personagem_skills = {}
                                cont = 0
                                for k in usuario_logado_db["Skills"].keys():
                                    cont += 1
                                    menu_personagem_skills[cont] = f"{k}"

                                # Se tiver 2 Skill Tree - Adicionar Todas como opção
                                if len(menu_personagem_skills) == 2:
                                    menu_personagem_skills[3] = "Todas"

                                menu_personagem_skills[0] = "Voltar para o Menu Personagem"

                                while not encerrar_menu_skills:

                                    # ----- Leitura do arquivo JSON -----
                                    with open("dados.json", "r") as dados_json:
                                        dados_py = json.load(dados_json)

                                    usuario_logado_db = dados_py["Usuarios"][id_usuario]

                                    escolha_skills = f.printMenu("Skills", menu_personagem_skills)

                                    if escolha_skills == 0:
                                        encerrar_menu_skills = True
                                        f.aviso("Voltando para o Menu", "Personagem")

                                    else:

                                        if len(menu_personagem_skills) == 2 or escolha_skills == 3: # Se tiver 1 Skill Tree

                                            # Print das Skills Trees das Skills
                                            for skill_tree, dados_skill_tree in usuario_logado_db["Skills"].items():
                                                sleep(1)
                                                print()
                                                print(f'\033[36m{skill_tree:^{tamanho_do_programa}}\033[m')
                                                f.linha()

                                                # Dados Skill Tree
                                                for classe, dados_classe in dados_skill_tree.items():
                                                    sleep(0.5)
                                                    print(f'\n\n\033[34m{classe}:\033[m')
                                                    sleep(1)

                                                    # Se for um diocionário
                                                    if isinstance(dados_classe, dict):
                                                        for k, v in dados_classe.items():
                                                            print(f'- \033[32m{k}:\033[m {v}')
                                                            sleep(1)
                                                    else:
                                                        print(f'- \033[32m{dados_classe}\033[m')
                                                print()
                                                print()
                                                f.linha()
                                                sleep(1)

                                        elif len(menu_personagem_skills) == 4: # Se tiver mais de 1 Skill Tree
                                            
                                            # Se for só uma


                                            # Print das Skills Trees das Skills
                                            for skill_tree, dados_skill_tree in usuario_logado_db["Skills"].items():

                                                sleep(1)
                                                print()
                                                if escolha_skills == 1 and skill_tree == "Saude Fisica": # Saude Fisica
                                                    print(f'\033[36m{skill_tree:^{tamanho_do_programa}}\033[m')
                                                    f.linha()

                                                    # Dados Skill Tree
                                                    for classe, dados_classe in dados_skill_tree.items():
                                                        sleep(0.5)
                                                        print(f'\n\n\033[33m{classe}:\033[m')
                                                        sleep(1)

                                                        # Se for um diocionário
                                                        if isinstance(dados_classe, dict):
                                                            for k, v in dados_classe.items():
                                                                print(f'- \033[32m{k}:\033[m {v}')
                                                                sleep(1)
                                                        else:
                                                            print(f'- \033[32m{dados_classe}\033[m')
                                                    print()
                                                    print()
                                                    f.linha()
                                                    sleep(2)

                                                elif escolha_skills == 2 and skill_tree == "Saude Mental": # Saude Mental
                                                    print(f'\033[36m{skill_tree:^{tamanho_do_programa}}\033[m')
                                                    f.linha()

                                                    # Dados Skill Tree
                                                    for classe, dados_classe in dados_skill_tree.items():
                                                        sleep(0.5)
                                                        print(f'\n\n\033[33m{classe}:\033[m')
                                                        sleep(1)

                                                        # Se for um diocionário
                                                        if isinstance(dados_classe, dict):
                                                            for k, v in dados_classe.items():
                                                                print(f'- \033[32m{k}:\033[m {v}')
                                                                sleep(1)
                                                        else:
                                                            print(f'- \033[32m{dados_classe}\033[m')
                                                    print()
                                                    print()
                                                    f.linha()
                                                    sleep(2)
                                                                                
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

                    if escolha_ajuda == 0:
                        encerrar_menu_ajuda = True
                        f.aviso("Voltando para o Menu", "Principal")
                        
                    else:
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
        encerrar_menu_missoes = False
        encerrar_menu_ajuda = False


        # with open("dados.json", "r") as dados_json:
        #     dados_py = json.load(dados_json)
        # ----- Dump para o arquivo JSON -----
        # with open("dados.json", "w") as dados_json:
        #     json.dump(dados_py, dados_json)

f.aviso(' Encerrando','Programa')
