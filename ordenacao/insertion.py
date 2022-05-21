# O(n²)

def insertionSort(vetor):

    for i in range(len(vetor)):
        atual = vetor[i]

        while i > 0 and vetor[i - 1] > atual:
            vetor[i] = vetor[i - 1]
            i -= 1
        
        vetor[i] = atual
        
    print(vetor)

def insertionSortDecrescente(vetor):

    for i in range(len(vetor)):
        atual = vetor[i]

        while i > 0 and vetor[i - 1] < atual:
            vetor[i] = vetor[i - 1]
            i -= 1
        
        vetor[i] = atual
        
    print(vetor)


if __name__ == "__main__":

    vetor = [1, 2, 2, 35 , 37, 89, 23, 9, 10]

    insertionSort(vetor)
    insertionSortDecrescente(vetor)