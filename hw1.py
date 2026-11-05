def caching_fibonacci():

    def fibonacci(n):
        if n <= 0:
            return 0

        if n == 1:
            return 1

        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(15))
