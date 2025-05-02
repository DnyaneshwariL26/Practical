def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap elements and display the swap action
        if min_index != i:
            print(f"Swapping {arr[i]} with {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Show array state after each pass
        print(f"Step {i + 1}: {arr}")

# Taking user input
arr = list(map(int, input("Enter numbers separated by space: ").split())) 
print("Initial array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
