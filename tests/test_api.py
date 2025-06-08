import pytest
import requests
from unittest.mock import Mock, patch

class TestAPI:
    """Test class for API endpoints"""
    
    def test_get_users(self, test_config):
        """Test getting users from API"""
        response = requests.get(f"{test_config['api_base_url']}/users")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
        assert 'name' in data[0]
        assert 'email' in data[0]
    
    def test_get_single_user(self, test_config):
        """Test getting a single user"""
        response = requests.get(f"{test_config['api_base_url']}/users/1")
        
        assert response.status_code == 200
        user = response.json()
        assert user['id'] == 1
        assert 'name' in user
        assert 'email' in user
    
    def test_create_post(self, test_config):
        """Test creating a new post"""
        payload = {
            'title': 'Test Post',
            'body': 'This is a test post created by pytest',
            'userId': 1
        }
        
        response = requests.post(
            f"{test_config['api_base_url']}/posts",
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == 'Test Post'
        assert 'id' in data
    
    def test_invalid_endpoint(self, test_config):
        """Test accessing invalid endpoint"""
        response = requests.get(f"{test_config['api_base_url']}/invalid")
        assert response.status_code == 404
    
    @patch('requests.get')
    def test_api_with_mock(self, mock_get):
        """Test API call with mocking"""
        # Mock the response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'id': 1,
            'name': 'Test User',
            'email': 'test@example.com'
        }
        mock_get.return_value = mock_response
        
        # Make the API call
        response = requests.get("https://api.example.com/users/1")
        
        # Assertions
        assert response.status_code == 200
        data = response.json()
        assert data['name'] == 'Test User'
        mock_get.assert_called_once_with("https://api.example.com/users/1")

@pytest.mark.integration
class TestAPIIntegration:
    """Integration tests for API"""
    
    def test_full_user_workflow(self, test_config):
        """Test complete user workflow"""
        # Get all users
        users_response = requests.get(f"{test_config['api_base_url']}/users")
        assert users_response.status_code == 200
        users = users_response.json()
        
        # Get first user details
        if users:
            user_id = users[0]['id']
            user_response = requests.get(f"{test_config['api_base_url']}/users/{user_id}")
            assert user_response.status_code == 200
            
            # Get user's posts
            posts_response = requests.get(f"{test_config['api_base_url']}/users/{user_id}/posts")
            assert posts_response.status_code == 200
