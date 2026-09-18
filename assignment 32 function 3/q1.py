n=7
def nthFibonacci( n):

    # base case
    if n <= 1:
        return n
    # sum of the two preceding 
    #Fibonacci numbers
    return nthFibonacci(n - 1) + nthFibonacci(n - 2)
for i in range(n):
  print(nthFibonacci(i))
