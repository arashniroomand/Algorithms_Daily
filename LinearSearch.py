def linear_search(arr, index):
    for num in arr:
        if num == target:
            return 1, index
        index += 1

        
        

arr= [10, 50, 30, 70, 80, 20, 90, 40]
target = 30
result, step = linear_search(arr,index = 1)
if result == 1:
    print(f"The target found after {step} step ")