import math
import re
import os

def automated_readability_index(sentence):
    qtd_letras = len(sentence)
    qtd_letras_sem_espaco = qtd_letras - sentence.count(' ')
    print(f'Quantidade de letras: {qtd_letras_sem_espaco}')
    print("-" * 30)
    qtd_palavras = len(sentence.split())
    print(f'Quantidade de palavras: {qtd_palavras}')
    print("-" * 30)
    frase = re.split(r'[.!?]+', sentence)
    qtd_frase = len(frase)
    print(f'Quantidade de frases: {qtd_frase}')
    print("-" * 30)
    print(f'{qtd_frase} frase, {qtd_palavras} palavras, {qtd_letras_sem_espaco} letras ')
    print("-" * 30)
    divisao1 = 4.71 * qtd_letras_sem_espaco / qtd_palavras
    divisao2 = 0.5 * qtd_palavras / qtd_frase
    resultado = divisao1 + divisao2 - 21.43
    resultado_arredondado = math.ceil(resultado)
    print(f'Resultado: {resultado}')
    print(f'Resultado arredondado: {resultado_arredondado}')
    if resultado_arredondado > 14:
        resultado_arredondado = 14
        print(f'O índice de legibilidade após aplicação de regra é: {resultado_arredondado}')
  
    elif resultado_arredondado < 0:
        resultado_arredondado = 1
        print(f'O índice de legibilidade após aplicação de regra é: {resultado_arredondado}')
       
    else:
        print(f'O índice de legibilidade após aplicação de regra é: {resultado_arredondado}')
if __name__ == '__main__':
    #Manipulação de arquivo, define o nome de caminho para os.path (por exemplo: saída, dividir e juntar).
    os.environ['OUTPUT_PATH'] = "count_letter.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #Atribui a várival sentença que receberá a entrada de dados através da função input
    sentence = input()
    #Atribui o resultado da função ARI ao output
    output = automated_readability_index(sentence)
    fptr.write(str(output) + '\n')
    fptr.close()