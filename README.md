# vidx-video-sharing

This project is inspired by looking for streams and finding dead links to a TV Show or Movie that you maybe want to view. This application is not strictly limited to streaming and in no way, shape or form am I promoting or encouraging this application to be used for streaming links it was just an inspiration! I want this application to be something else, ideally originally created user content that works with momentum based videos. If it's bad then it gets deleted if it's good, then it stays. 

If a video link is rated -5 then the video gets deleted from the database unless someone else has saved (reposted) the video to their profile and in this circumstance a reposted (saved) video is only viewable and accessible to the user that has saved it.

(NB) I use the words saved and reposted interchangeably throughout my readme and application.


## UX

My UX process was to analyze the customer’s requirements and try and think of different ways to incorporate this into not only just a website but a website that is user friendly and easy to navigate.

The client’s requirements are:

- To be able to register and sign into an account
- To be able to create, edit, delete and view videos on their account
- To be able to save other users videos on their profile
- To be able to up vote and down vote on videos of other users
- For videos to be deleted if they get a -5 in vote score
- To be able to view vote scores
- To be able to see what they voted


User stories:

- As a user I want to be able to create an account
- As a user I want to be able to create, edit and delete videos
- As a user I want to view other user’s videos
- As a user I want the ability to save other users videos
- As a user I want to be able to vote on other user’s videos as well as them with my videos
- As a user I want be able to see a videos score
- As a user I want to see if I have already voted on a video
- As a user I want to be able to log out of my account


### Important UX Notes

The All Videos page is based on Facebooks feed. Users can't view their own videos on the All Videos page only on the My Video page. Other users can see original videos of said user but not reposted(saved) videos. 

Another thing which is by design is that it's completely up to a user to be able to post as many videos of the same thing that they want because that is their choice. So for example if a user was to spam the All Videos section with the same video post then it's up to the other users to down vote the video until it gets deleted. In future a feature that I will include in this application is a "report a user" option. The report feature will delete a user and all their videos if they get reported 3 times.

I want this site to be self moderating where it's up to users what stays or what goes. Basically as the designer it's my way of not having any responsibility what so ever of the content of this application. This application is basically a trial run and prototype of a future project that I want to create. This application will hopefully help me understand what my future project needs or doesn't need. 

The way my authentication works is with a global variable that holds the username and stores it in a session. If this session expires then the application hits an exception and users are redirected back to the login screen. 

In my app I have exceptions that catch all. I know this isn't exactly the best practise but my reasoning behind it is that I want to make the UX work as seamlessly as possible in order to provide a smooth user experience. I plan to add more specific error handling in the future.


### Possible Bugs

If you sign into multiple accounts on the one browser all your logged in accounts automatically get logged into the most recent one that was logged into. This is due to the way my setLogin and getLogin functions work. The username is stored in a global session variable so this is why this happens when using the same browser and the same session


## Design

### Front-End

