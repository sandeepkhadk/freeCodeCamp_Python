def fibonacci(n):
    sequence = [0, 1]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(n - 2):
        next_value = sequence[i] + sequence[i + 1]
        sequence.append(next_value)

    return sequence


n = int(input("Enter the value of n: "))

result = fibonacci(n)

print("The", n, "th Fibonacci series is:", result)