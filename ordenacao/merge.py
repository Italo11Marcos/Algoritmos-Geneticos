# O(nlogn)

def mergeSort(vetor):
    if len(vetor) > 1:
        mid = len(vetor) // 2
        left = vetor[:mid]
        right = vetor[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              vetor[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                vetor[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            vetor[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            vetor[k]=right[j]
            j += 1
            k += 1

if __name__ == "__main__":

    vetor = [1, 2, 2, 35 , 37, 89, 23, 9, 10]

    mergeSort(vetor)

    print(vetor)