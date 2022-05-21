# O(n²)

def selectionSort(vetor):

    for index in range(len(vetor)):
        min_index = index

        for elemento in range(index + 1, len(vetor)):
            if vetor[elemento] < vetor[min_index]:
                min_index = elemento

        vetor[index], vetor[min_index] = vetor[min_index], vetor[index]

    print(vetor)

def selectionSortDecrescente(vetor):

    for index in range(len(vetor)):
        max_index = index

        for elemento in range(index + 1, len(vetor)):
            if vetor[elemento] > vetor[max_index]:
                max_index = elemento

        vetor[index], vetor[max_index] = vetor[max_index], vetor[index]

    print(vetor)




if __name__ == "__main__":

    vetor = [1, 2, 2, 35 , 37, 89, 23, 9, 10]

    selectionSort(vetor)
    selectionSortDecrescente(vetor)