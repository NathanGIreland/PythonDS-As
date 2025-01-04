def insertionSort(L, n):
    for i in range(n):        
        key = L[i]
        j = i - 1
        
        while j >= 0 and L[j] > key:
            L[j+ 1] = L[j]
            j = j - 1
        
        L[j + 1] = key
        
    return L
    
def printPedmas(L):
    pedmas = {6: 'Please', 7: 'Excuse', 9: 'My', 12: 'Dear', 30: 'Aunt', 70: 'Sally'}
    
    i = 0
    for key in L:
        if key in pedmas:
            i = i + 1
            print(i,'. ', pedmas[key])
        
    

unsortedList = [70, 9, 12, 7, 6, 30]    
print('Unsorted PEDMAS: ')
printPedmas(unsortedList)

print('\n -------- \n')

print('Sorted PEDMAS: ')
printPedmas(insertionSort(unsortedList, len(unsortedList)))



        