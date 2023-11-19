from time import sleep
import math

# --------------------- Funções ---------------------

# Função para definir o tamanho do programa no printdo terminal
def tamProg(titulo='Aplicativo Programa X'):
    return len(titulo) * 3 # armazenando em uma variável o tamanho do título para formatação do menu

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
def aviso(frase='Carregando o Menu ',menu='', tresPontos='... '):
    frase_aviso = f'{frase} {menu}{tresPontos}'
    print()

    centralizar(frase_aviso)
    linha(len(frase_aviso), '~')

    centralizar(frase_aviso)
    print(frase_aviso)

    centralizar(frase_aviso)
    linha(len(frase_aviso), '~')
    print()
    sleep(1)

# Função para centralizar
def centralizar(frase='', tamanho=tamProg()):
    centralizar =  math.ceil((tamanho - len(frase)) / 2)
    print(' ' * centralizar, end="")

# Função de printar os menus
def printMenu(titulo="",opcoes={},tamanho=tamProg(), menu='Menu '):

    aviso(menu=titulo)

    print(f'{f"{menu}{titulo}":^{tamanho}}')
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

    validacao_input = False

    while not validacao_input:
    
        try:
            escolha_usuario = int(input("Escolha uma opção: "))
            if escolha_usuario not in opcoes.keys():
                raise ValueError
            else: 
                validacao_input = True

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
        
        