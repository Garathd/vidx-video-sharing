#!/usr/bin/env python
import unittest
import pymysql
import db

# Setting and Getting for test video id
video_id = ""

def setVideoId(set_id):
    global video_id
    video_id = set_id
        
def getVideoId():
    return video_id
    
class tests(unittest.TestCase):
    
    # Testing user info
    username = "Garath"
    password = "access"
    user_id = 1
    
    # Testing video info
    title = "Test123xyz"
    description = "Test123xyz"
    image = ""
    video = "http://youtube.com"
    category_id = 1
    origin = "true"
    category_name = "Music"
    

    """
    Testing setting and getting Login Name
    """
    
    def testA(self):
        db.setLogin(tests.username)
        self.assertEqual(tests.username, db.getLogin())
        
    
    """
    Testing register user
    """
    def testB(self):
        result = db.register(tests.username, tests.password)
        self.assertFalse(result)
        
    
    """
    Testing login user
    """
    def testC(self):
        result = db.authenticate(tests.username, tests.password)
        self.assertEqual(result[0], tests.username)
        
        
    """
    Testing get user id by username
    """
    def testD(self):
        result = int(db.getUserId(tests.username))
        self.assertGreater(result, 0)
         
        
    """
    Testing getting a users list of videos
    """    
    def testE(self):
        result = db.getMyVideos(tests.user_id)
        self.assertTrue(result)
        
        
    """
    Testing getting all the videos
    """    
    def testF(self):
        result = db.getOtherVideos(tests.user_id)
        self.assertTrue(result)
        
        
    """
    Testing Add a new video 
    """
    def testG(self):
        db.addVideo(tests.user_id, 
        tests.title, 
        tests.description, 
        tests.image, 
        tests.video, 
        tests.category_id, 
        tests.origin)
        
        dbc = db.database()
    
        try:
            with dbc.cursor(pymysql.cursors.DictCursor) as cursor:
              sql = "SELECT video_id FROM videos WHERE title = '{}'".format(tests.title)
              cursor.execute(sql)
              result = cursor.fetchone()
              
              # Setting the video id of test video
              video_id = result['video_id']
              setVideoId(video_id)
              
        except Exception as e:
            print(e)    
              
        finally:
            dbc.close()
            self.assertEqual(video_id, getVideoId())
            
            
    """
    Test get Video By ID  
    """
    def testH(self):
        value = db.getVideoById(getVideoId())
        self.assertTrue(value)        
            
            
    """
    Testing Edit video 
    """
    def testI(self):
        
        # Temporary data
        new_title = "Test"
        new_description = "Test"
        
        db.edit(
        getVideoId(), 
        new_title, 
        new_description, 
        tests.image, 
        tests.video, 
        tests.category_id)
        
        self.assertNotEqual(new_title, tests.title)
        
        
    """
    Testing order videos by category
    """
    def testJ(self):
        
        args = {
            'category_id': 1
        }
        
        result = db.orderByCategory(args, tests.user_id, True)
        self.assertTrue(result)
        
        
    """
    Testing ordering my videos by reposted or original posts
    """
    def testK(self):
        result = db.orderBySaved(tests.user_id, 0)
        self.assertTrue(result)
        
        
    """
    Testing ordering videos by username
    """
    def testL(self):
        result = db.orderByUser(2, tests.user_id)
        self.assertTrue(result)
    
    
    """
    Testing getting the list of video categories
    """
    def testM(self):
        result = db.getCategories()
        self.assertTrue(result)
        
        
    """
    Testing get categories id by category name
    """
    def testN(self):
        result = db.getCategoryIdByName(tests.category_name)
        self.assertTrue(result)
        
        
    """
    Testing Register a users vote and check if they voted
    """
    def testO(self):
        db.vote(getVideoId(), tests.user_id, 1)
        calc = db.calcVotes(getVideoId())
        self.assertGreater(calc, 0)
        
        
    """
    Testing if user has voted on a specific video
    """
    def testP(self):
        result = db.checkVote(tests.user_id, getVideoId())
        self.assertEqual(result['count'], 1)
        
        
    """
    Testing calculate the total amount of votes of a specific video
    """
    def testQ(self):
        result = db.calcVotes(getVideoId())
        self.assertGreater(result, 0)
        
    
    """
    Testing get all vote information
    """
    def testR(self):
        result = db.getAllVotes()
        self.assertTrue(result)


    """
    Testing delete by video id
    """
    def testS(self):
        videoid = getVideoId()
        db.delete(videoid)
        
        
        
if __name__ == "__main__":
    unittest.main()