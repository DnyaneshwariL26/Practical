def quick_sort(arr, low, high, step=[1]):
    if low < high:
        pivot_index = partition(arr, low, high)
        print(f"Pivot {arr[pivot_index]} placed at correct position")
        print(f"Step {step[0]}: {arr}")
        step[0] += 1
        
        quick_sort(arr, low, pivot_index - 1, step)
        quick_sort(arr, pivot_index + 1, high, step)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Swapping {arr[i]} with {arr[j]}")

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Taking user input
arr = list(map(int, input("Enter numbers separated by space: ").split())) 
print("Initial array:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
