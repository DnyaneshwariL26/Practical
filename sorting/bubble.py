def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"Swapping {arr[j]} with {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        print(f"Step {i + 1}: {arr}")
        if not swapped:
            break  # Optimization: If no swaps, array is sorted

# Taking user input
arr = list(map(int, input("Enter numbers separated by space: ").split())) 
print("Initial array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
