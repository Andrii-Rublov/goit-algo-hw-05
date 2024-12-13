

#Function closure for Fibonacci sequence calculation

def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <= 0: 
            return 0 #seed value for F0 = 0
        elif n == 1:
            return 1 #seed value for F1 = 1
        elif n in cache: # condition if the value is already in cache
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        print(f'{n} is not in cache yet') #these prints are only for visual checking of cache usage 
        #print(cache)
        return cache[n]      
       
    return fibonacci

fib = caching_fibonacci()

#Checking the function
print(fib(10))
print(fib(15))
print(fib(9))
print(fib(11))
print(fib(16))

