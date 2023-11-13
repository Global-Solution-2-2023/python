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

# --------------------- Funções ---------------------

# Função para definir o tamanho do programa no printdo terminal
def calcTamanhoPrograma(titulo=''):
    return len(titulo) * 3 # armazenando em uma variável o tamanho do título para formatação do menu

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

# --------------------- Programa Principal ---------------------

# ---------- Variáveis ----------

encerrar_programa = False

# ---------- Loop do Programa ----------

while not encerrar_programa:
    tamanho_do_programa = calcTamanhoPrograma('Programa X')


    # ----- Leitura do arquivo JSON -----

    with open("dados.json", "r") as dados_json:
        dados_py = json.load(dados_json)

    # ----- Print do Menu Principal -----
    
    print(f'{"MENU PRINCIPAL":^{tamanho_do_programa}}')
    linhaSimples(tamanho_do_programa)
    print(f"{'[1] - Opcao 1':^{tamanho_do_programa}}\n{'[2] - Opcao 2':^{tamanho_do_programa}}\n{'[3] - Opcao 3':^{tamanho_do_programa}}\n{'[4] - Opcao 4':^{tamanho_do_programa}}")
    linhaSimples(tamanho_do_programa)


    escolha_principal = inputSublinhado('Selecione uma opção: ')

    carregandoMenu('Exemplo')




    # ----- Dump para o arquivo JSON -----

    with open("dados.json", "w") as dados_json:
        json.dump(dados_py, dados_json)
