#lista dicionario repetição algoritmo função
from tkinter import N


glossario = {
    'Algorítmo' : '''
    Sequência de passos que visam a atingir um objetivo bem definido. Algumas das das características do algoritmo são:
    Especifica uma sequência de passos;
    Seus passos são ordenados de forma lógica;
    Apresentam ações claras e precisas;
    Fixam um padrão de comportamento.
    ''',
    'Estruturas de Repetição' : '''
    Em Python existem duas formas de criar uma estrutura de repetição:
    O for é usado quando se quer iterar sobre um bloco de código um número determinado de vezes.
    O while é usado quando queremos que o bloco de código seja repetido até que uma condição seja satisfeita. Ou seja, é necessário que uma expressão booliana dada seja verdadeira. Assim que ela se tornar falsa, o while para.
    ''',
    'Lista' : '''
    Uma lista (list) em Python é uma sequência ou coleção ordenada de valores.
    Cada valor na lista é identificado por um índice.
    O valores que formam uma lista são chamados elementos ou itens.
    Existem várias maneiras de se criar uma nova lista.
    A maneira mais simples é envolver os elementos da lista por colchetes.
    ''',
    'Dicionário' : '''
    Um dicionário é uma espécie de estrutura de dados do tipo coleção. É, portanto, um objeto que contém mais que um valor. Dicionários em Python são conjuntos de chave-valor. A sintaxe para criação de dicionários em Python é {chave1 : valor1, chave2 : valor2, …​}. Assim como um dicionário de chaves (termos) que estão associadas a valores (significados dos termos), os dicionários em Python são uma estrutura de dados que nos permite mapear chaves a valores.
    ''',
    'Função' : '''
    Na programação, funções são blocos de código que realizam determinadas tarefas que normalmente precisam ser executadas diversas vezes dentro de uma aplicação. Quando surge essa necessidade, para que várias instruções não precisem ser repetidas, elas são agrupadas em uma função, à qual é dado um nome e que poderá ser chamada/executada em diferentes partes do programa.
    '''
}

print('\nGlossário de Introdução à Programação\n')
print('Algoritmo: ' + glossario['Algorítmo'] +
'____________________________________________________________________________________________________________' + '\n')
print('Estruturas de Repetição: ' + glossario['Estruturas de Repetição'] +
'____________________________________________________________________________________________________________' +  '\n')
print('Lista: ' + glossario['Lista'] + '\n'
'____________________________________________________________________________________________________________' +  '\n')
print('Dicionário: ' + glossario['Dicionário'] + '\n'
'____________________________________________________________________________________________________________' +  '\n')
print('Função: ' + glossario['Função'] + '\n'
'____________________________________________________________________________________________________________' +  '\n')
