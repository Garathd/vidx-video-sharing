import os
import pymysql

# Local Database Credentials
user = os.getenv('C9_USER')
password = ''

# Init Username
user_name = ''


"""
Set Login Name
"""
def setLogin(value):
    global user_name
    user_name = value
    
    
"""
Get Login Name
"""
def getLogin():
    return user_name
    
    
"""
ClearDB Database Connection
"""
def remote():
    connection = pymysql.connect(
        host="eu-cdbr-west-02.cleardb.net",
        user="b8c9433415b668",
        password="f364db5b",
        db="heroku_acb2a7f13c05325")
    return connection
        

"""
Local Database Connection
"""
def local():
    connection = pymysql.connect(
        host='localhost',
        user=user,
        password=password,
        db='milestoneProject4')
    return connection
    
  
# This is for setting either a local or remote database   
database = remote
    
"""
Register user to database
"""
def register(username, password):

    # Check if user exists already
    value = authenticate(username, password)
    if value == None:
        db = database()
    
        sql = "INSERT INTO users(username, password) VALUES ('{0}', '{1}')".format(username, password)
    
        try:
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql)
                db.commit()
                
        except Exception as e:
            print(e)
            
        finally:
            db.close()
            return True
      
    else:
        return False
        
        
"""
Authenticate User
"""
def authenticate(username, password):
    
    db = database()
    
    try:
        with db.cursor() as cursor:
          sql = "SELECT username FROM users WHERE username ='{0}' AND password ='{1}'".format(username, password)
          cursor.execute(sql)
          result = cursor.fetchone()

          if result == None:
              return False
          else:
              return result
          
    except Exception as e:
        print(e)
        
    finally:
        db.close()
        
    return result
    
    
"""
Get User ID
"""
def getUserId(username):
    
    db = database()
    
    try:
        with db.cursor() as cursor:
          sql = "SELECT user_id FROM users WHERE username ='{0}'".format(username)
          cursor.execute(sql)
          result = cursor.fetchone()
          value = str(result[0])
    
    except Exception as e:
        print(e)      
          
    finally:
        db.close()
        
    return value
    
    
"""
Get My Videos
"""
def getMyVideos(userid):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT v.video_id, v.title, v.description, v.img_source, v.video_source, v.origin, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id = '{}' ORDER BY v.video_id DESC".format(userid)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print(e)   
          
    finally:
        db.close()
        
    return result
    
    
"""
Get Other Users Videos 
"""
def getOtherVideos(userid):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT v.video_id, v.title, v.description, v.img_source, v.video_source, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id != '{}' AND origin = 'true' ORDER BY v.video_id DESC".format(userid)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print(e)     
          
    finally:
        db.close()
        
    return result
    
    
"""
Get video By ID
"""
def getVideoById(video_id):
    
    videoid = int(video_id)
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT * FROM videos WHERE video_id = {}".format(videoid)
          cursor.execute(sql)
          result = cursor.fetchone()
          
    except Exception as e:
        print(e)    
          
    finally:
        db.close()
        
    return result
    
    
"""
Add a new video 
"""
def addVideo(user_id, title, description, image, video, category_id, origin):
    
    db = database()
    
    sql = "INSERT INTO videos(user_id, title, description, img_source, video_source, category_id, origin) VALUES ({0}, '{1}', '{2}','{3}', '{4}', {5}, '{6}')".format(user_id, title, description, image, video, category_id, origin)

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    
    except Exception as e:
        print(e)       
            
    finally:
        db.close()
        
    
"""
Delete a video   
"""
def delete(videoid):
    
    db =  database()
    
    sql = "DELETE FROM videos WHERE video_id = {}".format(videoid)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    
    except Exception as e:
        print(e)       
            
    finally:
        db.close()
    
    
