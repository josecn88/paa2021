#!/usr/bin/python3
"""
#25089 Baú da Felicidade
Aluno: Jose Ceron Neto 316571 
Disciplina: Projeto e Análise de Algoritmos - PAA - CCO00201_A_2020_2
Prof. Dr. Diego Furtado Silva

"""
def baufelicidade():
    # Iniciar leitura da quantidade N de moedas encontrada N (2 ≤ N ≤ 100) 
    # Caso não inicie leitura, retorne erro
    try:
        linha1 = input().rstrip().split()
    except:
        return -1

    totalpesomoedas = 0
    #print(linha1)
    linha2 = input().rstrip().split()
    pesomoedas = [int(i) for i in linha2]
    #print(linha2)
    #print(pesomoedas)
    totalpesomoedas = sum(pesomoedas)
    #print("Peso Total Moedas", totalpesomoedas)

    # Baseado no nível de dificuldade dos demais exercicios do run.codes
    #  os casos de testes passaram, mas estou receoso
    # que a solucao seja tão simples assim :)
    print(totalpesomoedas % 2)


if __name__ == "__main__":
    if( baufelicidade() == -1):
        print("Erro de leitura")
