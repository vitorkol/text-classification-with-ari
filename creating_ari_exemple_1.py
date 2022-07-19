#Importando as bibliotecas 
import math
import re

#Para fins didáticos criei uma variável sentença que receberá a entrada de dados através da função input
#Terminal abrirá uma tela solicitando que o usuário digite o texto.
sentence = input('Digite a sua frase: ')

#Também é possível fazer a leitura de uma arquivo pré existente, para isso precisamos simplesmente passar o caminho do texto que será consumido
#Após carregar este arquivo de texto ele será passado como parâmetro para a função ARI.
#arquivoTexto = open('Caminho_do_arquivo.txt', 'r') -- descomentar essa linha
#sentence = arquivoTexto.read() -- descomentar essa linha

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
        
automated_readability_index(sentence)