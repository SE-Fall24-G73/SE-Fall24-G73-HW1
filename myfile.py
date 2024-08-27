def insertionSort(array):
    size = len(array)

    if size<=1:
        return
    
    for i in range (1, size):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

array = [14, 12, 10, 8, 6, 4, 2, 0, -2]
insertionSort(array)
print(array)
