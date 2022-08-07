def isEmpty(queue):
    if (len(queue)==0):
        return True
    else:
        return False
def enqueue(queue,itm):
    queue.append(itm)
    if(len(queue)==1):
        front=0
        back=0
    else:
        back=len(queue)-1
def dequeue(queue):
   
    if isEmpty(queue):
        return "Not possible"
    else:
        itm=queue.pop(0)
        if(len(queue)==0):
            front=back=None
    return itm
def peek(queue):
    if isEmpty(queue):
        return "Nothing"
    else:
        front=0
    return queue[front]


def display(queue):
    if isEmpty(queue):
        print("Queue is Empty")
    else:
        front=0
        back=len(queue)-1
        print("Front->",queue[front])
        for i in range(1,back):
            print(queue[i])
#_____main_____
queue=[]
front=None
while True:
    print("QUEUE OPERATIONS")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. Peek")
    print("4. Display the Queue")
    print("5. Exit")
    option=int(input("Enter the choice"))
    if(option==1):
        item=int(input("Enter the number you want to put in the queue"))
        enqueue(queue,item)
    elif(option==2):
        output=dequeue(queue)
        if(output=="Not possible"):
            print("Queue is Empty")
        else:
            print("The popped element is ",output)
    elif(option==3):
        output=peek(queue)
        if (output=="Nothing"):
            print("Queue is Empty")
        else:
            print("The front element of the queue is ",output)
    elif(option==4):
        display(queue)
    elif(option==5):
        break
    else:
        print("Wrong Choice!")