import random
import time

def jogo_da_forca():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for palavra in arquivo:
        palavras.append(palavra.strip())
        
    arquivo.close()
    
    palavra_original = palavra = random.choice(palavras)
    modificador = ''
    lista_palavra_original = []
    lista_palavra = []
    tentativas = 5
    
    for k in range(len(palavra)):
        if palavra[k] != ' ':
            modificador = palavra.replace(palavra[k], '_')
        palavra = modificador
    for letra in palavra:
        lista_palavra.append(letra)

    for letra in palavra_original:
        lista_palavra_original.append(letra)

    print('BEM-VINDO AO JOGO DA FORCA,ONDE O TEMA É ADIVINHAR UM ANIMAL!')
    time.sleep(0.5)
    print('Sorteando a palavra')
    print('....')
    time.sleep(2)
    print(f'O jogo da forca sorteou esta palavra:{palavra}, a qual possui {len(palavra)} letras '
          f'\ncaso você não acerte a letra correta inclusa nesta palavra, você tem 5 tentativas, se usar todas, PERDE!')

    while lista_palavra.count('_') != 0:
        letra = str(input('digite SOMENTE uma letra para ver se ela está na palavra:')).strip().lower()[0]
        indices = []
        if letra in lista_palavra_original:
            print('Sua letra encontra-se na palavra misteriosa')
            for k, v in enumerate(lista_palavra_original):
                if letra == v:
                    indices.append(k)
            for values in indices:
                lista_palavra.pop(values)
                lista_palavra.insert(values, letra)
            print(f'Agora a palavra misteriosa ficou sendo:')
            for valores in lista_palavra:
                print(valores, end=' ')
            print()
        else:
            tentativas -= 1
            print(f'você não acertou a letra,portanto agora voce só tem {tentativas} tentativas')

        if lista_palavra.count('_') == 0:
            print('PARABÉNSSSS, VOCÊ ACERTOU A PALAVRA!!')

        if tentativas == 0:
            print('você gastou todas suas tentativas')
            print(f'a palavra era {palavra_original}')
            print('FIM DO JOGO!')
            break


jogo_da_forca()
