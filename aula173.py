import argparse
import sys

def fib(n):
    #Funçao usada para calcular o enesimo termo da sequência de fibonacci

    a,b = 0,1
    for i in range(n):
        a,b = b a+b

    return a 

def main():
    #Função prncipal programa

    parser = argparse.ArgumentParser(description="Exemplo argparse")

    part = 1

    if part ==1:
        part1(parser)
    elif part ==2:
        part2(parser)
    elif part ==3:
        part3(parser)
    else:
        part4(parser)

def part1(parser):

    #Depois podemos colocar os argumentos
    parser.add_argument("num",help="Numero da sequência de Fibonacci que deseja obter",type=int)

    #Depois nós pegamos os argumentos colocados na linha de comando 
    args = parser.parse_args()

    #Obtemos o resultado
    resultado = fib(args.num)

    #E o imprimimos na tela 
    print("O",args.num,"da sequência de fibonacci é ",resultado)

def part2(parser):

    #Função da segunda parte

    parser.add_argument("num",help="Número da sequência de Fibonacci que deseja obter",type=int)

    #Podemos colocar também o argumento opcional output
    parser.add_argument("-o","--output",help="Manda a saída do programa para um arquivo separado",action="store_true")

    #Depois nós pegamos os argumentos colocados na linha de comando
    args = parser.parse_args()

    #Obtemos o resultado
    resultado = fib(args.num)

    #E o imprimimos na tela
    if args.output:
        arq = open("fib.txt",'w')
        sys.stdout = arq

    print("O",args.num,"da sequência de fibonacci é",resultado)

def part3(parser):

    #Função parte três
                


