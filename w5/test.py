def kadane(arr):
    currentMax = arr[0]
    globalMax = arr[0]

    for i in range(1,len(arr)):
        currentMax = max(arr[i], arr[i]+currentMax)
        if currentMax > globalMax:
            globalMax = currentMax
        
    return globalMax

arr = [-2,1,-3,4,-1,2,1,-5,4]
result = kadane(arr)
print(result)