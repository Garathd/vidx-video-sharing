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
            db.addPlaylist(userid, title, description, image, video, category)
        finally:
            return redirect('/{}'.format(user_name))
    
    
@app.route('/delete/<playlistid>', methods=['GET','POST'])
def delete(playlistid):
    
    try:
        user_name = db.getLogin()
        db.delete(playlistid)
    finally:
        return redirect('/{}'.format(user_name))
        
    
@app.route('/edit/<playlistid>', methods=['GET','POST'])
def edit(playlistid):
    
 
    user_name = db.getLogin()
    categories = db.getCategories()
    playlist = db.getPlaylistById(playlistid)
        
    # for play in playlist:
            
    #     title = play['title']
    #     description = play['description']
    #     img_source = play['img_source']
    #     video_source = play['video_source']
    #     category_id = play['category_id']
        
    # db.edit(playlistid, title, description, img_source, video_source, category_id)   
        
 
    return render_template('edit-playlist.html', playlist=playlist,categories=categories)
    
    
@app.route('/edit-playlist', methods=['GET','POST'])
def editplaylist():
    
    return("/")
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
