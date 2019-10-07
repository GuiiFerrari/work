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

        Minha colega Maria me explicou que eu devia utilizar a função int() 
        quando fazemos leitura de números inteiros.

        No fórum escreveram para usar a função ...

        A minha solução foi baseada na descrição encontrada na 
        página https://stackoverflow.com/questions/15976333/

    Descrição de ajuda ou indicação de fonte:
'''

#------------------------------------------------------------
class Revendedora:
    ''' Recebe uma lista estoque com os comprimentos de rolos 
        disponíveis e atende pedidos fazendo controle desse 
        estoque.
    '''
    
    def __init__(self, lista = None):
        self.estoque = lista    #recebe a lista do estoque
        self.tam_estoque = len(lista)
        self.vetor = [] #vetor que será retornado do método atenda_encomenda
    
    def __str__(self):
        numrolos = self.tam_estoque
        s= ''
        s = 'Estoque possui %d'%(numrolos) + ' rolos:\n'
        for i in range(numrolos):
            s += '    rolo %d'%(i) + ':  %d'%(self.estoque[i]) + ' m\n'
        return s
    
    def atenda_encomenda(self, encomenda):
        for i in range(self.tam_estoque):   #percorre o estoque
            if encomenda[0] <= self.estoque[i]: #caso seja possível cortar o rolo
                self.estoque[i] -= encomenda[0] #o rolo i do estoque é cortado
                self.vetor.append(i)    #o vetor de saída recebe o numero do rolo no final da lista
                if len(encomenda) > 1:  #caso tenha mais que um pedido
                    if self.atenda_encomenda(encomenda[1:]) == None: #o método é chamado novamente com o pedido reduzido
                        self.vetor.pop()    #caso retorna vazio, ou seja, que não é possivel, o ultimo item do vetor é excluido
                        self.estoque[i] += encomenda[0] #o pedaço recortado é restituído
                    else:
                        return self.vetor #caso seja possível retorna o vetor
                else:
                    return self.vetor #no caso de um único pedido, já retorna o vetor
        return None #caso percorra e não retorne nada, retorna None
               
        
        
                    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    