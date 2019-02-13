import os
import pymysql

user = os.getenv('C9_USER')
password = ''

# Check if the user is logged in
user_name = ''

# Database Connection
def database():
    connection = pymysql.connect(
        host='localhost',
        user=user,
        password=password,
        db='milestoneProject4')
    return connection
    
  
# Get User ID    
def getUserId(username):
    
    db = database()
    
    try:
        with db.cursor() as cursor:
          sql = "SELECT user_id FROM users WHERE username ='{0}'".format(username)
          cursor.execute(sql)
          result = cursor.fetchone()
          value = str(result[0])
    finally:
        db.close()
        
    return value
    
# Get Playlist   
def getMyPlaylist(userid):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT p.playlist_id, p.title, p.description, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id = '{}'".format(userid)
          cursor.execute(sql)
          result = cursor.fetchall()
    finally:
        db.close()
        
    return result
    
    
def addPlaylist(userid, title, description, image, video, category):
    
    db = database()
    
    title = title
    description = description
    image = image
    video = video
    user_id = userid
    category_id = category
    
    sql = "INSERT INTO playlists(user_id, title, description, img_source, video_source, category_id) VALUES ({0}, '{1}', '{2}','{3}', '{4}', {5})".format(user_id, title, description, image, video, category_id)

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()
    
    return result
    
# Get categories
def getCategories():
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM categories"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        db.close()
    
    return result

# Set Login Name
def setLogin(value):
    global user_name
    user_name = value
    
    
# Get Login Name    
def getLogin():
    return user_name
    
