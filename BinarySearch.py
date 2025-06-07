def binary_search(arr, target, index):
    if len(arr) == 0:
        print("Not found")
        return False

    num_elements = len(arr)
    index += 1
    mid_num = num_elements // 2
    pointer = arr[mid_num]

    print(f"Checking {pointer} at step {index}")

    if pointer == target:
        print(f"Found it after {index} step(s). The number was {target}")
        return True
    elif pointer > target:
        return binary_search(arr[:mid_num], target, index)
    else:
        return binary_search(arr[mid_num+1:], target, index)


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70
result = binary_search(arr, target, index=0)

if result:
    print("Found it!")
else:
    print("Target not found.")
