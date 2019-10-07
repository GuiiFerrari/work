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
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
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

#-------------------------------------------------------------------------- 

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem

    def __init__(self, nlin = None, ncol = 0, valor = 0):
        if nlin is None:                        #caso receba vazio é atribuido array vazio
            nlin = np.full((0,0), 0)                
        if type(nlin) == np.ndarray:            #condições caso entre um array
            if np.array_equal(nlin, np.full((0,0), 0)) == True:     #caso seja default, i.e NumPymagem()
                self.imagem = np.full((0,0), 0)
            elif np.array_equal(nlin, np.full((0,0), 0)) == False:  #caso o array seja dado pelo usuário
                self.imagem = np.array(nlin)
        else:
            if type(valor) != np.ndarray:
                self.imagem = np.full((nlin, ncol), valor)              #caso sejam valores int/float recebidos
            else:
                self.imagem = np.array(valor)
                
        
        
    
    def __str__(self):
        s = str('')
        linhas, colunas = self.size()
        for i in range(linhas):
            for j in range(colunas):
                if j != 0:
                    s += ', '
                s += '%s'%(self.imagem[i, j])
            if i != linhas:
                s += ('\n')
        return s        
        
        
        
    def __add__(self, other):
        lin, col = self.size()
        soma = NumPymagem(lin, col, 0)
        for i in range(lin):
            for j in range(col):
                soma.put(i, j, self.get(i, j) + other.get(i, j))
        return soma
        
        
    def __mul__(self, other):
        lin, col = self.size()
        resultado = NumPymagem(lin, col, 0)
        for i in range(lin):
            for j in range(col):
                resultado.put(i, j, self.get(i, j)*other)
        return resultado
    
    
    def put(self, lin, col, valor):
        self.imagem[lin, col] = valor
        
        
    def size(self):
        linhas = self.imagem.shape[0]
        colunas =  self.imagem.shape[1]
        numeroelementos = self.imagem.size        
        if colunas == numeroelementos:
            return 1, numeroelementos
        else:
            return linhas, colunas
    
    def get(self, lin, col):
        return self.imagem[lin][col]
    
    def crop(self, tlx = 0, tly = 0, brx = -3, bry = -3):       #o valor -3 é algo aleatorio da entrada para condições iniciais dos ifs
                                                                
        if brx == -3 and bry == -3 and tlx == 0 and tly == 0:   #no caso de chamar .crop()
            novaimagem = np.copy(self.imagem)                   #Apenas copia o array
            return novaimagem
                    
        if (brx == -3 and bry == -3) and (tlx > 0 and tly > 0): #caso derem 2 argumentos, claramente são os valores de br
            brx = tlx                                           #então os valores recebidos passam para o BR e TL recebe (0,0)
            bry = tly
            tlx = 0
            tly = 0
            novaimagem = NumPymagem(brx - tlx, bry - tly, 0)
            linha = 0  
            coluna = 0
            for i in range(tlx, brx):
                for j in range(tly, bry):
                    novaimagem.put(linha, coluna, self.get(i, j))
                    coluna += 1
                coluna = 0
                linha += 1
            return novaimagem

        if (brx != -3 and bry != -3) and ((tlx > 0 and tly> 0) or (tlx == 0 and tly !=0) or (tlx != 0 and tly == 0)):
            novaimagem = NumPymagem(brx - tlx, bry - tly, 0)
            linha = 0                                   #o if acima ficou grande pois existem 3 condições de chamar a função crop com 
            coluna = 0                                  #4 argumentos dados
            for i in range(tlx, brx):
                for j in range(tly, bry):
                    novaimagem.put(linha, coluna, self.get(i, j))
                    coluna += 1
                coluna = 0
                linha += 1
            return novaimagem
            
    
    def paste(self, other, lin, col):           
        linhas, colunas = self.size()
        linhaother, colunaother = other.size()
        i = lin                                 #sobrepõe os valores pelos de other dentro do intervalo especificado
        j = col
        iother = 0
        jother = 0
        while i < linhas and iother < linhaother:
            while j < colunas and jother < colunaother:
                self.put(i, j, other.get(iother, jother))
                j += 1
                jother += 1
            j = col
            jother = 0
            i += 1
            iother += 1    

    def pinte_disco(self, lin, col, raio, val):         
        linha, coluna = self.size()
        for i in range(linha):
            for j in range(coluna):             #abaixo usei a equação de uma circunferencia (X-A)^2 + (Y-B)^2 = R^2
                if ((i - lin)**2 + (j - col)**2) < raio**2:
                    self.put(i, j, val)
        
    def pinte_retangulo(self, tlx, tly, brx, bry, val):
        if tlx < 0:
            tlx = 0                     #zera o ponto TL caso seja dado foram da pymagem, depois segue normalmente preenchendo o retangulo
        if tly < 0:
            tly = 0
        linhas, colunas = self.size()
        i = tlx
        j = tly
        while i < brx and i < linhas:
            while j < bry and j < colunas:
                self.put(i, j, val)
                j += 1
            j = tly
            i += 1

########################################################################################

    def transpoe(self):
        copia = np.copy(self.imagem)       
        self.imagem = copia.T               #Recebe a própria imagem transposta
        
    def rearranja(self, nlin, ncol):
        nlins, ncols = self.size()
        if nlin*ncol == nlins*ncols:        #condição para o rearranjo
            copia = np.copy(self.imagem)
            self.imagem = copia.reshape(nlin, ncol)     #recebe o array rearranjado
            
    def espelha(self, eixo):
        copia = np.copy(self.imagem)    #recebe a copia do array
        lin, col = self.size()
        if eixo == 'h':
            self.imagem[0:lin, :] = copia[0:lin, ::-1]   #aqui ele recebe as linhas de maneira igual invertendo as colunas, o -1 faz a contagem inversa   
        if eixo == 'v':
            self.imagem = copia[::-1]                   #aqui só as linhas são invertidas
        
        
#########################################################################################
            
        
                
        
        
        

