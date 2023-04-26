#Program for Insertion Sort
#Function for Insertion Soort
def InsertionSort(arr):
    for i in range(1,len(arr)):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=k
    return arr
arr=[13,11,5,7,8,10]
list1=InsertionSort(arr)
print("Sorted Array:",list1)