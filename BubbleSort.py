def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"{arr[j]} > {arr[j+1]} so we swap.")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(arr)
            else:
                print(f"{arr[j]} <= {arr[j+1]} so no swap needed.")
        print("End of pass", i + 1)
        print("------------------")
        if not swapped:
            print("No swaps done in this pass. List is sorted.")
            break
    return arr

print("Bubble Sort with explanation:")
sorted_arr = bubble_sort(arr)
print("Sorted list:", sorted_arr)
