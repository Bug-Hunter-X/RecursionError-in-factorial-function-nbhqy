def factorial(n):
    if n == 0:
        return 1
    elif n > 100:  # Prevent excessive recursion
        raise ValueError("Factorial for large numbers may overflow.")
    else:
        return n * factorial(n-1)

number = 5
result = factorial(number)
print(result) 