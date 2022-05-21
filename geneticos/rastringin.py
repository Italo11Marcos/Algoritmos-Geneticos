from random import random, randint
from math import cos, pi
from matplotlib import pyplot as plt

N = 3
xmin = -5.12
xmax = 5.12
tamPOP = 60
Pm = 1/N

def gera_pop():
    pop = []
    for i in range(tamPOP):
        S = [xmin + random() * (xmax - xmin) for i in range(N+1)]
        pop.append(S)
    return pop

def fitness(POP):
    for p in POP:
        r = 0
        for i in range(N):
            r += pow(p[i],2) - 10 * cos(2*pi*p[i])
        p.append((10 * N + r))

def calcula_pi(POP):
        tt = sum([p[-1] for p in POP])
        pi = [p[-1]/tt for p in POP]
        return pi

def roleta(POP):
    tt = calcula_pi(POP)
    ttAc = 0
    PttAc = []
    for i in range(tamPOP):
        ttAc += tt[i]
        PttAc.append(ttAc)
    Q = []
    for i in range(tamPOP):
        t = random()
        for j in range(tamPOP):            
            if t < PttAc[j]:
                Q.append(POP[j])
                break
    return Q

def torneio(POP):
    S = []
    for i in range(tamPOP):
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        if(POP[p1][-1] > POP[p2][-2]):
            S.append(POP[p1])
        else:
            S.append(POP[p2])
    return S

def cruzamento(POP):
    Q = []
    for i in range(tamPOP):
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        f = [(POP[p1][j]+POP[p2][j])/2 for j in range(N)]
        Q.append(f)
    return Q

def cruzamento1(POP):
    Q = []
    for i in range(tamPOP):
        f = POP[0]
        p1, p2 = randint(0,tamPOP-1), randint(0,tamPOP-1)
        for j in range(N):
            if random() < 0.5:
                f[j] = POP[p1][j] + (-0.5 + random() * (0.5 - -0.5)) * POP[p2][j]
            else:
                f[j] = POP[p1][j]
        Q.append(f)
    return Q


def mutacao(POP):
    for i in range(tamPOP):
        for j in range(N):
            if random() < Pm:
                POP[i][j] *= random()

def mutacao1(POP):
    for i in range(tamPOP):
        for j in range(N):
            if random() < Pm:
                POP[i][j] = xmin + random() * (xmax - xmin)

def mutacao2(POP):
    for i in range(tamPOP):
        for j in range(N):
            if random() < Pm:
                POP[i][j] += random()

def elitismo(P, Q):
    P = sorted(P, key=lambda x: x[-1], reverse=True)
    Q = sorted(Q, key=lambda x: x[-1])
    for i in range(tamPOP//2):
        P[i] = Q[i]
    return P


def elitismo2(P, Q):
    Pi = []
    cont = 0
    
    for i in range(tamPOP):
        if (P[i][-1] > Q[i][-1]) and cont < 6:
            Pi.append(P[i])
            cont += 1
        else:
            Pi.append(Q[i])
    
    return Pi

def GA1():

    t = 50
    i = 0

    resultados = []
    resultado_final = []

    for i in range(1):

        P = gera_pop()
        fitness(P)

        while i < t:
            S = torneio(P)
            #S = roleta(P)
            Q = cruzamento(S)
            mutacao(Q)
            fitness(Q)
            P = elitismo(P, Q)
            resultados.append(min(P, key = lambda x: x[-1]))

            i+=1

        resultado_final.append(min(resultados, key = lambda x: x[-1])[-1])

    return min(resultados, key = lambda x: x[-1])[-1]
    #print(resultado_final)

def GA():

    t = 100
    i = 0
    
    resultados = []
    
    P = gera_pop()
    fitness(P)
    
    while i < t:
            #S = torneio(P)
            S = roleta(P)
            Q = cruzamento(S)
            mutacao(Q)
            fitness(Q)
            P = elitismo(P, Q)
            resultados.append(min(P, key = lambda x: x[-1])[-1])

            i+=1  
    print(resultados)
    plt.plot(range(t), resultados)
    plt.title('Processo Evolutivo - Rastrigin')
    plt.ylabel('Fitness')
    plt.xlabel('Gerações')
    plt.legend(loc='lower right')
    plt.show()
            
    #return min(resultados, key = lambda x: x[-1])[-1]

GA()
"""
#GA1()


resultado_final = []
for i in range(100):
    x = GA1()
    resultado_final.append(x)
    
print(resultado_final)
plt.plot(range(100), sorted(resultado_final, reverse=True))
plt.title('Processo Evolutivo - Rastrigin')
plt.ylabel('Fitness')
plt.xlabel('Gerações')
plt.legend(loc='lower right')
plt.show()
"""