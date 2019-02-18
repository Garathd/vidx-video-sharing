import os
import pymysql
import db
from jinja2 import Environment, PackageLoader, select_autoescape
from flask import Flask, render_template, request, redirect
from jinja2.ext import Extension, loopcontrols

app = Flask(__name__)


# Adding Jinja Environment so I can use Jinja Extensions
app.jinja_env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Adding Jinja Loop Controls Extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Login Page
@app.route('/')
def index():
    return render_template('login.html')
    
    
# Registration Page    
@app.route('/register')
def register():
    return render_template('register.html')

# Register the user
@app.route('/register-user/', methods=['GET','POST'])
def regcheck():
    
    # Getting form data
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        
        # Registering User
        try:
           db.register(username,password)

        except Exception as e:
            print(e)

        finally:
            return render_template('login.html')
            
            
# Checking User Credentials    
@app.route('/check-user/', methods=['GET','POST'])
def check():
    
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        
        # Authenticating the user
        try:
            result = db.authenticate(username,password)
            
            if result:
                user = str(result[0])
                if username == user:
                    db.setLogin(username)
                    return redirect('/feed')
          
            else:
                return render_template('login.html')
            
        except Exception as e:
            print(e)

    
    return render_template('login.html')
        
# User Profile        
@app.route('/<username>')
def dashboard(username):
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting list of my videos
        playlists = db.getMyPlaylist(userid)
        
        # Getting the vote information
        votes = db.getAllVotes()
        
    except Exception as e: 
        return redirect('/')
    
    return render_template('dashboard.html',
    username=username,
    playlists=playlists,
    votes=votes,
    get_votes=db.calcVotes)
    
    
# Menu Redirect for my profile    
@app.route('/profile')
def profile():
    
    try:
        # Get Username
        user_name = db.getLogin()
    except Exception as e:
        return redirect('/')
    
    return redirect('/{}'.format(user_name))
    
    
# Feed of videos created by other users original videos    
@app.route('/feed')
def feed():
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting original videos created by other users
        videos = db.getOtherVideos(userid)
        
        # Getting the vote information
        votes = db.getAllVotes()

    except Exception as e:
        print(e)
        return redirect('/')
    
    return render_template('videos.html',
    videos=videos,
    username=user_name,
    votes=votes,
    userid=userid,
    get_votes=db.calcVotes,
    check_voted=db.checkVote)
    
    
# New Video Page   
@app.route('/new-playlist')
def newplaylist():
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting list of categories
        categories = db.getCategories()
    except: 
        return redirect('/')
    
    return render_template('new-playlist.html', 
    user_name=user_name, 
    userid=userid, 
    categories=categories)
    
    
# Add Video to the database    
@app.route('/add-playlist', methods=['GET','POST'])
def addplaylist():
    
    # Video's original creator
    origin = "true"
    
    try:
        # Get username
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
            # Add the Video to the database
            db.addPlaylist(userid, title, description, image, video, category, origin)
        finally:
            return redirect('/{}'.format(user_name))
            
    
# Delete video    
@app.route('/delete/<playlistid>', methods=['GET','POST'])
def delete(playlistid):
    
    try:
        # Get username
        user_name = db.getLogin()
        
        # Delete the video
        db.delete(playlistid)
    finally:
        return redirect('/{}'.format(user_name))
        
        
# Edit video    
@app.route('/edit/<playlistid>')
def edit(playlistid):
    
    # Getting username
    user_name = db.getLogin()
    
    # Getting categories list
    categories = db.getCategories()
    
    # Getting playlists by id
    playlist = db.getPlaylistById(playlistid)
        
    return render_template('edit-playlist.html', 
    playlist=playlist,
    categories=categories)
    
# Down vote  
@app.route('/downvote/<playlistid>')
def downvote(playlistid):
    
    # Set vote value
    vote = -1
    
    # Calculating the votes for video
    total_votes = int(db.calcVotes(playlistid))
    
    if total_votes == None:
        total_votes = 0
    
    print("total_votes: {}".format(total_votes))
    

    # This deletes a video if it has a total score of -5
    if total_votes > -4:
        try:
            print("Is higher than minus 4")
            # Getting username
            user_name = db.getLogin()
            
            # Getting user id
            userid = db.getUserId(user_name)
            
            # Make vote
            db.vote(playlistid, userid, vote)
        except: 
            redirect('/')   
        finally:
            return redirect('/feed')
        
       
    else:
         print("Is lower or equal to minus 4")
         db.delete(playlistid)
         return redirect('/feed')
 
