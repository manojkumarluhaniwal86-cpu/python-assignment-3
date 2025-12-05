def factorial(n):
    result = 1
    if n < 0:
        return "Factorial does not exist for negative numbers"
    else:
        for i in range(1, n + 1):
            result *= i
        return result

# calling the function with sample number
number = 5
print(f"Factorial of {number} is: {factorial(number)}")
