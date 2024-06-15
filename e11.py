def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")
