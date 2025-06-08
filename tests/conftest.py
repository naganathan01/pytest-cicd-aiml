import pytest
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator, MathUtils

@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance"""
    return Calculator()

@pytest.fixture
def sample_data():
    """Fixture that provides test data"""
    return {
        'positive_numbers': [1, 2, 3, 4, 5],
        'negative_numbers': [-1, -2, -3, -4, -5],
        'zero': 0,
        'large_numbers': [1000, 2000, 3000],
        'decimals': [1.5, 2.7, 3.14, 0.5]
    }

@pytest.fixture
def math_utils():
    """Fixture that provides MathUtils instance"""
    return MathUtils()

@pytest.fixture(scope="session")
def test_config():
    """Session-wide configuration fixture"""
    return {
        'api_base_url': 'https://jsonplaceholder.typicode.com',
        'timeout': 30,
        'retries': 3
    }
