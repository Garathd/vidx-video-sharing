# milestone-project-4

This project is inspired by looking for streams and finding dead links to a TV Show or Movie that you maybe want to view. This application is not strictly limited to streaming and in no way shape or form am I promoting or encouraging this application to be used for streaming links it was just an inspiration!. I want this application to be something else, ideally originally created user content that works with momentum based videos. If it's bad then it gets deleted if it's good then it stays. 

If a video link is rated -5 then the video gets deleted from the database unless someone else has saved (reposted) the video to their profile and in this circumstance a reposted (saved) video is only viewable and accessible to the user that has saved it.


## UX

The clients requirements are:

- To be able to register and sign into an account
- To be able to create, edit, delete and view videos on their account
- To be able to save other users videos on their profile
- To be able to up vote and down vote on videos of other users
- For videos to be deleted if the get -5 in vote score

## Design

My design inspiration was essentially a YouTube and Facebook hybrid. I also took a little inspiration from Reddit with the Up Votes and Down Votes as I like it better than like and dislike. I like the layout of how Youtube Presents it's videos. I just modified it slightly to show 3 videos per row instead of 4 on the large resolution screen devices and then just shows one video per row on smaller resolution devices. There was really no need to use any wirefram. I have a few small sketches as I more or less knew in my head how I wanted the site to look.

## Features

The features of this application are as follows:

- Ability to Register and Sign Into an Account
- Ability to Create, Edit, Delete and View Videos
- Ability to Repost videos to your profile page
- Ability to vote on videos and if video has score of -5 then the ability to automatically delete them
- Ability to see if voted on a particular video and to view its voting score
- Ability to order by Category, Username, Reposted Videos and Original Videos

## Features Left to Implement

I still feel I could add a lot of features some more essential than others. I think the most essential thing would be a better authentication set up and the use of sessions. The way the user authentication works currently is that if a username and password is found in the database upon login check it saves the username in a global variable which is then used throughout the application to query different stuff from the database. 

Also another thing I have really considered but I think would be potentially better at a future stage is to have each of the video categories as sub menu items to the All Videos menu item. It would definitely make it easier for users to find videos of a specific category. But then the more I thought about it I realised that if I only initially had a small number of users with below 200 videos in total it miight be better for them to scroll through all the videos and vote up or down on the videos. If a user got sick of seeing the same videos they would more than likely vote down a video ensuring that below par or questionable posts can be removed quicker.

If I was to get more users with more videos I would definitely implement the menu seperation of categories and also add a feature to each video to report users if content is deemed innappropiate by users. If someone gets 3 reports on their account then their profile is automatiacally deleted from the system. It works more or less the same as if a video gets -5 vote on a video. 

I think another cool feature would be if a username is clicked then it brings you that users profile where you can see information about them as well as posts on their page and also the ability to send messages to other users. The way it currently works is that if a username is clicked than the videos are ordered by that user.

The ability to search videos is also a feature I would definitely implement at a latter stage if I was to get more videos and it was something initially that I was seriously considering doing in the first version of this application.


## Technologies Used

### Python and Flask

Flask is the Python Framework I’m using for this application

### CSS

I'm using SCSS to build my css stylesheets and probably a little unconventially I'm using [Materialize](https://materializecss.com/) and also [Bootstrap 4](https://getbootstrap.com/). To be honest though it doesn't seem to have any adverse effects and over all looks better and is more responsive and visually pleasing out of the box when used together than individually. It was intially a mistake on my part but ended up looking pretty good. I also did a little research and decided to use the two of them after reading this [article](https://stackoverflow.com/questions/28613848/is-it-possible-to-integrate-materializecss-into-bootstrap). I also tried Material Design for bootstrap but wasn't happy with the way it looked

### JQuery

I have only used minimal JQuery. I have used it for the scroll to top button, the mobile menu and for select options for the forms in materialize.

### Gulp

Using Gulp to watch out for SCSS changes and converting SCSS to CSS



## Testing

### Manual Testing

### Unit Testing

This project has 19 Unit Tests overall:

- ***testA***: This test is for setting the login username for a user

- ***testB***: This test is for registering a new user. This tests an already existing username and comes back as exists in the system but works perfect using a non existing username I just don't want to keep creating new users for every test

- ***testC***: This test is for authentication and checking if the login details match a users in the database

- ***testD***: This test uses the login username set in the first test and gets a user id using this username

- ***testE***: This test is for getting a list of users profile videos and I just use my own account to test against with my user id so it only shows my videos

- ***testF***: This test is for getting a list of other users profile videos and I just use my own account to test against with my user id so it only shows their videos

- ***testG***: This test creates a new video based on some test data, once the video is created the test does a query to the database to get the video id of the newly created video and then I use a function to set the video id as a global variable to be used for editing and deletion tests to ensure no data is left on the database from the tests

- ***testH***: This test is for finding a video by video id

- ***testI***: This test is for editing a video and then checking if the new data matches the original test data

- ***testJ***: This test is for ordering videos by categories

- ***testK***: This test is for ordering my videos by reposted(saved) or original videos(posts)

- ***testL***: This test is for ordering videos by username

- ***testM***: This test is for getting the list of video categories 

- ***testN***: This test is for getting a categories id by category name 

- ***testO***: This test is registering a users vote and then checking if they voted 

- ***testP***: This test is for testing if a user has voted on a specific video

- ***testQ***: This test is for calculating the total amount of votes of a specific video

- ***testR***: This test if for getting all the vote information

- ***testS***: This test uses the video id set during testG to delete all test data of this video


## Deployment

### Heroku Deployment Steps

## Content

## Media

## Acknowledgements

