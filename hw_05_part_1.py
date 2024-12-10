

#Function closure for Fibonacci sequence calculation

def caching_fibonacci(n, cache = {}):
    def fibonacci(n):
        if n <= 0: 
            return 0 #seed value for F0 = 0
        elif n == 1:
            return 1 #seed value for F1 = 1
        elif n in cache: # condition if the value is already in cache
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        print(f'{n} is not in cache yet') #these prints are only for visual checking og cache usage 
        #print(cache)
        return cache[n]      
       
    return fibonacci(n) 

#Checking the function
print(caching_fibonacci(10))
print(caching_fibonacci(15))
print(caching_fibonacci(9))
print(caching_fibonacci(11))
print(caching_fibonacci(16))

