# O(n²)

def bubbleSort(vetor):

    for final in range(len(vetor), 0, -1):
        troca = False

        for atual in range(0, final - 1):
            if vetor[atual] > vetor[atual + 1]:
                vetor[atual + 1], vetor[atual] = vetor[atual], vetor[atual + 1]
                troca = True

        if not troca:
            break

    print(vetor)

def bubbleSortDescrescente(vetor):

    for final in range(len(vetor), 0, -1):
        troca = False

        for atual in range(0, final - 1):
            if vetor[atual] < vetor[atual + 1]:
                vetor[atual + 1], vetor[atual] = vetor[atual], vetor[atual + 1]
                troca = True

        if not troca:
            break

    print(vetor)



if __name__ == "__main__":

    vetor = [1, 2, 2, 35 , 37, 89, 23, 9, 10]

    bubbleSort(vetor)
    bubbleSortDescrescente(vetor)