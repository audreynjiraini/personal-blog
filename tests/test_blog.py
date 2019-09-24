import unittest
from app.models import Blog

class BlogModelTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(id = 1, post_id = 1, title = 'Python Must Be Crazy', body = 'A thrilling new Python Series', posted = 2019/9/23, likes = 0, dislikes = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
        
        
    def tearDown(self):
        Post.query.delete()
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,1)
        self.assertEquals(self.new_blog.post_id,1)
        self.assertEquals(self.new_blog.title,'Python Must Be Crazy')
        self.assertEquals(self.new_blog.body,'A thrilling new Python Series')
        self.assertEquals(self.new_blog.posted,2019/9/23)
        self.assertEquals(self.new_blog.likes,1)
        self.assertEquals(self.new_blog.dislikes,1')


    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blogs = Blog.get_blog(1)
        self.assertTrue(len(got_blogs) == 1)