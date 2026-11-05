def caching_fibonacci():

    cache = {}

    def fibonacci(n):
        """
        Calculate the nth Fibonacci number.

        """

        # Base cases
        if n <= 0:
            return 0

        if n == 1:
            return 1

        # Return cached result if available
        if n in cache:
            return cache[n]

        # Calculate recursively and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))
    print(fib(20))
