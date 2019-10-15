# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
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
    monitores e colegas). Com exceção de material de MAC0122, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função 
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

#-------------------------------------------------------------------
#
# Funções administrativas mergeX() e mergesortX()
#
#-------------------------------------------------------------------
def mergeX(v, e, m, d):
    ''' (list, int, int, int) -> int

    RECEBE uma lista v tal que v[e:m] e v[m:d] estão em ordem crescente. 
    A função intercala essas fatias de forma que v[e:d] esteja em ordem crescente.

    RETORNA o número de transposições necessários para ordenar v[e:d].
    '''
    w = [] #cria lista vazia que recebe valores intercalados
    i = e
    j = m
    transposicoes = 0   #zera numero de tranposições
    #codigo abaixo funciona recebendo uma lista com metades ordenadas, como visto em sala de aula
    while i < m and j < d:
        if v[i] <= v[j]:
            w.append(v[i])
            i += 1
        else:
            w.append(v[j])
            j += 1
            transposicoes += (j - i) - (j - m) #cada transposição deve contar apenas o deslocamente dentro da lista B, ou seja,
    while i < m:                               # a direita ordenada da lista: j - i - j + m = m - i. Deixei explicito para fins de correção
        w.append(v[i])
        i += 1
    while j < d:
        w.append(v[j])
        j += 1
    for i in range(len(w)):
        v[e+i] = w[i]
    #print("Vixe! ainda não fiz a função mergeX().")
    return transposicoes

def mergesortX(v, e=None, d=None):
    ''' (list, int, int) -> int

    Recebe uma lista v e dois inteiros que definem 
    um segmento de v que deve ser ordenado. 

    Quando e e d são None, a lista inteira deve ser ordenada.

    A função retorna o número de transposições resultantes da ordenação 
    de v[e:d].
    '''
    if e == None: #caso valores sejam vazios, pega os limites da lista
        e = 0
    if d == None:
        if type(v) == list:
            d = len(v)
        else:
            d = 1
    transposicoes = 0 #zera transposições
    if e < d-1:
        m = (e+d)//2 #m = valor do meio da lista
        transposicoes += mergesortX(v,e,m) #vai somando as transposições que vão ocorrendo
        transposicoes += mergesortX(v,m,d)
        transposicoes += mergeX(v,e,m,d)
    #print("Vixe! ainda não fiz a função mergesortX().")
    return transposicoes


#-----------------------------------------------------------
class Cliente:
    '''
        Copie a sua classe Cliente do EP10 para aqui.

        Estenda essa classe adicionando os métodos:
           em_comum() e distanciaX()
        como especifado no enunciado.
 
        Coloque o seu código a seguir.
    '''

    def __init__(self, nome = ''):
        self.cliente = nome     #guarda o nome do cliente
        self.filmes = []    #cria uma lista de filmes vazia que será preenchida depois
        
    def put_classificacao(self, filmes):
        self.filmes = filmes.copy()     #preenche a lista de filmes copiando a lista recebida
        
    def __str__(self):
        s = ''
        s += self.cliente + '\n'
        for i in range(len(self.filmes)):
            s += '%s'%(i) + ': ' + '%s'%(self.filmes[i]) + '\n'
        return s
        
    def get_nome(self):
        return self.cliente     #retorna o nome

    def get_classificacao(self):
        return self.filmes.copy()   #retorna um clone da lista de classificação dos filmes
    
    def distancia(self, Y = None):
        if Y == None:   #caso receba vazio retorna 0
            return 0
        if self.filmes == Y.filmes:  #caso sejam listas identicas
            return 0
        # o algoritmo que verifica os filmes em comum foi baseado nos comandos encontrados em: https://stackoverflow.com/questions/23529001/ordered-intersection-of-two-lists-in-python
        referencia1 = sorted(set(Y.filmes) & set(self.filmes), key = Y.filmes.index)
        referencia2 = sorted(set(Y.filmes) & set(self.filmes), key = self.filmes.index)
        distancia = 0
        while referencia1 != referencia2:   #o objeto é percorrer a referencia1 para ficar igual a referencia2
            for i in range(len(referencia1)-1, 0, -1): #algoritmo de ordenação baseado no Bubble Sort
                for j in range(i):
                    if referencia1[j] == referencia2[i]:    #identifica a posição entre as duas listas
                        passos = j  #enquanto não tiverem o mesmo filme na mesma posição, vai ordenando por transposição
                        while referencia1[i] != referencia2[i]:
                            temp = referencia1[passos + 1]
                            referencia1[passos + 1] = referencia1[passos]
                            referencia1[passos] = temp
                            passos += 1
                            distancia += 1
        if distancia <= 2:
            return 0
        else:
            return distancia
        
    def distanciaX(self, Y):
        if self.filmes == Y.filmes: #se forem iguais já retorna 0
            return 0
        referencia1 = self.em_comum(Y) #recebe a lista em comum
        transp1 = mergesortX(referencia1)   #recebe o numero de transposições feitas
        distancia = transp1
        if distancia <= 2:
            return 0
        return distancia
        
    def em_comum(self, Y):
    #as duas linhas abaixam calculam a intersecção das duas listas de filmes, baseado no que vi em: https://stackoverflow.com/questions/23529001/ordered-intersection-of-two-lists-in-python
        set_1 = frozenset(self.filmes)
        passo2 = [x for x in Y.filmes if x in set_1]
        emcomum = []    #lista vazia que receberá os indices
        dic = {self.filmes[i]:i for i in range(len(self.filmes))}   #cria um dicionario da lista de self.filmes que guarda seus indices, pois percorre-lo é de ordem O(1). fonte: https://stackoverflow.com/questions/19103785/efficient-dictionary-searching
        for i in range(len(passo2)):    #percorre a lista em comum, anexando o valor do indice correspondente da outra lista
            emcomum.append(dic[passo2[i]]) #procura no dicionario o correspondente
        return emcomum
        