"""
Edit a video
"""
def edit(videoid, title, description, img_source, video_source, category_id):
    
    db =  database()
    
    sql = "UPDATE videos SET title = '{1}', description = '{2}', img_source = '{3}', video_source = '{4}', category_id = {5} WHERE video_id = {0}".format(videoid, title, description, img_source, video_source, category_id)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
            
    except Exception as e:
        print(e)        
            
    finally:
        db.close()
        

"""
Ordering videos by category
"""
def orderByCategory(ordering, userid, profile):
    
    category_id = ordering['category_id']

    db = database()
    
    # If it's my profile show my video list otherwise show peoples original videos
    if profile == True:
        sql = "SELECT v.video_id, v.title, v.description, v.origin, v.img_source, v.video_source, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id = {0} ORDER BY v.category_id = {1} DESC".format(userid,category_id)
    else:
        sql = "SELECT v.video_id, v.title, v.description, v.origin, v.img_source, v.video_source, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id != {0} AND v.origin = 'true' ORDER BY v.category_id = {1} DESC".format(userid,category_id)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print(e)    
          
    finally:
        db.close()
        
    return result
    
    
"""
Ordering my videos by reposted or original posts
"""
def orderBySaved(userid, saved):
    
    db = database()
    
    # Checking if the video is an original or a repost
    if int(saved) == 1:
        sql = "SELECT v.video_id, v.title, v.description, v.origin, v.img_source, v.video_source, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id = {} ORDER BY v.origin='false' DESC".format(userid)
    else:
        sql = "SELECT v.video_id, v.title, v.description, v.origin, v.img_source, v.video_source, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id = {} ORDER BY v.origin='true' DESC".format(userid)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print(e)    
          
    finally:
        db.close()
        
    return result    
    

"""
Ordering videos by username
"""
def orderByUser(users_id, my_id):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT v.video_id, v.title, v.description, v.img_source, v.video_source, u.username, c.category_name FROM videos v INNER JOIN users u ON v.user_id = u.user_id INNER JOIN categories c ON v.category_id = c.category_id WHERE u.user_id != {0} AND v.origin = 'true' ORDER BY v.user_id = {1} DESC".format(my_id,users_id)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print(e)
          
    finally:
        db.close()
        
    return result
        

"""
Get the list of video categories
"""
def getCategories():
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM categories ORDER by category_name ASC"
            cursor.execute(sql)
            result = cursor.fetchall()
            
    except Exception as e:
        print(e)        
    
    finally:
        db.close()
    
    return result
    
    
"""
Get categories id by category name
"""
def getCategoryIdByName(category_name):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT category_id FROM categories WHERE category_name = '{0}'".format(category_name)
            cursor.execute(sql)
            result = cursor.fetchone()
            
    except Exception as e:
        print(e)
    
    finally:
        db.close()
    
    return result
    
    
"""
Get all the voting information of the videos
"""
def getAllVotes():
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM votes"
            cursor.execute(sql)
            result = cursor.fetchall()
            
    except Exception as e:
        print(e)       
            
    finally:
        db.close()
    
    return result    
    
    
"""
Check if a user has voted on a specific video
"""
def checkVote(user_id, video_id):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT COUNT(vote) AS count, vote as vote FROM votes WHERE video_id = {0} AND user_id = {1}".format(video_id, user_id)
            cursor.execute(sql)
            result = cursor.fetchone()

    except Exception as e:
        print(e)       
            
    finally:
        db.close()
    
    return result
    

"""
Calculate to the total amount of votes of a specific video
"""
def calcVotes(video_id):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT SUM(vote) as count FROM votes WHERE video_id = {}".format(video_id)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count']
            
    except Exception as e:
        print(e)       
            
    finally:
        db.close()
    
    
"""
Register a users vote for a specific video
"""
def vote(video_id, user_id, result):
    
    db = database()

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "INSERT INTO votes(video_id, user_id, vote) VALUES ({0}, {1}, '{2}')".format(video_id, user_id, result)
            cursor.execute(sql)
            db.commit()
            
    except Exception as e:
        print(e)
    
    finally:
        db.close()
