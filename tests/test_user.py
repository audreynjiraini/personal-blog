import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(id = 3, username = 'audrey', email = 'audreynjiraini@gmail.com', password_hash = 'banana', profile_pic_path = 'default.jpeg', bio = 'Beyonce is the queen')
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))
        
        
    def tearDown(self):
        User.query.delete()
        
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)
        
    def test_no_access_password(self): # confirms that our application raises an attribute error when we try and access the password property.
        
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_password_verification(self): # confirms that our password_hash can be verified when we pass in the correct password.
        
        self.assertTrue(self.new_user.verify_password('banana'))
        
        
    