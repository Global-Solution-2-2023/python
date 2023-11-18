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

# ---------- Dados ---------- #

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

menu_skills = {
    "Saúde Física" : {
        1: {"Nome Skill" : "Skill 1"},
        2: {"Nome Skill" : "Skill 2"},
        3: {"Nome Skill" : "Skill 3"},
        4: {"Nome Skill" : "Skill 4"},
        5: {"Nome Skill" : "Skill 5"},
        0: "Voltar para o Menu Principal"
    },
    "Saúde Mental" : {
        1 : {"Nome Skill" : "Skill 1"},
        2 : {"Nome Skill" : "Skill 1"},
        3 : {"Nome Skill" : "Skill 1"},
        4 : {"Nome Skill" : "Skill 1"},
        5 : {"Nome Skill" : "Skill 1"},
        0 : "Voltar para o Menu Principal"
    }
}


# --------------------- Programa Principal ---------------------

# ---------- Variáveis ---------- 

tamanho_do_programa = f.calcTamanhoPrograma('Programa X')
encerrar_programa = False

# ---------- Loop do Programa ---------- 

while not encerrar_programa:

    # ----- Leitura do arquivo JSON -----
    with open("dados.json", "r") as dados_json:
        dados_py = json.load(dados_json)
    
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
