import os
import pymysql
import db
from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2.ext import Extension, loopcontrols
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

"""
Adding Jinja Environment so I can use Jinja Extensions
"""
app.jinja_env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Adding Jinja Loop Controls Extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


"""
Login Page
"""
@app.route('/')
def index():
    return render_template('login.html')
    

"""
Welcome Page
"""
@app.route('/welcome')
def welcome():
    
    try:
        username = db.getLogin()
        if username:
            return render_template('welcome.html', username=username)
        else: 
            return redirect('/')
    
    except:
        return redirect('/')
            
"""
User Logout
"""
@app.route('/logout')
def logout():
    
    if db.getLogin():
        message = {
        "message_type" : "success",
        "message_info" : "{0} has logged out!".format(db.getLogin())
        }
        
        #Clean the Login Variable
        db.setLogin('')
        return render_template('login.html', message=message)
        
    else:
       return redirect('/')
    
    
"""
Registration Page
"""
@app.route('/register')
def register():
    return render_template('register.html')
    

"""
Register the user
"""
@app.route('/register-user/', methods=['GET','POST'])
def regcheck():
    
    # Getting form data
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        
        # Registering User
        try:
            result = db.register(username,password)
            
            if result:
                # Account creation successful
                message = {
                    "message_type" : "success",
                    "message_info" : "{0}'s account has been created!".format(username)
                }
                return render_template('login.html', message=message)
            else:
                # Username has been taken
                message = {
                    "message_type" : "error",
                    "message_info" : "The username {0} has been taken!".format(username)
                }

                return render_template('register.html', message=message)

        except:
            return redirect('/register')


"""
Checking User Credentials
"""
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
                    
                    # Setting Username
                    db.setLogin(username)
                    
                    # Getting User ID
                    userid = db.getUserId(username)
                    
                    # Checking if user has any videos
                    videos = db.getMyVideos(userid)
                    
                    if videos:
                        return redirect('/videos')
                        
                    else:
                        return redirect('/welcome')
                        
            else:
                message = {
                    "message_type" : "error",
                    "message_info" : "Invalid Login Details!"
                }
                return render_template('login.html', message=message)
            
        except:
            return redirect('/')
            
    return render_template('login.html')
    
        
"""
User Profile
"""
@app.route('/<username>')
def dashboard(username):
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting list of my videos
        videos = db.getMyVideos(userid)
   
        if not videos:
            return redirect('/welcome')

        
        # Getting the vote information
        votes = db.getAllVotes()
        
        return render_template('dashboard.html',
        username=username,
        videos=videos,
        votes=votes,
        get_votes=db.calcVotes)
        
    except:
        return redirect('/')
    
    
"""
Menu Redirect for my profile
"""
@app.route('/profile')
def profile():
    
    try:
        # Get Username
        user_name = db.getLogin()
        return redirect('/{}'.format(user_name))
    except:
        return redirect('/')
    
    
"""
Feed of videos created by other users original videos
"""
@app.route('/videos')
def videos():
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting original videos created by other users
        videos = db.getOtherVideos(userid)
        
        # Getting the vote information
        votes = db.getAllVotes()
        
        return render_template('videos.html',
        videos=videos,
        username=user_name,
        votes=votes,
        userid=userid,
        get_votes=db.calcVotes,
        check_voted=db.checkVote)

    except:
        return redirect('/')
    
    
"""
Create a new video
"""
@app.route('/new-video')
def newplaylist():
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting list of categories
        categories = db.getCategories()
        
        return render_template('new-video.html', 
        user_name=user_name, 
        userid=userid, 
        categories=categories)
    except: 
        return redirect('/')
    
    
"""
Add Video to the database
"""
@app.route('/add-video', methods=['GET','POST'])
def addvideo():
    
    # Video's original creator
    origin = "true"
    
    if request.method == 'POST':
        form = request.form
        userid = form['user_id']
        title = form['title']
        description = form['description']
        image = form['image']
        video = form['video']
        category = form['category_id']
        
    try:
        # Get username
        user_name = db.getLogin()
        
        # Add the Video to the database
        db.addVideo(userid, title, description, image, video, category, origin)
        
        return redirect('/{}'.format(user_name))
        
    except: 
        return redirect('/')
            
            
"""
Edit video by video id
"""
@app.route('/edit/<videoid>')
def edit(videoid):
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting categories list
        categories = db.getCategories()
        
        # Getting playlists by id
        video = db.getVideoById(videoid)
            
        return render_template('edit-video.html', 
        video=video,
        categories=categories)            
            
    except:
        return redirect('/')
    

