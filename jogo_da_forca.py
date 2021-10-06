import random
import time


def jogo_da_forca():
    lista_palavras = ocultar_palavra()
    palavra_original = lista_palavras[0]
    palavra_oculta = lista_palavras[1]
    lista_palavra_original = []
    lista_palavra_oculta = []
    tentativas = 7

    for letras in palavra_oculta:
        lista_palavra_oculta.append(letras)

    for letras in palavra_original:
        lista_palavra_original.append(letras)

    print('BEM-VINDO AO JOGO DA FORCA,ONDE O TEMA É ADIVINHAR UM ANIMAL!')
    time.sleep(0.5)
    print('Sorteando a palavra')
    print('....')
    time.sleep(2)
    print(f'O jogo da forca sorteou esta palavra:{palavra_oculta}, a qual possui {len(palavra_oculta)} letras '
          f'\ncaso você não acerte a letra correta inclusa nesta palavra, você tem 7 tentativas, se usar todas, PERDE!')

    while lista_palavra_oculta.count('_') != 0:
        letra = str(input('digite SOMENTE uma letra para ver se ela está na palavra:')).strip().lower()[0]
        indices = []

        if letra in lista_palavra_original:
            print('Sua letra encontra-se na palavra misteriosa')
            for k, v in enumerate(lista_palavra_original):
                if letra == v:
                    indices.append(k)
            for values in indices:
                lista_palavra_oculta.pop(values)
                lista_palavra_oculta.insert(values, letra)
            print(f'Agora a palavra misteriosa ficou sendo:')
            for valores in lista_palavra_oculta:
                print(valores, end=' ')
            print()

        else:
            tentativas -= 1
            print(f'você não acertou a letra,portanto agora voce só tem {tentativas} tentativas')
            desenha_forca(tentativas)

        if lista_palavra_oculta.count('_') == 0:
            imprime_mensagem_vencedor()

        if tentativas == 0:
            imprime_mensagem_perdedor(palavra_original.upper())

            break


def gerar_palavras_aleatorias():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for palavra in arquivo:
        palavras.append(palavra.strip())

    arquivo.close()
    return random.choice(palavras)


def sortear_palavra():
    palavra_original = gerar_palavras_aleatorias()
    return palavra_original


def ocultar_palavra():
    palavra_oculta = palavra_original = sortear_palavra()
    modificador = ''
    lista_palavras = []
    for k in range(len(palavra_oculta)):
        if palavra_oculta[k] != ' ':
            modificador = palavra_oculta.replace(palavra_oculta[k], '_')
        palavra_oculta = modificador
    lista_palavras = [palavra_original, palavra_oculta]
    return lista_palavras


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif tentativas == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif tentativas == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif tentativas == 7:
        print(' |      (_)   ')
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


jogo_da_forca()
