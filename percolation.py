# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Guilherme Ferrari Fortino
    NUSP: 9301558

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
import numpy as np

#-------------------------------------------------------------------------
# se você quiser a classe Queue feita na aula, coloque o seu arquivo queue.py
# na mesma pasta do EP e descomente a linha abaixo
# from queue import Queue

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade n x m com todos os sítios inicialmente bloqueados.
    o parâmetro shape é a forma (n, m) do array que representa a grade.
    '''

    def __init__(self, shape = None):
        if shape != None:   #caso receba um shape
            linha, coluna = shape
            if coluna == None:  
                coluna = linha
                linha = 1
            if linha <= 0 or coluna <= 0:   #se receber um argumento negativo
                print('__init__(): shape inválido')
            else:
                self.shape = shape
                self.grade = np.full(self.shape, int(BLOCKED))
                self.op = self.grade.size   #guarda o numero de lugares bloqueados
                self.lin, self.col = shape
                if self.col == None:
                    self.col = self.lin
                    self.lin = 1
        if shape == None:   #imprime erro 
            print('__init__(): shape inválido')
            
    def __str__(self):  
        linhas, colunas = self.shape    #guarda o numero de linhas e colunas
        if colunas == None:
            colunas = linhas
            linhas = 1
        identador = '+---'*colunas + ('+\n') #identador para auxiliar o str
        resultado = identador
        for i in range(linhas):
            resultado += '|'
            for j in range (colunas):
                if self.grade[i, j] == OPEN:
                    resultado += ' o '
                elif self.grade[i, j] == FULL:
                    resultado += ' x '
                else:
                    resultado += '   '
                if j == colunas:
                    resultado += ('|') + ('\n')
                else:
                    resultado += '|'
            resultado += ('\n') + identador
        resultado += 'grade de dimensão: %sx%s'%(self.lin, self.col) + '\nno. sítios abertos: %s'%(self.op)
        resultado += '\npercolou: %s\n'%(self.percolates())
        return resultado
    
    def is_open(self, lin, col):
        if lin < self.lin and col < self.col and lin >= 0 and col >= 0: 
            if self.grade[lin, col] == OPEN or self.grade[lin, col] == FULL:      #retorna se é OPEN ou FULL
                return True
            else:
                return False
        else:
            print('is_open(): posição [',lin,',',col,'] está fora da grade', sep='')
            return None
    
    def is_full(self, lin, col):
        if lin < self.lin and col < self.col and lin >= 0 and col >= 0:
            return self.grade[lin, col] == FULL     #retorna se é FULL
        else:
            print('isfull(): posição [',lin,',',col,'] está fora da grade', sep='')
            return None        
        
    def open(self, lin, col):
        copia = np.copy(self.grade)
        if lin < self.lin and col < self.col and lin >= 0 and col >= 0:     #caso seja um ponto válido
            if self.grade[lin, col] == BLOCKED:
                if lin == 0:        #abaixo são verificadas todos os possíveis vizinhos e se estão FULL ou OPEN. Fiquei atento à pontos nas extremidades das grades
                    self.grade[lin, col] = FULL
                    self.op -= 1
                elif col == 0:
                    if lin == self.lin - 1:
                        if copia[lin - 1, col] == FULL or copia[lin, col + 1] == FULL:
                            self.grade[lin, col] = FULL
                            self.op -= 1    #diminui o numero de sitios abertos
                        else:
                            self.grade[lin, col] = OPEN
                            self.op -= 1
                    else:
                        if copia[lin - 1, col] == FULL or copia[lin, col + 1] == FULL or copia[lin + 1, col] == FULL:
                            self.grade[lin, col] = FULL
                            self.op -= 1
                        else:
                            self.grade[lin, col] = OPEN
                            self.op -= 1
                elif col == self.col - 1:
                    if lin == self.lin - 1:
                        if copia[lin - 1, col] == FULL or copia[lin, col - 1] == FULL:
                            self.grade[lin, col] = FULL
                            self.op -= 1
                        else:
                            self.grade[lin, col] = OPEN
                            self.op -= 1
                    else:
                        if copia[lin - 1, col] == FULL or copia[lin, col - 1] == FULL or copia[lin + 1, col] == FULL:
                            self.grade[lin, col] = FULL
                            self.op -= 1
                        else:
                            self.grade[lin, col] = OPEN
                            self.op -= 1  
                else:
                    if lin == self.lin - 1:
                        if copia[lin - 1, col] == FULL or copia[lin, col - 1] == FULL or copia[lin, col + 1] == FULL:
                            self.grade[lin, col] = FULL
                            self.op -= 1
                        else:
                            self.grade[lin, col] = OPEN
                            self.op -= 1
                    else:
                        if copia[lin - 1, col] == FULL or copia[lin, col - 1] == FULL or copia[lin + 1, col] == FULL or copia[lin, col + 1] == FULL:
                            self.grade[lin, col] = FULL
                            self.op -= 1
                        else:
                            self.grade[lin, col] = OPEN
                            self.op -= 1
            self.atualiza_grade()   #depois de abrir percorre a grade atualizando-a
        else:
            print('open(): posição [',lin,',',col,'] está fora da grade', sep='')
            return None
    
    def no_open(self):
        return self.op #retorna diretamente o numero de sitios abertos
    
    def get_grid(self):
        copia = np.copy(self.grade)  #retorna uma cópia
        return copia
            
    def percolates(self):
        percola = False
        for j in range(self.col):
            if self.grade[self.lin - 1, j] == FULL:
                percola = True  #há percolação se na ultima linha existir pelo menos um sítio FULL
        return percola
            
    def atualiza_grade(self):   #atualiza a grade
        copia = self.grade      
        numverificacoes = self.grade.size
        while numverificacoes > 0:  #a grade é atualiza o numero de elemento vezes, pois isso garante que ao final tudo estará atualizado
            for i in range(1, self.lin):
                for j in range(self.col):
                    if self.grade[i, j] == OPEN:
                        if j == 0:
                            if i == self.lin - 1:
                                if copia[i - 1, j] == FULL or copia[i, j + 1] == FULL:
                                    self.grade[i, j] = FULL
                            else:
                                if copia[i - 1, j] == FULL or copia[i, j + 1] == FULL or copia[i + 1, j] == FULL:
                                    self.grade[i, j] = FULL
                        elif j == self.col - 1:
                            if i == self.lin - 1:
                                if copia[i - 1, j] == FULL or copia[i, j - 1] == FULL:
                                    self.grade[i, j] = FULL
                            else:
                                if copia[i - 1, j] == FULL or copia[i, j - 1] == FULL or copia[i + 1, j] == FULL:
                                    self.grade[i, j] = FULL
                        else:
                            if i == self.lin - 1:
                                if copia[i - 1, j] == FULL or copia[i, j - 1] == FULL or copia[i, j + 1] == FULL:
                                    self.grade[i, j] = FULL
                            else:
                                if copia[i - 1, j] == FULL or copia[i, j - 1] == FULL or copia[i + 1, j] == FULL or copia[i, j + 1] == FULL:
                                    self.grade[i, j] = FULL               
            numverificacoes -= 1
            