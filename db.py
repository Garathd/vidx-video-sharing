import os
import pymysql

# Default Database Credentials
user = os.getenv('C9_USER')
password = ''

# Check if the user is logged in
user_name = ''

# Set Login Name
def setLogin(value):
    global user_name
    user_name = value
    
    
# Get Login Name    
def getLogin():
    return user_name
    
    
# ClearDB Database Connection
def database():
    connection = pymysql.connect(
        host="eu-cdbr-west-02.cleardb.net",
        user="b8c9433415b668",
        password="f364db5b",
        db="heroku_acb2a7f13c05325")
    return connection
        

# # Local Database Connection
# def database():
#     connection = pymysql.connect(
#         host='localhost',
#         user=user,
#         password=password,
#         db='milestoneProject4')
#     return connection
    
    
# Register user to database
def register(username, password):
    
    db = database()
    
    sql = "INSERT INTO users(username, password) VALUES ('{0}', '{1}')".format(username, password)

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
        
    finally:
        db.close()
        

# Authenticate User
def authenticate(username, password):
    
    db = database()
    
    try:
        with db.cursor() as cursor:
          sql = "SELECT username FROM users WHERE username ='{0}' AND password ='{1}'".format(username, password)
          cursor.execute(sql)
          result = cursor.fetchone()
          
    except Exception as e:
        print("auth: {}".format(e))
        
    finally:
        db.close()
        
    return result
    
    
# Get User ID    
def getUserId(username):
    
    db = database()
    
    try:
        with db.cursor() as cursor:
          sql = "SELECT user_id FROM users WHERE username ='{0}'".format(username)
          cursor.execute(sql)
          result = cursor.fetchone()
          value = str(result[0])
    
    except Exception as e:
        print("getUserId: {}".format(e))      
          
    finally:
        db.close()
        
    return value
    
    
# Get My Videos   
def getMyPlaylist(userid):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT p.playlist_id, p.title, p.description, p.img_source, p.video_source, p.origin, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id = '{}' ORDER BY p.playlist_id DESC".format(userid)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print("getMyPlaylist: {}".format(e))      
          
    finally:
        db.close()
        
    return result
    
    
# Get Other Users Videos    
def getOtherVideos(userid):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT p.playlist_id, p.title, p.description, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id != '{}' AND origin = 'true' ORDER BY p.playlist_id DESC".format(userid)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print("getOtherVideos: {}".format(e))      
          
    finally:
        db.close()
        
    return result
    
    
# Get Playlist By ID
def getPlaylistById(playlist_id):
    
    playlistid = int(playlist_id)
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT * FROM playlists WHERE playlist_id = {}".format(playlistid)
          cursor.execute(sql)
          result = cursor.fetchone()
          
    except Exception as e:
        print("getPlaylistById: {}".format(e))      
          
    finally:
        db.close()
        
    return result
    
    
# Add a new video    
def addPlaylist(user_id, title, description, image, video, category_id, origin):
    
    db = database()
    
    sql = "INSERT INTO playlists(user_id, title, description, img_source, video_source, category_id, origin) VALUES ({0}, '{1}', '{2}','{3}', '{4}', {5}, '{6}')".format(user_id, title, description, image, video, category_id, origin)

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    
    except Exception as e:
        print("addPlaylist: {}".format(e))        
            
    finally:
        db.close()
        
    
# Delete a video    
def delete(playlistid):
    
    db =  database()
    
    sql = "DELETE FROM playlists WHERE playlist_id = {}".format(playlistid)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    
    except Exception as e:
        print("delete: {}".format(e))        
            
    finally:
        db.close()
    
    
# Edit a video    
def edit(playlistid, title, description, img_source, video_source, category_id):
    
    db =  database()
    
    sql = "UPDATE playlists SET title = '{1}', description = '{2}', img_source = '{3}', video_source = '{4}', category_id = {5} WHERE playlist_id = {0}".format(playlistid, title, description, img_source, video_source, category_id)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
            
    except Exception as e:
        print("edit: {}".format(e))        
            
    finally:
        db.close()
        

# Ordering Videos by category
def orderByCategory(ordering, userid, profile):
    
    category_id = ordering['category_id']

    db = database()
    
    # If its my profile show my video list otherwise show peoples original videos
    if profile == True:
        sql = "SELECT p.playlist_id, p.title, p.description, p.origin, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id = {0} ORDER BY p.category_id = {1} DESC".format(userid,category_id)
    else:
        sql = "SELECT p.playlist_id, p.title, p.description, p.origin, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id != {0} AND p.origin = 'true' ORDER BY p.category_id = {1} DESC".format(userid,category_id)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print("orderByCategory: {}".format(e))      
          
    finally:
        db.close()
        
    return result
    
# Ordering my videos by reposted or original posts
def orderBySaved(userid, saved):
    
    db = database()
    
    # Checking if the video is an original or a repost
    if int(saved) == 1:
        sql = "SELECT p.playlist_id, p.title, p.description, p.origin, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id = {} ORDER BY p.origin='false' DESC".format(userid)
    else:
        sql = "SELECT p.playlist_id, p.title, p.description, p.origin, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id = {} ORDER BY p.origin='true' DESC".format(userid)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print("orderBySaved: {}".format(e))      
          
    finally:
        db.close()
        
    return result    
    
    
# Ordering Feed videos by username
def orderByUser(users_id, my_id):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT p.playlist_id, p.title, p.description, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id != {0} AND p.origin = 'true' ORDER BY p.user_id = {1} DESC".format(my_id,users_id)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    except Exception as e:
        print("orderByUser: {}".format(e))
          
    finally:
        db.close()
        
    return result
        

# Get the list of video categories
def getCategories():
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM categories ORDER by category_name ASC"
            cursor.execute(sql)
            result = cursor.fetchall()
            
    except Exception as e:
        print("getCategories: {}".format(e))        
    
    finally:
        db.close()
    
    return result
    
    
# Get categories information
def getCategoryByName(category_name):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT category_id FROM categories WHERE category_name = '{0}'".format(category_name)
            cursor.execute(sql)
            result = cursor.fetchone()
            
    except Exception as e:
        print("getCategoryByName: {}".format(e))
    
    finally:
        db.close()
    
    return result
    
    
# Get all the voting information of the videos
def getAllVotes():
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM votes"
            cursor.execute(sql)
            result = cursor.fetchall()
            
    except Exception as e:
        print("getAllVotes: {}".format(e))        
            
    finally:
        db.close()
    
    return result    
    
    
# Check if a user has voted on a specific playlist
def checkVote(user_id, playlist_id):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT COUNT(vote) AS count FROM votes WHERE playlist_id = {0} AND user_id = {1}".format(playlist_id,user_id)
            cursor.execute(sql)
            ans = cursor.fetchone()
            result = ans['count']

    except Exception as e:
        print("checkVote: {}".format(e))        
            
    finally:
        db.close()
    
    return result
    

# Calculate to the total amount of votes of a video    
def calcVotes(playlist_id):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT SUM(vote) as count FROM votes WHERE playlist_id = {}".format(playlist_id)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count']
            
    except Exception as e:
        print("calcVotes: {}".format(e))        
            
    finally:
        db.close()
    
    
# Register a vote for a video
def vote(playlist_id, user_id, result):
    
    db = database()

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "INSERT INTO votes(playlist_id, user_id, vote) VALUES ({0}, {1}, '{2}')".format(playlist_id, user_id, result)
            cursor.execute(sql)
            db.commit()
            
    except Exception as e:
        print("Vote: {}".format(e))
    
    finally:
        db.close()
