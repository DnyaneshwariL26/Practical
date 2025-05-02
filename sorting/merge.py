def merge_sort(arr, step=[1]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, step)
        merge_sort(right, step)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        print(f"Step {step[0]}: {arr}")
        step[0] += 1

# Taking user input
arr = list(map(int, input("Enter numbers separated by space: ").split())) 
print("Initial array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
