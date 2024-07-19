```python
# Global memoization dictionary
memo = { 0: 0, 1: 1}

def fibonacci(n):
    if n <= 1:
        return n     
    return fib(n-1) + fib(n-2)

# Example usage
n = 10
print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")
```
