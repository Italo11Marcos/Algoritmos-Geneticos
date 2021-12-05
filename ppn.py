# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:26:36 2021

@author: italo
"""

from random import random, randint
from math import ceil
import numpy as np
from matplotlib import pyplot as plt

tamPOP = 100
N = 8
Pm = 1/N

def gera_pop():
    pop = []
    for i in range(tamPOP):
        S = [randint(1, 100) for i in range(N)]
        pop.append(S)
    return pop

def fitness4(p):
    p.sort(reverse=True)
    if(N == 4):
        p.append((p[0]+p[1]) - (p[2]+p[3]))
    else:
        p[4] = (p[0]+p[1]) - (p[2]+p[3])
def fitness5(p):
    p.sort(reverse=True)    
    if(N == 5):
        p.append((p[0]+p[1]) - (p[2]-p[3]+p[4]))
    else:
        p[5] = (p[0]+p[1]) - (p[2]+p[3]+p[4])
def fitness6(p):
    p.sort(reverse=True)
    if(N == 6):
        p.append((p[0]+p[1]-p[2]) - (p[3]+p[4]+p[5]))
    else:
        p[6] = (p[0]+p[1]+p[2]) - (p[3]+p[4]+p[5])
def fitness7(p):
    p.sort(reverse=True)
    if(N == 7):
        p.append((p[0]+p[1]+p[2]) - (p[3]+p[4]+p[5]+p[6]))
    else:
        p[7] = ((p[0]+p[1]+p[2]) - (p[3]+p[4]+p[5]+p[6]))
def fitness8(p):
    p.sort(reverse=True)
    if(N == 8):
        p.append((p[0]+p[1]+p[2]+p[3]) - (p[4]+p[5]+p[6]+p[7]))
    else:
        p[8] = (p[0]+p[1]+p[2]+p[3]) - (p[4]+p[5]+p[6]+p[7])
  
def cruzamento(POP):
    Q = []
    for i in range(tamPOP):
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        """
        p, q = randint(0,N-1), randint(0,N-1)
        f = []
        for z in range(N):
            f.append(0)
        for j in range(N):
            if j <= p or j > q:
                f[j] = POP[p2][j]
            else:
                f[j] = POP[p1][j]       
        """
        """
        for z in range(N):
            f.append(0)
        for j in range(N):
            if random() < 0.5:
                f[j] = ceil(POP[p1][j] * random())
            else:
                f[j] = ceil(POP[p2][j] * random())"""
        f = [(POP[p1][j]+POP[p2][j])//2 for j in range(N)]
        Q.append(f)
    return Q

def mutacao(POP):
    for i in range(tamPOP):
        for j in range(N):
            if random() < Pm:
                p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
                POP[p1][j] = POP[p2][j]
                
                
def selecao(POP):
    S = []
    for i in range(tamPOP):
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        if abs(POP[p1][-1]) <= abs(POP[p2][-1]):
            S.append(POP[p1])
        else:
            S.append(POP[p2])
    return S

def elitismo(P, Q):
    P = sorted(P, key=lambda x: x[-1], reverse=True)
    Q = sorted(Q, key=lambda x: x[-1])
    for i in range(tamPOP//2):
        P[i] = Q[i]
    return P

def GA():
    
    stop = 50
    i = 0
    
    P = gera_pop()
    
    for p in P:
        fitness8(p)
        
    resultados = []
    
    while(i < stop):
    
        S = selecao(P)

        Q = cruzamento(S)

        mutacao(Q)

        for q in Q:
            fitness8(q)

        P = elitismo(P, Q)
    
        
        resultados.append(min(P, key = lambda x: abs(x[-1])))
        
        i += 1
        
    return(min(resultados, key = lambda x: abs(x[-1])))
    

resultados_finais = []

for i in range(100):
    x = GA()
    resultados_finais.append(x)
    
best = min(resultados_finais, key = lambda x: abs(x[-1]))
media = sum([p[-1] for p in resultados_finais])//100
resultados = []
for p in resultados_finais:
    resultados.append(p[-1])
print(media, best)
  
#plt.plot(range(100), medias, '--',label='Média')
plt.plot(range(100), resultados, label='Melhor')
plt.title('Processo Evolutivo PPN ({})'.format(N))
plt.ylabel('Fitness')
plt.xlabel('Execuções')
plt.legend(loc='lower right')
plt.show()
#print(resultados_finais)