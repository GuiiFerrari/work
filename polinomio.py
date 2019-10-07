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
class Polinomio:
    
    def __init__(self, coefs = None):
        if coefs == None:
            self.copiacoef = self.coefs.copy()
        elif type(coefs) == list:
            self.coefs = coefs.copy()
        else:
            self.coefs = coefs

    def __str__(self):
        coeficientes = self.coefs
        p = ''
        self.verificacoefs()    #verifica se há zeros adicionais e evita prints com sinais extras
        if type(coeficientes) == int or type(coeficientes) == float or type(coeficientes) == complex:   # no caso de ter apenas um termo
            if type(coeficientes) == complex:
                p = '({0.real:.f} + {0.imag:.f}i)'.format(coeficientes)
            else:
                if coeficientes >= 0:
                    if type(coeficientes) == float:
                        p = '%f '%(coeficientes)
                    if type(coeficientes) == int:
                        p = '%d '%(coeficientes)
                else:
                    if type(coeficientes) == float:
                        p = '- %f'%(abs(coeficientes))
                    if type(coeficientes) == int:
                        p = '- %d '%(abs(coeficientes))
            return p
        if coeficientes[0] > 0: #adiciona o termo linear
            if type(coeficientes[0]) == int:
                p = '+ %d'%(coeficientes[0])
            if type(coeficientes[0]) == float:
                p = '+ %f'%(coeficientes[0])
        if coeficientes[0] < 0:
            if type(coeficientes[0]) == int:
                p = '- %d'%(abs(coeficientes[0]))
            if type(coeficientes[0]) == float:
                p = '- %f'%(abs(coeficientes[0]))
        graup = len(coeficientes) - 1       #guarda o grau do polinomio
        for indice in range(1, len(coeficientes)):  
            if coeficientes[indice] != 0:
                if indice != graup:   #enquanto não chegar no ultimo item que é o grau maximo do polinomio
                    if type(coeficientes[indice]) == complex:
                        p = '+ ({0.real:.f} + {0.imag:.f}i)'.format(coeficientes[indice]) + '*x^%d '%(indice) + p 
                    else:
                        if coeficientes[indice] > 0:
                            if type(coeficientes[indice]) == float:
                                p = '+ %f*x^%d '%(coeficientes[indice], indice) + p
                            if type(coeficientes[indice]) == int:
                                p = '+ %d*x^%d '%(coeficientes[indice], indice) + p
                        else:
                            if type(coeficientes[indice]) == float:
                                p = '- %f*x^%d '%(abs(coeficientes[indice]), indice) + p
                            if type(coeficientes[indice]) == int:
                                p = '- %d*x^%d '%(abs(coeficientes[indice]), indice) + p
                if indice == graup:         #no caso do ultimo coeficiente, não precisa adicionar o sinal '+'
                    if type(coeficientes[indice]) == complex:
                        p = '({0.real:.f} + {0.imag:.f}i)'.format(coeficientes[indice]) + '*x^%d '%(indice) + p 
                    else:
                        if coeficientes[indice] > 0:
                            if type(coeficientes[indice]) == float:
                                p = '%f*x^%d '%(coeficientes[indice], indice) + p
                            if type(coeficientes[indice]) == int:
                                p = '%d*x^%d '%(coeficientes[indice], indice) + p
                        else:
                            if type(coeficientes[indice]) == float:
                                p = '- %f*x^%d '%(abs(coeficientes[indice]), indice) + p
                            if type(coeficientes[indice]) == int:
                                p = '- %d*x^%d '%(abs(coeficientes[indice]), indice) + p
        return p
    
    def grau(self):
        return len(self.coefs) - 1
                    
    def coeficientes(self):
        self.verificacoefs()  #verifica se há zeros em excesso
        return self.coefs
                    
    def derive(self):
        coeficientes = self.coefs
        novoscoeficientes = []      #cria uma lista vazia que será preenchida
        for i in range(1, len(coeficientes)):
            novoscoeficientes.append(coeficientes[i]*i)     #preenche a lista com o coeficiente resultando (coeficiente * expoente)
        p = Polinomio(novoscoeficientes)
        return p
                    
    def __call__(self, valor = 0):
        coefs = self.coefs
        soma = 0
        for i in range(len(coefs)):
            soma += coefs[i]*((valor)**i)   #basicamente vai calculando os valores termo a termo e somando
        return soma
    
    def __add__(self, other):
        if type(other) == Polinomio:
            coefa = self.coefs
            coefb = other.coefs
            i = 0
            somacoef = []
            k1 = min(len(coefa), len(coefb))
            while i <= k1 - 1:          #faz a soma dentro do intervalo da intersecção das listas dos polinomios
                somacoef.append(coefa[i] + coefb[i])
                i += 1
            if len(somacoef) >= len(coefa) and len(somacoef) <= len(coefb): #no caso de sobrar coeficientes em other
                while i <= (len(coefb)-1):
                    somacoef.append(coefb[i])
                    i += 1
            else:                               #caso sobra coeficientes em self
                while i <= (len(coefa)-1):
                    somacoef.append(coefa[i])
                    i += 1
            soma = Polinomio(somacoef)
        if type(other) == float or type(other) == int or type(other) == complex:
            copia = self.coefs.copy()       #faz uma copia para não alterar a imagem self
            copia[0] += other
            soma = Polinomio(copia)
        return soma
    
    def __sub__(self, other): 
        if type(other) == Polinomio:
            if self.coefs == other.coefs:
                return Polinomio(0)
            coefa = self.coefs
            coefb = other.coefs
            i = 0
            somacoef = []
            k1 = min(len(coefa), len(coefb))
            while i <= k1 - 1:          #mesmo principio do add, subtrai primeiro no intervalo concomitante, depois verifica o restante
                somacoef.append(coefa[i] - coefb[i])
                i += 1
            if len(somacoef) >= len(coefa) and len(somacoef) <= len(coefb):
                while i <= (len(coefb)-1):
                    somacoef.append(-coefb[i])
                    i += 1
            else:
                while i <= (len(coefa)-1):
                    somacoef.append(coefa[i])
                    i += 1
            subtracao = Polinomio(somacoef)
        if type(other) == float or type(other) == int or type(other) == complex:
            coefs = self.coefs
            coefs[0] -= other
            subtracao = Polinomio(coefs)
        return subtracao

    def __radd__(self, other):
        return self + other
    
    def verificacoefs(self):        #método extra que verifica se há zeros adicionais em termos de ordens superiores
        continua = True             #inicializa a condição em True
        while continua == True and self.coefs != []:    #enquanto existir itens na lista e a continuação ser verdadeira o laço continua
            if type(self.coefs) != list:    #no caso de ter apenas um valor
                copia = []
                copia.append(self.coefs)
                self.coefs = []
                self.coefs.append(copia[0])
            if self.coefs[-1] == 0:     #caso o último termo seja 0 ele é retira (.pop())
                self.coefs.pop()
            elif self.coefs != []:      #caso o ultimo termo não seja vazio
                continua = False
            else:                       #caso o ultimo termo tenha valor diferente de zero
                continua = False
                
    def __mul__(self, other):
        if type(other) == int or type(other) == float or type(other) == complex: #caso com lista de um termo
            copia = self.coefs.copy()
            for i in range(len(copia)):
                copia[i] = copia[i]*other
            return Polinomio(copia)
        else:
            self.verificacoefs()        #reduz os coeficientes desnecessários
            other.verificacoefs()
            graumaximo = len(self.coefs) + len(other.coefs) + 1 #grau maximo possível da multiplicação
            resultadolista = [0]*graumaximo  #cria a lista resultante com zeros
            for i in range(len(self.coefs)):
                for j in range(len(other.coefs)):
                    resultadolista[i + j] += self.coefs[i] * other.coefs[j] #o termo da multiplicação entra no coeficiente i + j do resultante, pois a ordem do coeficiente é i + j
            resultado = Polinomio(resultadolista)   #cria um polinomio com a lista resultante
            resultado.verificacoefs()               #diminui coeficientes desnecessários
            return resultado
    
    def __rmul__(self, other):
        return self*other
            