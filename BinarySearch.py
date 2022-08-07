def BinarySearch(list1,item):
    
    u=len(list1)-1# last value in the list with highest index value
    begin=0
    while(begin<=u):
        mid=(begin+u)//2
        if(item==list1[mid]):
            return mid 
        elif(item>list1[mid]):
            begin=mid+1
        else:
            u=mid-1
    else:
        return False
list1=[1,2,3,4,5,6,7,8,9,10]
item=int(input("Enter the number you want to SEARCH!!!"))
index=BinarySearch(list1,item)
if(index):
    print("Element found at index value:",index,"Position:",index+1)
else:
    print("Sorry! Element Not Found")






