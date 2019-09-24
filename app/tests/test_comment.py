import unittest
from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):
    '''
   Test Class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_comment = Comment(id = 3, comment = 'Testing', posted = 2019/9/23, user_id = 3, blog_id = 1)
        
        
    def tearDown(self):
        Comment.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,3)
        self.assertEquals(self.new_comment.comment,'Testing')
        self.assertEquals(self.new_comment.posted,2019/9/23)
        self.assertEquals(self.new_comment.user_id,3)
        self.assertEquals(self.new_comment.blog_id,1)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(3)
        self.assertTrue(len(got_comments) == 1)
        
