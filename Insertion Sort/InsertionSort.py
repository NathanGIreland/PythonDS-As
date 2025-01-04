def insertionSort(L, n):
    for i in range(n):      
        key = L[i] ## Key = Value of the current biggest element in the array
        j = i - 1 ## j = The index of the value on the left of the biggest current element saved into a second pointer

        ## Loops while the second pointer, j, is bigger than -1 and the value is L[j] is bigger than key (current biggest)
        while j >= 0 and L[j] > key:
            L[j+ 1] = L[j] ## If L[j] is bigger than the key it places it to the right of the Key
            j = j - 1 ##Moves the j back into position of the current index in sorted portion
        
        L[j + 1] = key ##Places the key to the right of the last element in the sorted array
        
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



        
