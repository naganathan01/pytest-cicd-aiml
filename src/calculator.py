class Calculator:
    """A simple calculator class for demonstration"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Calculate power of a number"""
        return base ** exponent

def add_numbers(a, b):
    """Simple function to add two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Simple function to multiply two numbers"""
    return a * b

class MathUtils:
    """Utility class for mathematical operations"""
    
    @staticmethod
    def factorial(n):
        """Calculate factorial of a number"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
