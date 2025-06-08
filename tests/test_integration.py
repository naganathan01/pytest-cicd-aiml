import pytest
from calculator import Calculator, MathUtils

@pytest.mark.integration
class TestCalculatorIntegration:
    """Integration tests for calculator components"""
    
    def test_calculator_with_math_utils(self):
        """Test integration between Calculator and MathUtils"""
        calc = Calculator()
        utils = MathUtils()
        
        # Test complex calculation workflow
        base = 5
        exponent = 3
        result = calc.power(base, exponent)  # 5^3 = 125
        
        # Check if result is prime (125 is not prime)
        is_prime = utils.is_prime(result)
        assert is_prime == False
        
        # Calculate factorial of base (5! = 120)
        factorial_result = utils.factorial(base)
        assert factorial_result == 120
        
        # Add factorial to power result
        final_result = calc.add(result, factorial_result)  # 125 + 120 = 245
        assert final_result == 245
    
    def test_error_handling_integration(self):
        """Test error handling across components"""
        calc = Calculator()
        utils = MathUtils()
        
        # Test division by zero
        with pytest.raises(ValueError):
            calc.divide(10, 0)
        
        # Test negative factorial
        with pytest.raises(ValueError):
            utils.factorial(-5)
    
    @pytest.mark.slow
    def test_performance_integration(self):
        """Test performance with large numbers"""
        calc = Calculator()
        utils = MathUtils()
        
        # Test with larger numbers
        large_num1 = 1000
        large_num2 = 2000
        
        result = calc.multiply(large_num1, large_num2)
        assert result == 2000000
        
        # Test prime checking with reasonable size
        assert utils.is_prime(97) == True  # 97 is prime
        assert utils.is_prime(100) == False  # 100 is not prime

@pytest.mark.integration
@pytest.mark.slow
class TestComplexWorkflows:
    """Complex workflow integration tests"""
    
    def test_mathematical_workflow(self):
        """Test complex mathematical workflow"""
        calc = Calculator()
        utils = MathUtils()
        
        numbers = [2, 3, 5, 7, 11]  # Prime numbers
        
        # Verify all are prime
        for num in numbers:
            assert utils.is_prime(num) == True
        
        # Calculate sum using calculator
        total = 0
        for num in numbers:
            total = calc.add(total, num)
        
        assert total == 28  # Sum of first 5 primes
        
        # Calculate factorial of count
        count_factorial = utils.factorial(len(numbers))
        assert count_factorial == 120  # 5! = 120
        
        # Final calculation
        final = calc.multiply(total, 2)  # 28 * 2 = 56
        assert final == 56
