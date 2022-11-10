'''Selection Sort : selects the smallest element from an unsorted list in each iteration and places that element in beginning of unsorted list
    Jatin Kharbanda
    21104077
    Electrical

    '''


'''Algorithm : 
    selectionSort (array, size)

    repeat (size - 1) times
    
    set the first unsorted element as the minimum
    
    for each of the unsorted elements
    
        if element < currentMinimum
        set element as new minimum
        
    swap minimum with first unsorted position
    
    end selectionSort'''


# Selection Sort code in python :


def selectionSort(array, size):
    n=0
    swaps=0

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            n+=1
            

            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        print(f'the list after {step} comparisions is: \n', array)
        print()

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        swaps+=1
    return n,swaps


print()
print("Selection Sorting")
print()
data = [4, 3, 5, 6, 1, 2]

size = len(data)
comp1,swaps1=selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

print()
print("**********************************************************************************")

'''Bubble Sorting : Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order'''

'''Algorithm :
    bubbleSort(array)
    
    for i <- 1 to indexOfLastUnsortedElement-1
    
        if leftElement > rightElement
        
        swap leftElement and rightElement
        
    end bubbleSort'''

# Bubble sort Code in Python
print()
print("Bubble Sorting : ")


def bubbleSort(array):
    n=0
    swaps=0
    

    # loop to access each array element
    
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            n+=1

            # compare two adjacent elements
            if array[j] > array[j + 1]:

                # swapping elements if elements are not in the intended order

                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swaps+=1
        print()
        print(f'The list after {i+1} comparisions is: \n', array)
        print()
        
        
        
        print()
    return n,swaps
    


data = [4, 3, 5, 6, 1, 2]


comp2,swaps2=bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

'''
Comparision

1. Number of comparisions in Both'''
print()
print("Comparisions in Selection sort = ",comp1,'\n',"Comparisions in bubble sort = ",comp2)

#2. Number of swaps : 
print()
print("Swaps in selection sort = ",swaps1, "\nswaps in Bubble sort = ",swaps2)

# 3. Both of them are in place as no extra memory is required for them, the array gets sorted in itself
