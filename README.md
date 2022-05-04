# Employee Clock in System
(Developer: Devan Hayes)
[Employee Clocking System Live](link for site goes here)

![Deployed Program]()
![Google Sheets Image]()


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
8. [Validator Testing](#validator-testing)
9. [Deployment](#deployment)
10. [Credits](#credits)

## Project Goals


### User Experience
The user first decides which option they would like to do, then a google sheet is updated with the data. 

### Target Audience
- Bussiness' that would like to track employee clock in and out times

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
10. As a Creator of a project I can create tasks in the project so that other users can assign themselves to a task

### Business Owner Stories
1. As a Site Admin I can create, read, update and delete posts so that I can manage my page content
2. As a Site Admin I can approve projects so that the community is safe from spam and unwanted posts

## Features
### feature1
- The options menu has four options to choose from.
    - Option one allows the user to clock in by entering their employee number.
    - Option two allows the user to clock out.
    - Option three allows the user to add new employees to the list of current employees
    - Option four allows the user to quit running the program.

![feature image]()

### feature2
- The clock-in option allows an existing employee to enter their employee number.
- The nubmer runs through a validation function to check the correct lenght of the number entered.
- This then creates a new row in the Google Sheet (employee_clocking_system) and inputs the employees number, name and time of clock in.

![feature image]()

### feature3
-The clock-out option allows a user who has already clocked in to add a clock-out time to the row created in the clock-in section (Google Sheets)

![feature image]()

### feature4
- This option allows the user to add a new employee to the list.
    - First the user is prompted to enter a user name.
    - Next the user is prompted to add the hourly rate of the new employee.
    - Finally the new user is assigned an employee number and a new employee has been successfully added to the list

![feature image]()

### feature5
- The User Feedback option allows the user to give feedback.
- The user enters their feedback and the user_feedback worksheet in google sheets is updated

![feature image]()

### feature6
- The Exit option allows the user to end the program.


## feature7
- The input validation checks has the user entered valid data and the correct amount of digits.
- If the incorrect amount of digits is entered the user an error message will be displayed in the terminal.

![feature image]()

- Input validation checks if alphabetical characters have been used.
- If alphabetical characters are used instead of numbers an error message will be displayed in the terminal. 

![feature image]()

- Input validation checks if special characters and spaces are used.
- If special characters are used an error message will be displayed in the terminal. 

![feature image]()


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
| Fill in function here | Fill in expected result here | Fill in Actual result here | Fill in action to resolve issue here|
| Fill in function here | Fill in expected result here | Fill in Actual result here | Fill in action to resolve issue here|
| Fill in function here | Fill in expected result here | Fill in Actual result here | Fill in action to resolve issue here|
| Fill in function here | Fill in expected result here | Fill in Actual result here | Fill in action to resolve issue here|

## Testing

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Fill in feature here | Fill in action to resolve issue here |  Fill in expected result here |Fill in Actual result here |
| Fill in feature here | Fill in action to resolve issue here |  Fill in expected result here |Fill in Actual result here |
| Fill in feature here | Fill in action to resolve issue here |  Fill in expected result here |Fill in Actual result here |
| Fill in feature here | Fill in action to resolve issue here |  Fill in expected result here |Fill in Actual result here |
| Fill in feature here | Fill in action to resolve issue here |  Fill in expected result here |Fill in Actual result here |

## Validator Testing 
### PEP8 Validation
- The PEP8 Valitator has resulted in no errors or warnings

![PEP8 Validator]()

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
### Code
- To implement time into the program I used https://www.programiz.com/python-programming/datetime/current-time 
- To find additonal features working with Google Sheets I used https://www.youtube.com/watch?v=yPQ2Gk33b1U&ab_channel=PrettyPrinted 
