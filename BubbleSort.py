#Bubble Sort Program
def BubbleSort(arr):
    n=len(arr)-1
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[24,21,45,17,38,46]
list2=BubbleSort(arr)
print("Sorted List:",list2)

