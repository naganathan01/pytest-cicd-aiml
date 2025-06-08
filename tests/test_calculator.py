import pytest
from calculator import Calculator, add_numbers, multiply_numbers, MathUtils

class TestCalculator:
    """Test class for Calculator"""
    
    def test_addition(self, calculator):
        """Test addition functionality"""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
        assert calculator.add(-5, -3) == -8
    
    def test_subtraction(self, calculator):
        """Test subtraction functionality"""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 5) == -5
        assert calculator.subtract(-3, -2) == -1
    
    def test_multiplication(self, calculator):
        """Test multiplication functionality"""
        assert calculator.multiply(3, 4) == 12
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(0, 5) == 0
    
    def test_division(self, calculator):
        """Test division functionality"""
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(9, 3) == 3
        assert calculator.divide(-8, 2) == -4
    
    def test_division_by_zero(self, calculator):
        """Test division by zero raises exception"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)
    
    def test_power(self, calculator):
        """Test power functionality"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 2) == 25
        assert calculator.power(10, 0) == 1

class TestSimpleFunctions:
    """Test simple standalone functions"""
    
    def test_add_numbers(self):
        """Test add_numbers function"""
        assert add_numbers(2, 3) == 5
        assert add_numbers(-1, 1) == 0
        assert add_numbers(0, 0) == 0
    
    def test_multiply_numbers(self):
        """Test multiply_numbers function"""
        assert multiply_numbers(3, 4) == 12
        assert multiply_numbers(-2, 3) == -6
        assert multiply_numbers(0, 5) == 0

class TestMathUtils:
    """Test MathUtils class"""
    
    def test_factorial(self, math_utils):
        """Test factorial calculation"""
        assert math_utils.factorial(0) == 1
        assert math_utils.factorial(1) == 1
        assert math_utils.factorial(5) == 120
        assert math_utils.factorial(4) == 24
    
    def test_factorial_negative(self, math_utils):
        """Test factorial with negative number"""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            math_utils.factorial(-1)
    
    def test_is_prime(self, math_utils):
        """Test prime number detection"""
        assert math_utils.is_prime(2) == True
        assert math_utils.is_prime(3) == True
        assert math_utils.is_prime(17) == True
        assert math_utils.is_prime(4) == False
        assert math_utils.is_prime(1) == False
        assert math_utils.is_prime(0) == False

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (100, 200, 300),
])
def test_add_numbers_parametrized(a, b, expected):
    """Parametrized test for add_numbers function"""
    assert add_numbers(a, b) == expected

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, True),
    (17, True),
    (4, False),
    (9, False),
    (1, False),
])
def test_prime_numbers_parametrized(number, expected):
    """Parametrized test for prime number detection"""
    utils = MathUtils()
    assert utils.is_prime(number) == expected
