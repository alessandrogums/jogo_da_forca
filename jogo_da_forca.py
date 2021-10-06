import random
import time


def jogo_da_forca():
    lista_palavras = ocultar_palavra()
    palavra_original = lista_palavras[0]
    palavra_oculta = lista_palavras[1]
    lista_palavra_original = []
    lista_palavra_oculta = []
    tentativas = 5

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
          f'\ncaso você não acerte a letra correta inclusa nesta palavra, você tem 5 tentativas, se usar todas, PERDE!')

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

        if lista_palavra_oculta.count('_') == 0:
            print('PARABÉNSSSS, VOCÊ ACERTOU A PALAVRA!!')

        if tentativas == 0:
            print('você gastou todas suas tentativas')
            print(f'a palavra era {palavra_original}')
            print('FIM DO JOGO!')
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


jogo_da_forca()
