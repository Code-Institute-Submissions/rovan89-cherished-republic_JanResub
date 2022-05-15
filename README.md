# Cherished Repblic
(Developer: Devan Hayes)
[Employee Clocking System Live](link for site goes here)


## Tables of Contents
1. [Project Goals](#project-goals)
    1. [User Experience](#user-experience)
    2. [Target Audience](#target-audience)
    3. [User Stories](#user-stories)
    4. [Business Owner Stories](#business-owner-stories)
2. [Features](#features)
    1. [feature1](#feature1)
    2. [feature2](#feature2)
    3. [feature3](#feature3)
    4. [feature4](#feature4)
    5. [feature5](#feature5)
3. [User Input Validation](#user-input-validation)
4. [Languages](#languages)
5. [Frameworks and Tools](#frameworks-and-tools)
6. [Bugs](#bugs)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Project Goals
- To create a community driven site where people can come together and help thier local community become a better place.
- To allow users to interact and organise event's, creat discussions about thier local area.

### User Experience
The user first decides which option they would like to do, then a google sheet is updated with the data. 

### Target Audience
- The target audience for this site are poeple who want to better thier community.
- People who have ideas on how to improve their local area and need somewhere to share their thoughts.

### User Stories
1. As a User I can view a paginated list of posts so that I can easily select a post to view
2. As a User I can create posts so that share my concerns about my local area
3. As a User I can leave comments on posts so that I can voice my opinion
4. As a User I can upvote posts so that so I can help raise awareness of posts I agree with
5. As a User I can mark my comment as a "Solution" so that so that others can easily see this is a solution to the issue
6. As a User I can view comments of others so that I can read the conversation
7. As a User I can click on a post so that I can view the full text
8. As a User I can register an account so that I can comment and like posts
9. As a User I can create a community project so that other users can join and help solve the given issue
10. As a User I can edit, update and delete posts so that I can manage my postings.
11. As a Creator of a project I can create tasks in the project so that other users can assign themselves to a task


### Business Owner Stories
1. As a Site Admin I can create, read, update and delete posts so that I can manage my page content
2. As a Site Admin I can approve projects so that the community is safe from spam and unwanted posts

## Features
### Home Page Post Display
- The home page displays all user posts.  
- These posts are ordered by date of creation.
- Post on the main page display the author, when the post was created and the heading of the post.
- Post on the main page are clickable and can open up the Post Detail page.
 

## Features
### Start Discussion
- The Start Discussion feature allows users to create discussion posts.
- This is where user can post and raise awarnes of issues in their area.

### Post Detail View
- When the post is clicked on the main page it opens the post detail view.
- Post Detail user functions
    - Users can comment on posts
    - Users can like posts
    - Users can edit post
    - Users can delete posts


### Registration
- User can use the register link in the nave bar to be directed to the register form.
- To register the user must fill out the following feilds:
    - Username
    - E-mail
    - Password

### Login
- This feature allows users to login into their unique account

### feature6
- The Exit option allows the user to end the program.

## feature7
- The input validation checks has the user entered valid data and the correct amount of digits.
- If the incorrect amount of digits is entered the user an error message will be displayed in the terminal.

## Languages
- Python 3

## Frameworks and Tools
- gitHub
- Gitpod
- Git
- Cloudinary
- Heroku
- Django

## Libraries 
- PostgreSQL for the database
- Psycopg2 to connect to PostgreSQL
- DJ3 Cloudinary Storage
- Summernote

## Bugs
| **Feature / Function** | **Expected Result** | **Actual Result** | **Action** |
|-------------|------------|---------------------|-------------------|
| Register function in user/views.py | To register a user and redirect the user back to the home page | Page not found (404) | Fixed url path to point at home page |
| To allow users to create and post comments | For the comment to be posted | HTTP ERROR 405 | The function was indented incorrectly |
| In view.py the post function validates the comment | the comment should be validated | 'User' object has no attribute 'name' | Changed comment_form.instance.name = request.user.name to comment_form.instance.name = request.user.username|
| TodoItems get() menthod  | To return multiple items | Error raised: get() returned more than one ToDoList -- it returned 3! | Made change from get_object_or_404() to get_list_or_404()|

## Testing

| **Feature** | **Action** | **Expected Result** | **Manual Testing** | **Actual Result** |
|-------------|------------|---------------------|-------------------|--------------------|
| Start Discussion | This allows users to be redirected to the create post page where they can create their own post and start a community discussion | The user fills out the form and the contents get saved to the data base and are rendered o the home page | This was tested by clicking the Start Discussion button, filling out the create post form, the clicking the post button | Works as expected | 
| Edit Post | This allows users to edit posts on the site |  Users would click the edit button a be redirected to the edit post page | Click edit button, edit post click post button and update the database | Works as expected |
| Delete Post | This allows users to delete posts on the site |  Users would click the delete button which would delete the post | Click delete button and update the database | Works as expected |
| Like Post | The user can like any post on the website |  Click the like button once to like it and a second time to unlike it | | Works as expected |
| Comments | Users can read comments from other users and add their own comments | Add test comment and see if it has updated the database | | Works as expected |
| Fill in feature here | Fill in action to resolve issue here |  Fill in expected result here |Fill in Actual result here |


## Deployment
Heroku was used for the deployment of this program.
1. In the workspace terminal command line: "pip3 freeze > requirements.txt"
2. Create account on Heroku
3. On the dashboard page, select "create new app"
4. Click create app
5. Go to the "settings" tab, find "Config Vars" completed the foloowing convig vars: CLOUDINARY_URL, DATABASE_URL, DISABLE_COLLECTSTATIC and SECRET_KEY
6. In settings find add buid packs to app
    1. python
6. Scroll up to the navigation menu and find "deploy", select GitHub as deployment method
7. In the Deployment Method section select Gitub or connect to GitHub
8. In the "Connect to GitHub, searh the desired repository
9. Enable automatic deploys and then deploy branch
10. Once deployed click on "View" to open aplication

## Credits
- Hero Image by Freepik: freepik.com

### Code
- To implement time into the program I used https://www.programiz.com/python-programming/datetime/current-time 
- To find additonal features working with Google Sheets I used https://www.youtube.com/watch?v=yPQ2Gk33b1U&ab_channel=PrettyPrinted 
