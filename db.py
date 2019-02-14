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
    
def getOtherVideos(userid):
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT p.playlist_id, p.title, p.description, p.img_source, p.video_source, u.username, c.category_name FROM playlists p INNER JOIN users u ON p.user_id = u.user_id INNER JOIN categories c ON p.category_id = c.category_id WHERE u.user_id != '{}' AND origin = 'true'".format(userid)
          cursor.execute(sql)
          result = cursor.fetchall()
          
    finally:
        db.close()
        
    return result
    

def getPlaylistById(playlist_id):
    
    playlistid = int(playlist_id)
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
          sql = "SELECT * FROM playlists WHERE playlist_id = {}".format(playlistid)
          cursor.execute(sql)
          result = cursor.fetchone()
    finally:
        db.close()
        
    return result
    
    
def addPlaylist(userid, title, description, image, video, category, origin):
    
    db = database()
    
    title = title
    description = description
    image = image
    video = video
    user_id = userid
    category_id = category
    origin = origin
    
    sql = "INSERT INTO playlists(user_id, title, description, img_source, video_source, category_id, origin) VALUES ({0}, '{1}', '{2}','{3}', '{4}', {5}, {6})".format(user_id, title, description, image, video, category_id, origin)

    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()
    
    
def delete(playlistid):
    
    db =  database()
    
    sql = "DELETE FROM playlists WHERE playlist_id = {}".format(playlistid)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()
    
    
def edit(playlistid, title, description, img_source, video_source, category_id):
    
    db =  database()
    
    sql = "UPDATE playlists SET title = '{1}', description = '{2}', img_source = '{3}', video_source = '{4}', category_id = {5} WHERE playlist_id = {0}".format(playlistid, title, description, img_source, video_source, category_id)
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()

# Get categories
def getCategories():
    
    db = database()
    
    try:
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM categories ORDER by category_name ASC"
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
    
