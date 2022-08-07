#Selection Sort program
def SelectionSort(arr,size):
    for i in range(size):
        min1=i
        for j in range(i+1,size):
            if (arr[j]<arr[min1]):
                min1=j
        (arr[i],arr[min1])=(arr[min1],arr[i])
    return arr
arr=[1,8,6,15,14,45,27,17]
size=len(arr)
list3=SelectionSort(arr,size)
print(list3)