"""
Edit video
"""
@app.route('/edit-video', methods=['GET','POST'])
def editvideo():
    
    if request.method == 'POST':
        form = request.form
        videoid = form['video_id']
        title = form['title']
        description = form['description']
        img_source = form['image']
        video_source = form['video']
        category_id = form['category_id']
        
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Edit video information in the database
        db.edit(videoid, title, description, img_source, video_source, category_id)
        return redirect('/{}'.format(user_name)) 
    
    except:
        return redirect('/')       
            
    
"""
Delete a video
"""
@app.route('/delete/<videoid>', methods=['GET','POST'])
def delete(videoid):
    
    try:
        # Get username
        user_name = db.getLogin()
        
        # Delete the video
        db.delete(videoid)
        
        return redirect('/{}'.format(user_name))
    except:
        return redirect('/')
        
        
"""
Down vote
"""
@app.route('/downvote/<videoid>')
def downvote(videoid):
    
    # Set vote value
    vote = -1
    
    # Calculating the votes for video
    total_votes = db.calcVotes(videoid)
    
    if total_votes == None:
        total_votes = 0

    # This deletes a video if it has a total score of -5
    if total_votes > -4:
        try:
            # Getting username
            user_name = db.getLogin()
            
            # Getting user id
            userid = db.getUserId(user_name)
            
            # Make vote
            db.vote(videoid, userid, vote)
            return redirect('/videos')
            
        except: 
            redirect('/')   
            
    else:
         db.delete(videoid)
         return redirect('/videos')
 
 
"""
Up vote
"""
@app.route('/upvote/<videoid>')
def upvote(videoid):
    
    # Set vote value
    vote = 1
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Make vote
        db.vote(videoid, userid, vote)
        
        return redirect('/videos')
        
    except: 
        redirect('/')   
    
    
"""
Repost a video
"""
@app.route('/repost/<videoid>')
def repost(videoid):
    
    # Video's original creator
    origin = "false"
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Get playlist by id
        video = db.getVideoById(videoid)
        
        # Setting variables with copied video data
        title = video['title']
        description = video['description']
        img_source = video['img_source']
        video_source = video['video_source']
        category_id = video['category_id']
        
        # Adding video to database
        db.addVideo(userid, title, description, img_source, video_source, category_id, origin)
        
        return redirect('/{}'.format(user_name))
        
    except:
        return redirect('/')
        

"""
Order profile videos by category
"""
@app.route('/my-profile/order-by/category/<category_name>')     
def orderprofilecategory(category_name):
    
    # My videos and profile
    profile = True
    
    try:
        # Getting username
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting category by category name and ordering
        category_id = db.getCategoryIdByName(category_name)
        
        # Getting vote information
        votes = db.getAllVotes()
        
        # Getting profile video list ordered by category name
        ordered = db.orderByCategory(category_id, userid, profile)
        
        return render_template('dashboard.html', 
        videos=ordered, 
        username=user_name,
        votes=votes,
        get_votes=db.calcVotes)

    except:
        return redirect('/')

         
"""
Order profile videos by original videos and reposted videos
"""
@app.route('/my-profile/order-by/saved/<status>')     
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
        
        return render_template('dashboard.html', 
        videos=ordered, 
        username=user_name,
        votes=votes,
        get_votes=db.calcVotes)  

    except:
        return redirect('/')
        
        
"""
Order videos by category
"""
@app.route('/videos/order-by/category/<category_name>')     
def ordercategory(category_name):
    
    # Not my videos or profile page
    profile = False
    
    try:
        # Getting user name
        user_name = db.getLogin()
        
        # Getting user id
        userid = db.getUserId(user_name)
        
        # Getting categories by name and ordering
        category_id = db.getCategoryIdByName(category_name)
        
        # Getting vote information
        votes = db.getAllVotes()
        
        # Getting video list ordered by category name
        ordered = db.orderByCategory(category_id, userid, profile)
        
        return render_template('videos.html',
        videos=ordered, 
        username=user_name,
        votes=votes,
        userid=userid,
        get_votes=db.calcVotes,
        check_voted=db.checkVote) 
    
    except:
        return redirect('/')
        
        
"""
Ordering videos by username
"""
@app.route('/videos/order-by/user/<user_name>')     
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
        
        # Getting videos ordered by user name
        ordered = db.orderByUser(users_id, my_id)
        
        return render_template('videos.html',
        videos=ordered, 
        username=my_username,
        votes=votes,
        userid=my_id,
        get_votes=db.calcVotes,
        check_voted=db.checkVote)

    except:
        return redirect('/')
        
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
