import unittest
from unittest.mock import AsyncMock, patch

class UserProfileManager:
    def __init__(self):
        self.user_profiles = {}
        self.external_validation_service = ExternalValidationService()

class ExternalValidationService:
    async def validate(self, user_info):
        # Add your validation logic here
        pass

@patch('model_a_user_test.ExternalValidationService', autospec=True)
def test_user_profile_manager(mock_external_validation_service):
    mock_external_validation_service.return_value.validate.return_value = True
    # Your test cases here

    async def add_user(self, user_id, user_info):
        if user_id in self.user_profiles:
            raise ValueError("User already exists")
        validation_result = await self.external_validation_service.validate(user_info)
        if not validation_result:
            raise ValueError("User info validation failed")
        self.user_profiles[user_id] = user_info
        return "User added successfully"

    def update_user(self, user_id, user_info):
        if user_id not in self.user_profiles:
            raise KeyError("User does not exist")
        self.user_profiles[user_id] = user_info
        return "User updated successfully"

    def delete_user(self, user_id):
        if user_id not in self.user_profiles:
            raise KeyError("User does not exist")
        del self.user_profiles[user_id]
        return "User deleted successfully"

    async def merge_user_profiles(self, primary_user_id, secondary_user_id):
        if primary_user_id not in self.user_profiles or secondary_user_id not in self.user_profiles:
            raise KeyError("One or both users do not exist")
        primary_profile = self.user_profiles[primary_user_id]
        secondary_profile = self.user_profiles[secondary_user_id]
        merged_profile = {**secondary_profile, **primary_profile}  # Simplified merge strategy
        self.user_profiles[primary_user_id] = merged_profile
        del self.user_profiles[secondary_user_id]
        return "Profiles merged successfully"

class TestUserProfileManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserProfileManager()

    @patch.object(UserProfileManager, 'external_validation_service')
    def test_add_user_success(self, mock_validation_service):
        mock_validation_service.validate.return_value = True
        user_id = 1
        user_info = {'name': 'John Doe'}
        result = self.manager.add_user(user_id, user_info)
        self.assertEqual(result, "User added successfully")
        self.assertEqual(self.manager.user_profiles[user_id], user_info)

    @patch.object(UserProfileManager, 'external_validation_service')
    def test_add_user_exists(self, mock_validation_service):
        mock_validation_service.validate.return_value = True
        user_id = 1
        user_info = {'name': 'John Doe'}
        self.manager.add_user(user_id, user_info)
        with self.assertRaises(ValueError):
            self.manager.add_user(user_id, user_info)

    @patch.object(UserProfileManager, 'external_validation_service')
    async def test_add_user_validation_fails(self, mock_validation_service):
        mock_validation_service.validate.return_value = False
        user_id = 1
        user_info = {'name': 'John Doe'}
        with self.assertRaises(ValueError):
            await self.manager.add_user(user_id, user_info)

    def test_update_user_success(self):
        user_id = 1
        user_info = {'name': 'John Doe'}
        self.manager.user_profiles[user_id] = user_info
        updated_info = {'name': 'Jane Doe'}
        result = self.manager.update_user(user_id, updated_info)
        self.assertEqual(result, "User updated successfully")
        self.assertEqual(self.manager.user_profiles[user_id], updated_info)

    def test_update_user_not_exists(self):
        user_id = 1
        user_info = {'name': 'Jane Doe'}
        with self.assertRaises(KeyError):
            self.manager.update_user(user_id, user_info)

    def test_delete_user_success(self):
        user_id = 1
        user_info = {'name': 'John Doe'}
        self.manager.user_profiles[user_id] = user_info
        result = self.manager.delete_user(user_id)
        self.assertEqual(result, "User deleted successfully")
        self.assertNotIn(user_id, self.manager.user_profiles)

    def test_delete_user_not_exists(self):
        user_id = 1
        with self.assertRaises(KeyError):
            self.manager.delete_user(user_id)

    async def test_merge_user_profiles_success(self):
        primary_user_id = 1
        secondary_user_id = 2
        primary_profile = {'name': 'John Doe', 'email': 'john.doe@example.com'}
        secondary_profile = {'name': 'Jane Doe', 'age': 30}
        self.manager.user_profiles[primary_user_id] = primary_profile
        self.manager.user_profiles[secondary_user_id] = secondary_profile
        result = await self.manager.merge_user_profiles(primary_user_id, secondary_user_id)
        self.assertEqual(result, "Profiles merged successfully")
        expected_merged_profile = {'name': 'John Doe', 'email': 'john.doe@example.com', 'age': 30}
        self.assertEqual(self.manager.user_profiles[primary_user_id], expected_merged_profile)
        self.assertNotIn(secondary_user_id, self.manager.user_profiles)

    async def test_merge_user_profiles_not_exists(self):
        primary_user_id = 1
        secondary_user_id = 2
        with self.assertRaises(KeyError):
            await self.manager.merge_user_profiles(primary_user_id, secondary_user_id)

if __name__ == '__main__':
    unittest.main()
