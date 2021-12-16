# MAC122 - PDA
# EP3 - Busca com duplo hash
# Heloísa Tambara - 12556819 

 # função para leitura dos arquivos
def func(arq):
    matriz = [] #declaro vetor
    texto = arq.readlines() #quebra as linhas do arquivo em vetores 
    
    for i in range(len(texto)):  # percorre os vetores
        texto[i] = texto[i].replace('\n', '').split(',')  # tira os '\n' e quebra nas vírgulas
        texto[i][1] = texto[i][1].split(' ') 

        
    return texto





def primo(a): # devolve os divisores de um número
    a = int(a)
    divisores = []
    for i in range(a):
        if i != 0 and i != a - 1:
            if a % (i + 1 ) == 0:
                divisores.append(i+1)
    return divisores


def hash(a, M):
    s = 0
    # s conterá a soma dos valores numéricos dos caracteres
    for chr in a:
        s = s + ord(chr)
    return s % M


def hash2(a):
    k = 2
    div = primo(a)
    while k < a:
        if k in div: 
            k += 1
        else: break # para quando k e a forem primos entre si

    return k # valor da função - passo

    
def insere_hash(a, x, ind):
    M = len(a)
    cont = 0
    i = hash(x, M)
    k = hash2(M)
    # procura a próxima posição livre
    while a[i] != None:
        if x in a[i]:
            a[i].append(ind) # x já está na tabela, adiciona seu novo índice 
            return -1 
        cont += 1 # conta os elementos da tabela
        if cont == M: return -2 # tabela cheia
        i = (i + k) % M # tabela circular
    # achamos uma posição livre - coloque x nesta posição junto da sua posição na tabela original
    a[i] = [x, ind]
    return i


def busca_hash(a, x):
    M = len(a)
    cont = 0
    i = hash(x, M)
    k = hash2(M)
    # procura x a partir da posição i
    while a[i] == None or a[i][0] != x:
        if a[i] == None: return -1, cont # não achou x, pois há uma vazia
        cont += 1 # conta os elementos da tabela
        if cont == M: return -2, cont; # a tabela está cheia
        i = (i + k) % M # tabela circular
    # encontrou
    return i, cont # devolve o índice do valor na tabela hash e a quantidade de comparações feitas para encontrá-lo


def main():
    prep = ['da', 'de', 'do', 'e', 'dos', 'das', 'del']
    while True:
         # Pedir o nome do arquivo de origem (‘fim’: break)
        arq = input('Nome do arquivo de origem: ')
        if arq == 'fim': 
            break
        else:
            arq = open(arq, 'r')
             # Ler o arquivo de origem e colocar em TABarq
            TABarq = func(arq)
            tmax = len(TABarq)*len(TABarq[0][1]) 
            TAB = tmax * [None] # cria a tabela hash
            for k in range(len(TABarq)):
                for j in range(len(TABarq[k][1])):
                    if TABarq[k][1][j] not in prep:
                        insere_hash(TAB, TABarq[k][1][j], k) # insere os nomes - desconsidera preposições
        
        while True:
            search = str.capitalize(input('\nProcurar nome: ')) # capitalize ajusta o valor de maiúsculas e minúsculas - preposições não são capitalizadas, portanto não serão encontradas
            if search == 'Fim':
                arq.close() # fecha o arquivo para abrir um próximo
                break
            else:
                print()
                aux = busca_hash(TAB, search)[0]
                if aux >= 0: # se encontrar o nome
                    linhas = TAB[aux] # imprime as linhas da tabela original em que o nome aparece
                    for k in range(1, len(linhas)): 
                        info = TABarq[linhas[k]]
                        print(f'{info[0]},', end='')
                        for j in range(len(info[1])):
                            print(f' {info[1][j]}', end='') 
                        print(f', {info[2]}')

                else:
                    print('Valor não encontrado.') 
                print(f'\n* * * {busca_hash(TAB, search)[1] + 1} comparações para localizar os nomes') # quantas comparações foram feitas
main()