My design inspiration was essentially a YouTube and Facebook hybrid. I also took a little inspiration from Reddit with the Up Votes and Down Votes as I like it better than like and dislike. I like the layout of how YouTube presents its videos. I just modified it slightly to show 3 videos per row instead of 4 on the large resolution screen devices and then just show one video per row on smaller resolution devices. I have a few small very basic sketches as I more or less knew in my head how I wanted the site to look. I did my sketches using [Adobe XD](https://www.adobe.com/uk/products/xd.html?sdid=88X75SKR&mv=search&ef_id=CjwKCAiAqt7jBRAcEiwAof2uKyYmJoV3wlWgAtyiwwWG5Q9ndPqtJejDidjgRFtcyOti86rbwX6lkhoCu8IQAvD_BwE:g:s&s_kwcid=AL!3085!3!315413032962!e!!g!!adobe%20xd). Screenshots can be found in the [mockups folder](https://github.com/Garathd/vidx-video-sharing/tree/master/mockups).

I was considering also doing some mobile resolution mockups but its more or less the same except for the mobile menu and the fact that instead of having 3 videos per row in the All Videos/ My Videos pages it just has one video per row.

***Login/Register Pages***
These pages are more or less the same design wise. If there is an issue with either login or registration then a brief information message should appear on the screen. New users will be directed to a welcome page.

***Welcome Page***
The welcome page appears to the new users and users who have no videos saved on their profile. This page explains how the site works and explains the various buttons. This is also the help page

***All Videos Page***
This page displays all the users’ videos except for the videos of the user that is signed in. Users are redirected to this page when they sign in and if they have existing videos on their profile or else click the logo when they are signed in. On this page you can repost videos as well as vote on videos. Videos can be ordered by user or by category.

***My Videos Page***
Also known as the profile page. This page lets you delete, edit and view your videos. This page also shows reposted videos. Videos can be ordered by category and status (original or reposted). The My Videos and the All Videos pages have more or less an identical design except for a few different options on videos.

***New Video / Edit Video Page***
These pages have identical design. The edit video pages text fields are populated with data from a chosen video and in the new video page the text fields are blank


### Back-End (MySQL Database)

My backend consists of a relatively simple MySQL database. For testing and Development I use the local [Cloud 9](https://aws.amazon.com/cloud9/?origin=c9io) Database and then for the live version I use the [ClearDB](https://elements.heroku.com/addons/cleardb) heroku add on. The databases can be set in the applications db.py file with options for local or remote databases.

My Database consists of 4 tables:

- ***users***
- ***videos***
- ***categories***
- ***votes***

I had to set ``` ON DELETE CASCASE ``` on the *video id* FOREIGN KEY on the ***votes*** table that REFERENCES the *video id* PRIMARY KEY on the ***videos*** table. This was to ensure that if a video got deleted than all corresponding vote data would be deleted 


The dump file for my database can be viewed [here](https://github.com/Garathd/vidx-video-sharing/blob/master/dump.sql)

### The ER Diagram for my database:

![alt text](https://github.com/Garathd/vidx-video-sharing/blob/master/images/ER-Diagram.png)


## Features

The features of this application are as follows:

- Ability to Register, Sign into and Logout of an Account
- Ability to Create, Edit, Delete and View Videos
- Ability to repost videos to your profile page
- Ability to vote on videos and if video has score of -5 then the ability to automatically delete them
- Ability to see if voted on a particular video and to view its voting score
- Ability to order by Category, Username, Reposted Videos and Original Videos


## Features Left to Implement

Something I have really considered but I think would potentially be better at a future stage is to have each of the video categories as sub menu items to the All Videos menu item. It would definitely make it easier for users to find videos of a specific category. But then the more I thought about it I realised that if I only initially had a small number of users with below 200 videos in total it might be better for them to scroll through all the videos and vote up or down on the videos. If a user got sick of seeing the same videos they would more than likely vote down a video ensuring that below par or questionable videos can be removed quicker.

If I was to get more users with more videos I would definitely implement the menu separation of categories and also add a feature to each video to report users if content is deemed inappropriate by users. If someone gets 3 reports on their account for the one video then their profile is automatically deleted from the system as well as their votes and videos. The functionality works more or less the same as a video that gets -5 votes.

I think another cool feature would be if a username is clicked then it brings you that user’s profile where you can see information about them as well as posts on their page and also the ability to send messages to other users. The way it currently works is that if a username is clicked than the videos are ordered by that user.

The ability to search videos is also a feature I would definitely implement at a later stage if I was to get more videos and it was something that initially I was seriously considering doing in the first version of this application.


## Technologies Used

### Python and Flask

Flask is the Python Framework I’m using for this application

### CSS

I'm using SCSS to build my css style sheets and probably a little unconventionally I'm using [Materialize](https://materializecss.com/) and also [Bootstrap 4](https://getbootstrap.com/). To be honest though it doesn't seem to have any adverse effects and over all looks better and is more responsive and visually pleasing out of the box when used together than individually. It was initially a mistake on my part but ended up looking pretty good. I also did a little research and decided to use the two of them after reading this [article](https://stackoverflow.com/questions/28613848/is-it-possible-to-integrate-materializecss-into-bootstrap). I also tried Material Design for bootstrap but wasn't happy with the way it looked

### JQuery

I have only used minimal JQuery. I have used it for the scroll to top button, the mobile menu and for select options for the forms in materialize.

### Gulp

Using Gulp to watch out for SCSS changes and converting SCSS to CSS


## Testing

### Manual Testing

For manual testing I have tested on the following browsers. *Firefox*, *Chrome*, *Edge* and *IE11*. I had to add some css fixes for both Microsoft Browsers.

I used an Alcatel U5 for mobile phone resolution testing and a Dell Inspiron 5567 for all other testing.

After running each possible scenario multiple times, going over each feature, user stories and client requirements I then validated my HTML and CSS using the following:

- [HTML Validation](https://www.freeformatter.com/html-validator.html)
- [CSS Validation](https://jigsaw.w3.org/css-validator/)


#### Scenarios

- Try registering a user that already exists on the system
- Register a new user
- Login with incorrect details
- Login in with correct details
- Create a new video
- Edit a video
- Delete a video
- Share a video
- Vote Up a video
- Vote Down a video
- Vote Down a video to -5 and see if it gets deleted
- Order profile videos by Reposted and Original
- Order profile videos by Category
- Order all videos by User
- Order all videos by Category
- Edit a video using the URL and video id for a video that is mine
- Edit a video using the URL and video id for a video that is another user’s video
- Delete a video using the URL and video id for a video that is mine
- Delete a video using the URL and video id for a video that is another user’s video
- Logout


### Unit Testing

This project has 20 Unit Tests overall:

- ***testA***: This test is for the username which is going be used at later stage to get the users id

- ***testB***: This test is for registering a new user. This tests an already existing username and comes back as exists in the system but works perfect using a non existing username I just don't want to keep creating new users for every test

- ***testC***: This test is for seeing if a username already exists

- ***testD***: This test is for authentication and checking if the login details match users in the database

- ***testE***: This test uses the login username set in the first test and gets a user id using this username

- ***testF***: This test is for getting a list of users profile videos and I just use my own account to test against with my user id so it only shows my videos

- ***testG***: This test is for getting a list of other users profile videos and I just use my own account to test against with my user id so it only shows their videos

- ***testH***: This test creates a new video based on some test data, once the video is created the test does a query to the database to get the video id of the newly created video and then I use a function to set the video id as a global variable to be used for editing and deletion tests to ensure no data is left on the database from the tests

- ***testI***: This test is for finding a video by video id

- ***testJ***: This test is for editing a video and then checking if the new data matches the original test data

- ***testK***: This test is for ordering videos by categories

- ***testL***: This test is for ordering my videos by reposted (saved) or original videos (posts)

- ***testM***: This test is for ordering videos by username

- ***testN***: This test is for getting the list of video categories 

- ***testO***: This test is for getting a categories id by category name 

- ***testP***: This test is registering a users vote and then checking if they voted 

- ***testQ***: This test is for testing if a user has voted on a specific video

- ***testR***: This test is for calculating the total amount of votes of a specific video

- ***testS***: This test if for getting all the vote information

- ***testT***: This test uses the video id set during testG to delete all test data of this video


## Deployment

During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used [GitHub](https://github.com/Garathd/vidx-video-sharing) to keep track of changes and to maintain version control in my code base.

The development version of my application is on GitHub and I push this code using *git push origin master* and the code is run and tested on Cloud 9 before being updated to heroku

The production version of my application is deployed to heroku and I push this code using *git push heroku master* and the live application can be found [here](https://vidx-video-sharing.herokuapp.com/).


### Heroku Deployment Steps

1. Go to the Heroku Website and create new app
2. Create requirements.txt and Procfile to tell heroku what is required to run the app
3. Login into Heroku Account via command line and add the newly created app
4. Go back to Heroku Website and in the settings tab click *Reveal Config Vars* and add IP and PORT vars from Project Config
5. Install [ClearDB](https://elements.heroku.com/addons/cleardb) and import local MySQL Database dump.sql
5. Restart all dynos
6. Finally do an initial git commit and push to heroku


## Content and Media

All content and media on this application comes from whatever the users decide to upload and its very existence on the system depends on whether user videos can retain a vote score of over -5


## Acknowledgements

- [ER Diagram Generator](https://app.sqldbm.com)
- [ClearDB](https://elements.heroku.com/addons/cleardb)
- [Adobe XD](https://www.adobe.com/uk/products/xd.html?sdid=88X75SKR&mv=search&ef_id=CjwKCAiAqt7jBRAcEiwAof2uKyYmJoV3wlWgAtyiwwWG5Q9ndPqtJejDidjgRFtcyOti86rbwX6lkhoCu8IQAvD_BwE:g:s&s_kwcid=AL!3085!3!315413032962!e!!g!!adobe%20xd)
