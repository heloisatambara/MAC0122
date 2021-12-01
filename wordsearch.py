from time import time

def bpNORMAL(a, b):
    m, n = len(a), len(b)
    conta = 0
    for k in range(n - m + 1):
        i, j = 0, k
        while i < m:
            print(i, j)
            if a[i] != b[j]: break
            i, j = i + 1, j + 1
        if i == m: conta += 1
    return conta


def bpBM1(a, b):
    m, n = len(a), len(b)
    conta = 0
    # tabela de últimas ocorrências de cada caractere em a
    ult = [-1] * 256
    # varrer a e definir as últimas ocorrências de cada caractere
    for k in range(m): ult[ord(a[k])] = k
    # procura a em b - da esquerda para a direita
    k = m - 1
    while k < n:
        j, i = k, m - 1
        while i >= 0:
            if a[i] != b[j]: break
            j, i = j - 1, i - 1
        # comparação chegou ao fim
        if i < 0: conta += 1
        # caso particular - se k é n-1 (último de b)
        # então k+1 é índice inválido
        # o if abaixo evita esse caso
        if k + 1 >= n: break
        # desloca baseado no valor de b[k+1]
        k = k + m - ult[ord(b[k+1])]
    return conta

def main():
    while True:
        b = input('Entre com o nome do arquivo de texto (# para fechar o programa): ')
        if b =='#':
            break
        b = open(arq, 'r')
        while True:
            a = input('Entre com a palavra a procurar (# para escolher outro arquivo): ')
            if a == '#':
                break
            t0 = time()
            co = b.count(a)
            tc = time() - t0
            print(f'count: Encontrada {co} vezes em {tc} segundos.')
            t0 = time()
            no = bpNORMAL(a, b)
            tn = time() - t0
            print(f'count: Encontrada {no} vezes em {tn} segundos.')
            t0 = time()
            bm = bpBM1(a, b)
            tb = time() - t0
            print(f'count: Encontrada {bm} vezes em {tb} segundos.')
