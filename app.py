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
from time import sleep
from random import randint
import math

# ---------- Opções ---------- #

menu_principal = {
    "1" : "Personagem",
    "2" : "Skills",
    "3" : "Missões",
    "4" : "Ajuda",
    "5" : "Configurações",
    "0" : "Sair"
}

menu_ajuda = {
    "1" : {"Para que serve uma vida saudável?" : "Para ter mais saúde."},
    "2" : {"Problema 2" : "Resposta 2"},
    "3" : {"Problema 3" : "Resposta 3"},
    "4" : {"Problema 4" : "Resposta 4"},
    "5" : {"Problema 5" : "Resposta 5"},
    "0" : "Voltar para o menu"
}

skills = {
    "Saúde Física" : {
        "1": {"Nome Skill" : "Skill 1"},
        "2": {"Nome Skill" : "Skill 2"},
        "3": {"Nome Skill" : "Skill 3"},
        "4": {"Nome Skill" : "Skill 4"},
        "5": {"Nome Skill" : "Skill 5"},
        "0": {"" : ""},
    },
    "Saúde Mental" : {
        "1" : {"" : ""},
        "2" : {"" : ""},
        "3" : {"" : ""},
        "4" : {"" : ""},
        "5" : {"" : ""},
        "0" : "Sair"
    }
}

# --------------------- Funções ---------------------

# Função para definir o tamanho do programa no printdo terminal
def calcTamanhoPrograma(titulo=''):
    return len(titulo) * 6 # armazenando em uma variável o tamanho do título para formatação do menu

# Função de linha simples para estética
def linhaSimples(tam):
    print('-' * tam)

# Função de linha com detalhe para estética
def linDetalhe(tam):
    print('-=' * tam)

# Função de sublinhado para estética
def inputSublinhado(frase):
    escolha = input(frase)
    linhaSimples(len(frase + str(escolha)))
    sleep(1)
    return escolha

# Função para "carregar" o menu
def carregandoMenu(menu):
    print()
    frase = f'Carregando o Menu {menu}...'
    linhaSimples(len(frase))
    print(frase)
    linhaSimples(len(frase))
    print()
    sleep(0.5)

# Função Menu Principal
def printMenu(titulo="",opcoes={},tamanho=calcTamanhoPrograma('Programa X')):

    print(f'{titulo.upper():^{tamanho}}')
    linhaSimples(tamanho)

    # Calcular a centralização dos items do menu
    frase_maior = ''

    for k, v in opcoes.items():
        frase_nova = f'[{k}] - {v}'

        if len(frase_nova) > len(frase_maior):
            frase_maior = frase_nova

    centralizar = math.ceil((tamanho - len(frase_maior)) / 2)


    # Print do menu
    for k, v in opcoes.items():
        print(' ' * centralizar, end="")
        print(f"[{k}] - {v}")

    linhaSimples(tamanho)

    # Verificando
    escolha_usuario = verificarOpcao(opcoes, titulo.upper())
    
    return escolha_usuario

# Tratamento de erro e verificar opção
def verificarOpcao(opcoes='', menu=''):
    
    try:
        escolha_usuario = input("Escolha uma opção: ")
        if escolha_usuario not in opcoes.keys():
            raise ValueError

    except:
        print("Por favor, insira uma opção válida\n")

    # Opções
    match escolha_usuario:
        case "0":
            if menu == 'MENU PRINCIPAL':
                print("Saindo do programa...\n")
                sleep(1)
                return (escolha_usuario, True) # para sair do programa
        
            else:
                print("Voltando para o menu principal...\n")
                sleep(1)
                return escolha_usuario

        case _:
            for k, v in opcoes.items():
                if escolha_usuario ==  k:
                    print(f'\n {v}')
            return escolha_usuario
                

# --------------------- Programa Principal ---------------------

# ---------- Variáveis ---------- 

tamanho_do_programa = calcTamanhoPrograma('Programa X')
encerrar_programa = False

# ---------- Loop do Programa ---------- 

while not encerrar_programa:

    # ----- Leitura do arquivo JSON -----
    with open("dados.json", "r") as dados_json:
        dados_py = json.load(dados_json)
    

    escolha_principal = printMenu("menu principal", menu_principal)

    try:
        if escolha_principal[1] == True:
            break 
    except:
        pass

    match escolha_principal:
        case 1: # Personagem
            escolha_personagem = printMenu("Personagem",)

        case 2: # Skills
            escolha_skills = printMenu("Skills",)
            

        case 3: # Missões
            escolha_missoes = printMenu("Missões",)
            

        case 4: # Ajuda
            escolha_ajuda = printMenu("Ajuda",)
            

        case 5: # Configurações
            escolha_configuracoes = printMenu("Configurações",)
            




    # ----- Dump para o arquivo JSON -----
    with open("dados.json", "w") as dados_json:
        json.dump(dados_py, dados_json)
