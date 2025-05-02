def selection_sort(arr):#which takes an array (list) as input.
    n = len(arr)#Stores the number of elements in the list.
    for i in range(n):
        min_index = i #Assumes the current element (arr[i]) is the smallest.
        for j in range(i + 1, n):#Compares all elements after the current position (i).
                                #Updates min_index if a smaller element is found.
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap elements
        #Moves the smallest element to its correct position.

# Taking user input
arr = list(map(int, input("Enter numbers separated by space: ").split())) #Converts input into a list of integers
selection_sort(arr)#Calls the sorting function
print("Sorted array:", arr)
