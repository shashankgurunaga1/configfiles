#Finding all the prime factors using Sieve of Eratosthenes
def SieveofEratosthenes(n):
    prime=[]
    list1=[]
    for i in range(n+1):
        prime.append(True)
    for j in range(2,n):
         if (prime[j]==True):
            for k in range(j*j,n+1,j):
                prime[k]=False
    for l in range(2,n):
        if prime[l]:
            list1.append(l)
    return list1 # returns the array/list of all prime numbers till the number n
n=int(input("Enter the number till which you  have to get all prime numbers using Sieve of Eratosthes"))
output=SieveofEratosthenes(n)
print(output)


    