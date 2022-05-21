from random import random, randint
import numpy as np
from matplotlib import pyplot as plt

tamPOP = 60
N = 8
Pm = 1/N

def gera_pop():
    pop = []
    for i in range(tamPOP):
        S = [randint(1, N) for i in range(N)]
        pop.append(S)
    return pop

def fitness(p):
    matriz = np.zeros([N,N])
    
    for i in range(N):
        matriz[i][p[i]-1] = 1
        
    columns = np.sum(matriz, 0)
    diagonals = [b.diagonal(i).sum() for b in (matriz, matriz[::-1]) for i in range(-N+1, N)]
    if N == 4:
        diagonals.pop(0)
        diagonals.pop(5)
        diagonals.pop(5)
        diagonals.pop(-1)
    elif N == 5:
        diagonals.pop(0)
        diagonals.pop(8)
        diagonals.pop(8)
        diagonals.pop(-1)
    elif N == 6:
        diagonals.pop(0)
        diagonals.pop(10)
        diagonals.pop(10)
        diagonals.pop(-1)
    elif N == 7:
        diagonals.pop(0)
        diagonals.pop(12)
        diagonals.pop(12)
        diagonals.pop(-1)
    elif N == 8:
        diagonals.pop(0)
        diagonals.pop(14)
        diagonals.pop(14)
        diagonals.pop(-1)
    conflitos_columns = 0
    conflitos_diagonals = 0

    for i in columns:    
        if i>1:
            conflitos_columns += i

    for i in diagonals:
        if i>1:
            conflitos_diagonals += i

    total_conflitos = conflitos_columns + conflitos_diagonals

    p.append(total_conflitos)

def torneio(P):
    S = []
    for i in range(tamPOP):
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        if P[p1][-1] < P[p2][-1]:
            S.append(P[p1])
        else:
            S.append(P[p2])
    return S

def calcula_pi(P):
        tt = sum([p[-1] for p in P])
        pi = [p[-1]/tt for p in P]
        return pi

def roleta(P):
    tt = calcula_pi(P)
    ttAc = 0
    PttAc = []
    for i in range(tamPOP):
        ttAc += tt[i]
        PttAc.append(ttAc)
    S = []
    for i in range(tamPOP):
        t = random()
        for j in range(tamPOP):            
            if t < PttAc[j]:
                S.append(P[j])
                break
    return S

def cruzamento(POP):
    Q = []
    for i in range(tamPOP):
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        f = [(POP[p1][j]+POP[p2][j])//2 for j in range(N)]
        Q.append(f)
    return Q

def mutacao(POP):
    for i in range(tamPOP):
        for j in range(N):
            if random() < Pm:
                POP[i][j] = randint(1,N-1)

def elitismo(P, Q):
    P = sorted(P, key=lambda x: x[-1], reverse=True)
    Q = sorted(Q, key=lambda x: x[-1])
    for i in range(tamPOP//2):
        P[i] = Q[i]
    return P


def ga():

    t = 50
    i = 0

    P = gera_pop()
    
    for p in P:
        fitness(p)

    resultados = []

    while(i<t):

        S = torneio(P)

        #S = roleta(P)

        Q = cruzamento(S)

        mutacao(Q)

        for q in Q:
            fitness(q)

        P = elitismo(P, Q)

        resultados.append(min(P, key = lambda x: x[-1]))
        
        i+=1

    #print(min(resultados, key = lambda x: x[-1]))
    return min(resultados, key = lambda x: x[-1])

resultados_finais = []

for i in range(100):
    x = ga()
    resultados_finais.append(x)
    
best = min(resultados_finais, key = lambda x: x[-1])
media = sum([p[-1] for p in resultados_finais])//100
resultados = []
for p in resultados_finais:
    resultados.append(p[-1])
#resultados = sorted(resultados, reverse=True)
print(media, best)
  
#plt.plot(range(100), medias, '--',label='Média')
plt.plot(range(100), resultados, label='Melhor')
plt.title('Processo Evolutivo ({} Rainhas)'.format(N))
plt.ylabel('Fitness')
plt.xlabel('Gerações')
plt.legend(loc='lower right')
plt.show()
#print(resultados_finais)