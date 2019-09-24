import unittest
from app.models import Subscriber,User
from app import db

class SubscriberModelTest(unittest.TestCase):
    '''
   Test Class to test the behaviour of the Subscriber class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_subscriber = Comment(id = 1, email = 'audreynjiraini@gmail.com')
        
        
    def tearDown(self):
        Comment.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscriber,Comment))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_subscriber.id,3)
        self.assertEquals(self.new_subscriber.email,'audreynjiraini@gmail.com')


    def test-save_subscriber(self):
        self.new_subscriber.save_subscribernew_subscriber()
        self.assertTrue(len(Subscriber.query.all())>0)