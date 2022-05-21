from random import randint, random
import numpy as np

pop = [[0,0,0,1,1], [0,0,1,0,2], [0,0,1,1,3], [0,1,0,0,4], [0,1,0,1,5], [0,1,1,0,6], [0,1,1,1,7], [1,0,0,0,8]]
npop = [[1,0,0,1], [1,1,0,1],[1,1,1,1],[1,1,0,0],[1,1,1,0],[1,0,1,0],[1,0,1,1],[0,0,0,0]]  #c[:4]

N = 8           #quantidade de rainhas
tamPOP = 20    #tamanho da população
Pm = 0.3        #probabilidade de mutacao

def gera_pop():
    P = []
    for i in range(tamPOP):
        S = []
        for j in range(N):
            x = randint(0,N-1)
            S.append(pop[x])
        P.append(S)
    return P

def bin_to_dec(p):
    i, inteiro = 0, 0
    while i < 4:
        inteiro += p[3-i] * pow(2,i)
        i += 1
    if inteiro > 8 or inteiro == 0:
        p = [0,0,1,0]
    else:
        p[4] = inteiro
        
def calcula_fitness(P):

    matriz = np.zeros([N,N])

    i = 0
    for p in P:
        matriz[i][p[-1] - 1] = 1
        i += 1

    columns = np.sum(matriz, 0)
    diagonals = [b.diagonal(i).sum() for b in (matriz, matriz[::-1]) for i in range(-N+1, N)]
    diagonals.pop(0)
    diagonals.pop(13)
    diagonals.pop(13)
    diagonals.pop(-1)
    
    conflitos_columns = 0
    conflitos_diagonals = 0

    for i in columns:
        if i>1:
            conflitos_columns += 1

    for i in diagonals:
        if i>1:
            conflitos_diagonals += 1

    total_conflitos = conflitos_columns + conflitos_diagonals

    P.append(total_conflitos)
 
def torneio(P):
    S = []
    for i in range(tamPOP):
        p1, p2 = randint(0,N-1), randint(0,N-1)
        if P[p1][-1] <= P[p2][-1]:
            S.append(P[p1])
        else:
            S.append(P[p2])
    return S

def cruzaUniforme(P1, P2):
        f1 = []
        f2 = []
        for i in range(N):
            p = random()
            if (p <= 0.3):
                f1.append(P1[i])
                f2.append(P2[i])
            else:
                f1.append(P2[i])
                f2.append(P1[i])
        return f1, f2

def cruzamento(S):
    Q = []
    i = 0

    while i < tamPOP:
        p1, p2 = randint(0, N-1), randint(0, N-1)
        f1, f2 = cruzaUniforme(S[p1], S[p2])
        Q.append(f1)
        Q.append(f2)
        i += 2

    return Q

def mutacao(Q):
    
    for i in range(tamPOP):
        for j in range(N):
            for k in range(4):
                if random() < Pm:
                    if Q[i][j][k] == 0:
                        Q[i][j][k] = 1
                    else:
                        Q[i][j][k] = 0
            if Q[i][j][:4] in npop:
                Q[i][j] = pop[randint(0,N-1)]

def elitismo(P, Q):
    P = sorted(P, key=lambda x: x[-1], reverse=True)
    Q = sorted(Q, key=lambda x: x[-1])
    for i in range(5):
        P[i] = Q[i]
    return P



def ga():
    #gera a população inicial
    P = gera_pop()

    #transforma de binario para inteiro
    for i in range(tamPOP):
        for j in range(N):
            bin_to_dec(P[i][j])

    #calcula o fitness
    for p in P:
        calcula_fitness(p)

    t = 100
    a = 0

    resultados = []

    while a < t:
        
        S = torneio(P)
        
        Q = cruzamento(S)

        mutacao(Q)
                
        for i in range(tamPOP):
            for j in range(N):
                bin_to_dec(Q[i][j])
                
        for q in Q:
            calcula_fitness(q)

        elitismo(P,Q)

        resultados.append(min(P, key = lambda x: x[-1]))

        a+=1

    print(min(resultados, key = lambda x: x[-1]))


ga()