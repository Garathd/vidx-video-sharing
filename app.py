import os
import pymysql
import db
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    #Clean the Login Variable
    db.setLogin('')
    
    return render_template('login.html')
    
@app.route('/check-user/', methods=['GET','POST'])
def check():
    
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        
        connection = db.database()
        
    try:
        with connection.cursor() as cursor:
          sql = "SELECT username FROM users WHERE username ='{0}' AND password ='{1}'".format(username, password)
          cursor.execute(sql)
          result = cursor.fetchone()
          
          if result:
            user = str(result[0])
            
            if username == user:
                db.setLogin(username)
                
                user_name = db.getLogin()
                
                return redirect('/{}'.format(username))
          
          else:
              return render_template('login.html')
          
    finally:
        connection.close()
    
    return render_template('login.html')
        
@app.route('/<username>')
def dashboard(username):
    
    try:
        user_name = db.getLogin()
        userid = db.getUserId(user_name)
        playlists = db.getMyPlaylist(userid)
    except: 
        return redirect('/')

    if user_name != username:
        return redirect('/')
    
    return render_template('dashboard.html', username=username, playlists=playlists)
    
    
@app.route('/home')
def home():
    
    try:
        user_name = db.getLogin()
    except:
        return redirect('/')
    
    return redirect('/{}'.format(user_name))
    
@app.route('/videos')
def videos():
    
    try:
        user_name = db.getLogin()
        userid = db.getUserId(user_name)
        videos = db.getOtherVideos(userid)

    except Exception as e:
        print("Exception: {}".format(e))
        return redirect('/')
    
    return render_template('videos.html',videos=videos, username=user_name)
    
@app.route('/new-playlist')
def newplaylist():
    
    try:
        user_name = db.getLogin()
        userid = db.getUserId(user_name)
        categories = db.getCategories()
    except: 
        return redirect('/')
    
    return render_template('new-playlist.html', user_name=user_name, userid=userid, categories=categories)
    
    
@app.route('/add-playlist', methods=['GET','POST'])
def addplaylist():
    
    # Original Poster
    origin = "true"
    
    try:
        user_name = db.getLogin()
    except: 
        return redirect('/')
       
       
    if request.method == 'POST':
        form = request.form
        userid = form['user_id']
        title = form['title']
        description = form['description']
        image = form['image']
        video = form['video']
        category = form['category_id']
        
        
        try:
            db.addPlaylist(userid, title, description, image, video, category, origin)
        finally:
            return redirect('/{}'.format(user_name))
    
    
@app.route('/delete/<playlistid>', methods=['GET','POST'])
def delete(playlistid):
    
    try:
        user_name = db.getLogin()
        db.delete(playlistid)
    finally:
        return redirect('/{}'.format(user_name))
        
    
@app.route('/edit/<playlistid>')
def edit(playlistid):
    
    user_name = db.getLogin()
    categories = db.getCategories()
    playlist = db.getPlaylistById(playlistid)
        
    return render_template('edit-playlist.html', playlist=playlist,categories=categories)
    
@app.route('/downvote/<playlistid>')
def downvote(playlistid):
    
    user_name = db.getLogin()
    categories = db.getCategories()
    playlist = db.getPlaylistById(playlistid)
        
    return redirect('/{}'.format(user_name))
    
@app.route('/upvote/<playlistid>')
def upvote(playlistid):
    
    user_name = db.getLogin()
    categories = db.getCategories()
    playlist = db.getPlaylistById(playlistid)
        
    return redirect('/{}'.format(user_name))
    
    
@app.route('/repost/<playlistid>')
def repost(playlistid):
    
    # Not Original Post
    origin = "false"
    
    try:
        user_name = db.getLogin()
        userid = db.getUserId(user_name)
        playlist = db.getPlaylistById(playlistid)
        
        title = playlist['title']
        description = playlist['description']
        img_source = playlist['img_source']
        video_source = playlist['video_source']
        category_id = playlist['category_id']
        
        db.addPlaylist(userid, title, description, img_source, video_source, category_id, origin)
        
        
    finally:
        return redirect('/{}'.format(user_name))
        
    
@app.route('/order-by/category/<category_name>')     
def ordercategory(category_name):
    
    try:
        user_name = db.getLogin()
        userid = db.getUserId(user_name)
        category_id = db.getCategoryByName(category_name)
        
        ordered = db.orderByCategory(category_id, userid)
        return render_template('videos.html',videos=ordered, username=user_name)

    except Exception as e:
        print("Exception: {}".format(e))
        return redirect('/')
        
        
@app.route('/order-by/user/<user_name>')     
def orderuser(user_name):
    
    try:
        my_username = db.getLogin()
        my_id = db.getUserId(my_username)
        users_id = db.getUserId(user_name)

        ordered = db.orderByUser(users_id, my_id)
        return render_template('videos.html',videos=ordered, username=my_username)

    except Exception as e:
        print("Exception: {}".format(e))
        return redirect('/')
        
    
@app.route('/edit-playlist', methods=['GET','POST'])
def editplaylist():
    
    if request.method == 'POST':
        form = request.form
        playlistid = int(form['playlist_id'])
        title = form['title']
        description = form['description']
        img_source = form['image']
        video_source = form['video']
        category_id = int(form['category_id'])
        
    try:
        user_name = db.getLogin()
        db.edit(playlistid, title, description, img_source, video_source, category_id)
    finally:
        return redirect('/{}'.format(user_name))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
