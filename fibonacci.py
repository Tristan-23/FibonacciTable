def fibonacci(n):
    fib_sequence = []
    a, b = 1, 2
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Voer een getal in voor de Fibonacci-reeks: "))
print(fibonacci(n))
