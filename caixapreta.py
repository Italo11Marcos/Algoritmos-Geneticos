from random import randint
from random import random
from matplotlib import pyplot as plt


def fitness(b):
    return 9 + b[1]*b[4]-b[22]*b[13]+b[23]*b[3]-b[20]*b[9]+\
        b[35]*b[14]-b[10]*b[25]+b[15]*b[16]+b[2]*b[32]+\
        b[27]*b[18]+b[11]*b[33]-b[30]*b[31]-b[21]*b[24]+\
        b[34]*b[26]-b[28]*b[6]+b[7]*b[12]-b[5]*b[8]+b[17]*b[19]-\
        b[0]*b[29]+b[22]*b[3]+b[20]*b[14]+b[25]*b[15]+b[30]*b[11]+\
        b[24]*b[18]+b[6]*b[7]+b[8]*b[17]+b[0]*b[32]

        
def inicializa(N, l):
    P = []
    for i in range(N):
        s = [randint(0,1) for j in range(l)]
        P.append(s)
    return P

def avalia(P):
    for i in P:
        i.append(fitness(i))
    return P

def cruzamento(S, N, l):
    Q = []
    i = 0

    while i < N:
        p1, p2 = randint(0, N-1), randint(0, N-1)
        f1, f2 = twoPC(S[p1], S[p2], l)
        Q.append(f1)
        Q.append(f2)
        i += 2

    return Q

def torneio(P, N, l):
    
    S = []
    for i in range(N):
        S1, S2 = randint(0, N-1), randint(0, N-1)
        if P[S1][l] > P[S2][l]:
            S.append(P[S1])
        else:
            S.append(P[S2])
    return S

def twoPC(P1,P2,L):
        p,q = randint(0,L-1),randint(0,L-1)
        F1 = []
        F2 = []
        for i in range(L):
            if i <= p or i > q:
                F1.append(P1[i])
                F2.append(P2[i])
            else:
                F1.append(P2[i])
                F2.append(P1[i])
        return F1,F2
    
def onePC(P1,P2,L):
        q = randint(0,L-1)
        F1 = []
        F2 = []
        for i in range(L):
            if i <= q:
                F1.append(P2[i])
                F2.append(P1[i])
            else:
                F1.append(P1[i])
                F2.append(P2[i])
        return F1,F2

def cruzaUniforme(P1, P2, l):
    F1 = []
    F2 = []

    for i in range(l):
        if random() <= 0.5:
            F1.append(P1[i])
            F2.append(P2[i])
        else:
            F1.append(P2[i])
            F2.append(P1[i])
    return F1, F2

def mutationBitABit(Q, Pm, N, l):
    for i in range(N):
        for j in range(l):
            if random() <= Pm:
                Q[i][j] = 1 - Q[i][j]
    return Q

def elitismo(S, Qm):
    P = []
    cont = 0
    
    for i in range(len(S)):
        if (S[i][-1] > Qm[i][-1]) and cont < 6:
            P.append(S[i])
            cont += 1
        else:
            P.append(Qm[-1])
    
    return P

def calcula_pi(P):
        tt = sum([i[-1] for i in P])
        pi = [i[-1]/tt for i in P]
        return pi

def roleta(P,N):
    tt = calcula_pi(P)
    ttAc = 0
    PttAc = []
    for i in range(N):
        ttAc += tt[i]
        PttAc.append(ttAc)
    Q = []
    for i in range(N):
        t = random()
        for j in range(N):            
            if PttAc[j] > t:
                Q.append(P[j])
                break
    return Q

def GA():
    
    t = 0               # Contador de gerações
    parada = 50         # Critério de parada
    N = 20              # Tamanho da população
    l = 36              # Tamanho de cada indivíduo (bits)
    Pm = 1/l            # Probabilidade de mutação
    max_geracao = []    # Maior fitness de cada geração
    
    
    P = inicializa(N, l)
    P = avalia(P)
    
    while (t < parada):
        
        S = torneio(P, N, l)
        #S = roleta(P, N)
        Q = cruzamento(P, N, l)
        Qm = mutationBitABit(Q, Pm, N, l)
        Qm = avalia(Qm)
        P = elitismo(S, Qm)
        
        max_geracao.append(max(P, key = lambda x: x[-1])[-1])
        
        t += 1
        
    plt.plot(range(t), sorted(max_geracao))
    plt.title('Processo Evolutivo - Caixa Preta')
    plt.ylabel('Fitness')
    plt.xlabel('Gerações')
    plt.legend(loc='lower right')
    plt.show()
        
    #return max(max_geracao, key = lambda x: x[-1])[-1]
    

GA()
"""        
resultado_final = []
for i in range(100):
    x = GA_Simples()
    resultado_final.append(x)
    
print(resultado_final)
plt.plot(range(100), resultado_final)
plt.title('Processo Evolutivo - Caixa Preta')
plt.ylabel('Fitness')
plt.xlabel('Gerações')
plt.legend(loc='lower right')
plt.show()
"""