# Simpsons Fan Page

![Website Display ](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/responsive_img.png)

## Author 
Kate_Ellen

## Project Overview 
This project has been created for educational purposes. 

This blog is about all things Simpson's. You can read blog posts and comments, and interact once you're a user. 

### Wire Frames 

The final result is slightly different as during the development stage the way things were displayed was not as user friendly as expected and I decided to go less minamilistic on the homepage. 

* [Homepage](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/home_page_wireframe.png)
* [Phone](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/phone_wireframe.png)
* [Characters](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/page2_wireframe.png)

## Styling

### Colours

The palette of colors for the site are primarily yesllow and black. They yellow is a classic reminder of the simpsons, and the black gave it a more defined look. 
I used the pink shade from the donut on top to make elements which you can hover over more noticible. 

![Color-palette](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/colour_scheme.png)
## Agile Process

## Project Goals

The goal of this project is to create blog page, where people can start a conversation. 
This project is for educational purposes only.

### Importance and Feasibility chart

| Opportunity/Problem                                                    | Importance | Viability/Feasibility |
| :--------------------------------------------------------------------- | :--------: | :-------------------: |
| 1. Users are able to register an account and login                     |     5      |           5           |
| 2. Users can read blog posts.                                          |     5      |           5           |
| 3. Users are unable to access certain fetaures if not registered.      |     5      |           4           |
| 4. Admin can add characters.                                           |     4      |           4           |
| 5. Users can view information on their favourite characters.           |     3      |           4           |

## User Stories

User Stories can be found at https://github.com/KateEllen/Simpsons-fan-page/projects/1 

### User Goals

* As a **User**, I want to easily understand the purpose of the site when navigating on it.
* As a **User**, I want to be able to have the same functionalities on different devices (mobile, tablet and PC).
* As a **User**, I want to be able to read blog posts easily on the site.
* As a **User**, I want to be able to sign up for an account.

### Registered User goals

* As a **Registered User**, I want to be able to easily login and logout of my account.
* As a **Registered User**, I want to be able to easily add comments to blog posts.
* As a **Registered User**, I want to be able read the blog. 


### Site Owner/Superuser goals

* As a **Site Owner/Superuser**, I want to be able to add new posts.
* As a **Site Owner/Superuser**, I want to be able to edit and delete characters.
* As a **Site Owner/Superuser**, I want to be able to access the admin section of the site to view comments and delete them.

## Testing

### Lighthouse Audit 
![Lighthouse Audit]()


### Validator Testing 
#### W3C CSS Validation 
Passed through the CSS validator with no errors.
![CSS Validator](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/css_validation.png)

#### HTML Validator 
All pages passed through HTML Validator with no errors.
![HTML Validator](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/html_validation.png)

#### PEP8
All python files passed through PEP8 with no errors. 
![JS Validator](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/python_validation.png)

#### Cross Browser and Device Testing

- I tested my site on the below. 
1. Samsung S20 - 5.97 X 2.72 
2. MacBook Pro - 12.78 X 8.94 
3. dev tools emulator: pixel 2 - SM 411 x 731 mm

- It was also tested on safari, chrome and firefox. 

#### Navigation
    1. Select navigation option
    2. Try to click the nav link.
    5. Ensure each link shows it's named page. 
    6. Repeat on all pages.

#### Register Page 
    1. The form fields have validation, it was tested using correct and incorrect input, receiving the expected output. 
    2. If no name entered, warning pops up. 
    3. Password secion denies password if not suitable. If enter all numbers it will no accept. 

#### Login Page 
    1. Click log in on nav. 
    2. Enter your name and password. 
    3. When correct credential are input, user gains full access to site. 
    4. When incorrect credentials are put in user does not gain entry to full site and error message is shown. 

#### Log Out Page 
    1. Click log out on nav. 
    2. Click log out button on log out page. 
    3. When correct logged out user does not have full access to site. 

#### Donut Home Page Link
  1. Click the spinning donut image. 
  2. Ensure it brings you back to home page. 
  3. Test on all pages. 

#### Comment Section
  1. Try to add comment.  
  2. If logged in, success message for pending comment should appear.  
  3. If logged out, access denied message is shown when you click on the link. 
  4. Test on all blog posts. 

#### Character Page
  1. Click character link.  
  2. Select character image to view character info.  
  3. If admin, option is given to delete character. 
  4. If not admin option to delete is not shown. 
  5. If logged in, option is given to edit. 
  6. If not logged no there is no option to edit. 

## Defects 

## Features

- HOME PAGE/ BLOG LIST PAGE
You can view the home page and blog posts here. 

- BLOG DETAIL PAGE
Here is where you can view the blog posts and leave comments. 

- CHARACTER PAGE
Here you can view the character's uploaded by the SuperUser. When not registered you can read about the chararcters, when 
logged in you can edit the character and if you are a SuperUser you can delete characters. 

- ADD CHARACTER
As a SuperUser you can add characters to the page. 

- EDIT CHARACTER
As a registered user you can edit character details. 

- DELETE CHARACTER
As a SuperUser you can delete characters from the character page. 

- ADD COMMENT PAGE
Registered users can leave comments on blog posts. If not registered you are redirected to signup. 

- LOGIN
Users who have already registered can login to the page and can leave comments and edit characters. 

- REGISTER
Users can sign up for an account if they do not already have one. 

- LOGOUT
Users who are logged in can easily log out. 

## Future Feautures

- 404 page
A modified 404 page to suit the style of the website.

- 500 page
A modified 500 page to suit the style of the website.

- Staff users
I would like to add approved users to the site. They would have the same access as a SuperUser. 

- Swag Shopping Page
I would like to add a merch page where fans can buy merch from the blog.


## Deployments 
### Heroku 

The site was deployed to Heroku. The steps to deploy are as follows: 
  - First, you must log into Heroku and go into the deploy tab. 
  
  - From here, you go to the Config Vars section. 

  ![Deployment1](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/config_vars.png)
  
  - You then enter Key: CLOUDINARY_URL and Value: your cloudinary key. Enter Key: DATABASE_URL and add your database value. Enter Key : SECRET_KEY and your secret key value. 
  
  - After finishing the above you will go to the 'Deploy' tab. 
  
  ![Deployment2](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/deploy_tab.png)
  
  - You then connect to your Github account. 

  ![Deployment3](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/deployment.png)
  
  - Once you enter your repository name, your Github project will be connected to Heroku. 
  
  - From here you have two options to deploy. You can select the option to enable automatic deploys, so when you commit any changes will automatically deploy. 
  
  - The second option is to manually deploy. When you click the 'Deploy' button, you will watch your files being uploaded. 

   ![Deployment4](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/deployment_2.png)
  
  - Once this is complete, a sucess message will appear with a 'View' button that will bring you to the deployed project. 

  ### Local/Gitpod

The live link can be found here - https://simpsons-blog.herokuapp.com/

### Credits

## Media Credits


## Acknowledgments
