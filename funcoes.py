from time import sleep
import math

# --------------------- Funções ---------------------

# Função para definir o tamanho do programa no printdo terminal
def calcTamanhoPrograma(titulo='Programa X'):
    return len(titulo) * 6 # armazenando em uma variável o tamanho do título para formatação do menu

# Função de linha simples para estética
def linha(tam=0,caractere='-'):
    print(f'{caractere}' * tam)

# Função de sublinhado para estética
def inputSublinhado(frase):
    escolha = input(frase)
    linha(len(frase + str(escolha)))
    sleep(1)
    return escolha

# Função para "carregar" o menu
def carregandoMenu(menu):
    frase = f'Carregando o Menu {menu}...'
    print()

    centralizar(frase)
    linha(len(frase), '~')

    centralizar(frase)
    print(frase)

    centralizar(frase)
    linha(len(frase), '~')
    print()
    sleep(1)

# Função para centralizar
def centralizar(frase='', tamanho=calcTamanhoPrograma()):
    centralizar =  math.ceil((tamanho - len(frase)) / 2)
    print(' ' * centralizar, end="")

# Função de printar os menus
def printMenu(titulo="",opcoes={},tamanho=calcTamanhoPrograma()):

    carregandoMenu(titulo)

    print(f'{f"Menu {titulo}":^{tamanho}}')
    linha(tamanho)

    # Calcular a centralização dos items do menu
    frase_maior = ''

    for k, v in opcoes.items():
        frase_nova = f'[{k}] - {v}'

        if len(frase_nova) > len(frase_maior):
            frase_maior = frase_nova

    # Print do menu
    for k, v in opcoes.items():
        centralizar(frase_maior)
        print(f"[{k}] - {v}")

    linha(tamanho)

    # Verificando
    escolha_usuario = verificarOpcao(opcoes, titulo.upper())
    
    sleep(1)
    return escolha_usuario

# Tratamento de erro e verificar opção
def verificarOpcao(opcoes='', menu=''):
    
    try:
        escolha_usuario = int(input("Escolha uma opção: "))
        if escolha_usuario not in opcoes.keys():
            raise ValueError

    except:
        print("Por favor, insira uma opção válida\n")

    # Opções
    match escolha_usuario:
        case "0":
            if menu == 'PRINCIPAL':
                print("Saindo do programa...\n")
                sleep(1)
                return escolha_usuario
        
            else:
                print("Voltando para o menu principal...\n")
                sleep(1)
                return escolha_usuario

        case _:
            for k, v in opcoes.items():
                if escolha_usuario ==  k:
                    print(f'\n {v}')
            return escolha_usuario
        
        