# Up vote    
@app.route('/upvote/<playlistid>')
def upvote(playlistid):
    
    # Set vote value
    vote = 1
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Make vote
        db.vote(playlistid, userid, vote)
    except: 
        redirect('/')   
    finally:
        return redirect('/feed')
    
    
# Repost a video    
@app.route('/repost/<playlistid>')
def repost(playlistid):
    
    # Video's original creator
    origin = "false"
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Get playlist by id
        playlist = db.getPlaylistById(playlistid)
        
        # Setting variables with copied video data
        title = playlist['title']
        description = playlist['description']
        img_source = playlist['img_source']
        video_source = playlist['video_source']
        category_id = playlist['category_id']
        
        # Adding video to database
        db.addPlaylist(userid, title, description, img_source, video_source, category_id, origin)
        
    finally:
        return redirect('/{}'.format(user_name))
        

# Order feed videos by category    
@app.route('/order-by/category/<category_name>')     
def ordercategory(category_name):
    
    # Not my videos or profile page
    profile = False
    
    try:
        # Getting user name
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting categories by name and ordering
        category_id = db.getCategoryByName(category_name)
        
        # Getting vote information
        votes = db.getAllVotes()
        
        # Getting feed video list ordered by category name
        ordered = db.orderByCategory(category_id, userid, profile)
    
    except Exception as e:
        print(e)
        return redirect('/')
        
    finally:
        return render_template('videos.html',
        videos=ordered, 
        username=user_name,
        votes=votes,
        userid=userid,
        get_votes=db.calcVotes,
        check_voted=db.checkVote)
        
      
# Order profile videos by category       
@app.route('/order-by/my-profile/category/<category_name>')     
def orderprofilecategory(category_name):
    
    # My videos and profile
    profile = True
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting category by category name and ordering
        category_id = db.getCategoryByName(category_name)
        
        # Getting vote information
        votes = db.getAllVotes()
        
        # Getting profile video list ordered by category name
        ordered = db.orderByCategory(category_id, userid, profile)

    except Exception as e:
        print("Exception: {}".format(e))
        return redirect('/')
        
    finally:
         return render_template('dashboard.html', 
         playlists=ordered, 
         username=user_name,
         votes=votes,
         get_votes=db.calcVotes)
         

# Order profile videos by original videos and reposted videos           
@app.route('/order-by/my-profile/saved/<status>')     
def ordersaved(status):
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting vote information
        votes = db.getAllVotes()
        
        # Getting profile video list ordered by original and reposted
        ordered = db.orderBySaved(userid, status)

    except Exception as e:
        print(e)
        return redirect('/')
        
    finally:
         return render_template('dashboard.html', 
         playlists=ordered, 
         username=user_name,
         votes=votes,
         get_votes=db.calcVotes)         
        

# Ordering feed videos by username       
@app.route('/order-by/user/<user_name>')     
def orderuser(user_name):
    
    try:
        # Getting my username
        my_username = db.getLogin()
        
        # Getting my user id
        my_id = db.getUserId(my_username)
        
        # Getting user id to search 
        users_id = db.getUserId(user_name)
        
        #Getting vote information
        votes = db.getAllVotes()
        
        # Getting feed videos ordered by user name
        ordered = db.orderByUser(users_id, my_id)

    except Exception as e:
        print(e)
        return redirect('/')
        
    finally:
        return render_template('videos.html',
        videos=ordered, 
        username=my_username,
        votes=votes,
        userid=my_id,
        get_votes=db.calcVotes,
        check_voted=db.checkVote)

# Edit videos
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
        # Getting username
        user_name = db.getLogin()
        
        # Edit video information in the database
        db.edit(playlistid, title, description, img_source, video_source, category_id)
    finally:
        return redirect('/{}'.format(user_name))

@app.route('/logout')
def logout():
    #Clean the Login Variable
    db.setLogin('')
    
    return redirect('/')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
