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

# --------------------- Funções ---------------------#

# ---------- Opções ---------- #
menu_options = {
    "1" : "Personagem",
    "2" : "Skills",
    "3" : "Missões",
    "4" : "Configurações",
    "5" : "Ajuda",
    "0" : "Sair"
}

menu_ajuda_options = {
    "1" : {"Para que serve uma vida saudável" : "Para ter mais saude"},
    "2" : {"Problema 2" : "Resposta 2"},
    "3" : {"Problema 3" : "Resposta 3"},
    "4" : {"Problema 4" : "Resposta 4"},
    "5" : {"Problema 5" : "Resposta 5"},
    "0" : "Voltar para o menu"
}

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
    while True:

        print(f'{titulo.upper():^{tamanho}}')
        linhaSimples(tamanho)

        # Centralizar
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
        try:
            escolha_usuario = input("Escolha uma opção: ")
            if escolha_usuario not in opcoes:
                raise ValueError
        except:
            print("Por favor, insira uma opção válida\n\n")
            continue
        # Printando opção escolhida
        print(f"{opcoes.get(escolha_usuario)}\n") 

        # Opções
        match escolha_usuario:
            case "0":
                print("Saindo do programa...")
                break
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                menuAjuda("Menu Ajuda", menu_ajuda_options)

# ------ Menu Ajuda ------ 
def menuAjuda(titulo="", opcoes={}, tamanho=calcTamanhoPrograma('Programa X')):
    while True:

        print(f'{titulo.upper():^{tamanho}}')
        linhaSimples(tamanho)

        # Centralizar
        frase_maior = ''
        for chave in opcoes:
            if isinstance(opcoes[chave], dict):
                frase_nova = f'[{chave}] - {list(opcoes[chave].keys())[0]}'
            else:
                frase_nova = f'[{chave}] - {opcoes[chave]}'

            if len(frase_nova) > len(frase_maior):
                frase_maior = frase_nova

        centralizar = math.ceil((tamanho - len(frase_maior)) / 2)

        # Print do menu
        for chave in opcoes:
            if isinstance(opcoes[chave], dict):
                print(' ' * centralizar, end="")
                print(f'[{chave}] - {list(opcoes[chave].keys())[0]}')
            else:
                print(' ' * centralizar, end="")
                print(f'[{chave}] - {opcoes[chave]}')


        linhaSimples(tamanho)

        # Verificando
        try:
            escolha_usuario = input("Escolha uma opção: ")
            if escolha_usuario not in opcoes:
                raise ValueError
            # Printando opção escolhida
            if escolha_usuario == "0":
                print(opcoes[escolha_usuario])
            else:
                print(list(opcoes[escolha_usuario].keys())[0])
        except:
            print("Por favor, insira uma opção válida\n\n")
            continue

        # Opções
        match escolha_usuario:
            case "0":
                print("Voltando para o menu principal...\n\n")
                break
            case "1":
                print(f'\nR: {list(opcoes["1"].values())[0]}\n\n')
            case "2":
                print(f'\nR: {list(opcoes["2"].values())[0]}\n\n')
            case "3":
                print(f'\nR: {list(opcoes["3"].values())[0]}\n\n')
            case "4":
                print(f'\nR: {list(opcoes["4"].values())[0]}\n\n')
            case "5":
                print(f'\nR: {list(opcoes["5"].values())[0]}\n\n')

# --------------------- Programa Principal ---------------------

# ---------- Variáveis ---------- 
tamanho_do_programa = calcTamanhoPrograma('Programa X')

# ---------- Loop do Programa ---------- 
printMenu("menu principal", menu_options)

# ----- Leitura do arquivo JSON -----
with open("dados.json", "r") as dados_json:
    dados_py = json.load(dados_json)


# ----- Dump para o arquivo JSON -----
with open("dados.json", "w") as dados_json:
    json.dump(dados_py, dados_json)
