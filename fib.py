#name: Cassidy Ward
#date: 10/19/2021
#description: the program takes a
#positive integer parameter and returns the number at that position of the Fibonacci sequence

def fib(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        lst = [1,1]
        for i in range(2,n):
            lst.append(lst[i-1]+lst[i-2])
        return lst[n-1]
