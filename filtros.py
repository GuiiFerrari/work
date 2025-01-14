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

def main():
    mt = [ [ 9,  4,  5,  0,  8,  0],
           [10,  3,  2,  1,  7,  6],
           [ 9,  1,  6,  3, 15,  5],
           [ 0,  3,  8, 10,  1,  3],
           [ 1, 16,  9, 12,  7,  4] ]

    print("1. array representando uma  imagem:")
    img = np.array(mt, int)
    print(img, "\n")
    
    print("2. vista da vizinhança de largura 3 de [1][2]:")
    print(img[0:3 , 1:4], "\n")

    print("3. vista da vizinhança de largura 3 de [4][5]:")
    print(img[3:6 , 4:7], "\n")  # cuidado com índices negativos

    print("4. maximo da vizinhaça de largura 3 de [1][2]:", np.max(img[0:3 , 1:4]))

    print("5. maximo da vizinhaça de largura 3 de [4][5]:", np.max(img[3:6 , 4:7]), "\n")

          
    print("6. array após dilataçao:")   
    dil = img.copy()
    filtro_dilatacao(dil, 3) # função mutadora
    print(dil, "\n")
    
    print("7. array representando o contraste:")
    cimg = dil - img
    print(cimg, "\n")
    
    print("8. array representando a segmentação:")    
    img_binaria = segmentacao(img, 3, 9, 99, 0) # função não é mutadora
    print(img_binaria)
    
#------------------------------------------------------------------
def filtro_dilatacao(img, v):
    '''(array, int) -> None

    Recebe um array img representando uma imagem e um inteiro positivo ímpar v.
    Aplica o filtro da dilatação na imagem considerando vizinhanças de largura v.
    '''
    
    #o metodo np.amax eu utilizei do seguinte site: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.amax.html
    #basicamente apliquei um método que estava no manual
    
    copia = np.copy(img)
    alcance = int((v-1)/2)      #determino o "raio de atuação" a partir do ponto central analisado
    limitelinha, limitecoluna = img.shape
    if limitecoluna == None:
        limitecoluna = limitelinha
        limitelinha = 1        
    for i in range(0, limitelinha):
        for j in range(0, limitecoluna):
            linha = i - alcance
            coluna = j - alcance
            if linha < 0:               #se o ponto minimo das vizinhanças for <0, então assume valor 0
                linha = 0
            if coluna < 0:
                coluna = 0
            copiaparcial = copia[linha:(i + alcance + 1), coluna :(j + alcance + 1)]   #seleciona a vizinhança do ponto
            maximo = np.amax(copiaparcial)      #função que pegar o valor máximo do recorte feito do array
            if copia[i][j] != maximo :          #o ponto central seja diferente do maximo da vizinhaça, então o ponto recebe o maximo
                img[i,j] = maximo
 
#------------------------------------------------------------------
def segmentacao(img, v, limiar, alto, baixo):
    '''(array, int, int, int, int) -> array
 
    Recebe uma imagem img e inteiros v, limiar, alto e baixo.
    Retorna a imagem binária obtida através da aplicação do filtro 
    da segmentação em img. 
    '''
    copia = np.copy(img)
    limitelinha, limitecoluna = img.shape
    if limitecoluna == None:
        limitecoluna = limitelinha
        limitelinha = 1
    filtro_dilatacao(copia, v)      #a copia é recebe a dilatação
    contraste = copia - img
    copiacontraste = np.copy(contraste)     #copia do contraste que será alterada
    for i in range(0, limitelinha):
        for j in range(0, limitecoluna):
            if contraste[i, j] <= limiar:       #analisa o valor basiado no limiar dado
                copiacontraste[i, j] = baixo
            else:
                copiacontraste[i, j] = alto
    return copiacontraste                       #retorna a imagem segmentada

#--------------------------------------------------------------------------
if __name__ == "__main__":
    main()
