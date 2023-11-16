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

# Função para printar um menu
def printMenu(titulo="",opcoes={},tamanho=calcTamanhoPrograma('Programa X')):
    frase_maior = ''

    print(f'{titulo.upper():^{tamanho}}')
    linhaSimples(tamanho)

    for k, v in opcoes.items():
        frase_nova = f'[{k}] - {v}'

        if len(frase_nova) > len(frase_maior):
            frase_maior = frase_nova

    centralizar = math.ceil((tamanho - len(frase_maior)) / 2)

    while True:

        for k, v in opcoes.items():

            print(' ' * centralizar, end="")

            print(f"[{k}] - {v}")

        linhaSimples(tamanho)

        escolha_usuario = tratarInput('qual a sua opcao?', len(opcoes))
        
        return escolha_usuario

# --------------------- Programa Principal ---------------------

# ---------- Variáveis ---------- #

encerrar_programa = False

# ---------- Loop do Programa ----------

while not encerrar_programa:

    tamanho_do_programa = calcTamanhoPrograma('Programa X')

    # ----- Leitura do arquivo JSON -----

    with open("dados.json", "r") as dados_json:
        dados_py = json.load(dados_json)

    # ----- Print do Menu Principal -----
    
    printMenu("menu principal", menu_options)


    escolha_principal = inputSublinhado('Selecione uma opção: ')

    carregandoMenu('Exemplo')


    # ----- Dump para o arquivo JSON -----

    with open("dados.json", "w") as dados_json:
        json.dump(dados_py, dados_json)
