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
    monitores e colegas). Com exceção de material de MAC0110 ou MAC0122, 
    caso  você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
from percolation import Percolation
import numpy as np
import random
import math
                 
class PercolationStats:
    '''Classe utilizada para estimar o limiar de percolação.
    '''

    def __init__(self, shape, T):
        grade = Percolation(shape)
        self.grade = Percolation(shape)
        self.T = T
        self.x = [] #inicia a lista de armazena os limiares de percolação
        self.numsitios = grade.op   #guarda o numero de sitios da grade
        for i in range(T):  
            contagem = 0    #reinicia a contagem de sitios abertos
            while grade.percolates() == False:
                valorlinha = random.randint(0, grade.lin - 1)   #produz um valor inteiro aleatorio dentro do shape da grade
                valorcoluna = random.randint(0, grade.col - 1)
                if grade.is_open(valorlinha, valorcoluna) == False: #caso não seja BLOCKED abre o ponto da grade
                    grade.open(valorlinha, valorcoluna)             #e adiciona +1 na contagem
                    contagem += 1
            self.x.append(contagem/self.numsitios)  #adiciona um valor de limiar na lista
            grade = Percolation(shape)      #refaz a grade

    def mean(self):
        return np.mean(self.x)      #usa o numpy e retorna a média
    
    def stddev(self):
        return np.std(self.x)       #usa o numpy e retorna o desvio padrão
    
    def confidenceLow(self):
        return self.mean() - (1.96*self.stddev()/math.sqrt(self.T)) #retorna o valor inferior
         
    def confidenceHigh(self):
        return self.mean() + (1.96*self.stddev()/math.sqrt(self.T)) #retorna o valor superior       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        