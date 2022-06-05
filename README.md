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


## Data Model
| Field     | Data Type         | Purpose                          | Form Validation          |
|-----------|-------------------|----------------------------------|--------------------------|
| pk        | unique Identifier |                                  |                          |
| name      | CharField         | Character's Name                 | required, max length 200 |
| image     | CloudinaryField   | Image of Character               | required                 |
| bio       | TextField         | Biography of Character           | required                 |
| tag_lines | TextField         | Common phrases used by Character | required                 |

- [x] Create - If a user is a superuser and logged in, they will see a menu option to create a character
- [x] Read - Characters are read from the Database for the Characters Page, Update Character Page and Character Detail page
- [x] Update - If a superuser is logged in they will see an edit character button at the bottom of a character detail page to access the update functionality.
- [x] Delete - If a superuser is logged in they will see a delete character button at the bottom of a character delete page to access the delete functionality

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
![Lighthouse Audit](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/lighthouse.png)


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
- NAVIGATION:
1. Has easy navigation for users to go between login/logout functionality and Charcters vs Home/Blog Page
Options change based on user’s logged in status, Register Login are replaced by Sign Out
2. If User is super user, then they can access the admin function to add a character

- HOME PAGE/ BLOG LIST PAGE:
1. Allows user to see a list of blogs about the simpons, getting them right into the main focus of the website
2. Has Navigation to easily allow user to login or access admin options or switch to characters page
![Home page](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/home_page.png)

- BLOG DETAIL PAGE
1. Allows user to see the main body of a blog entry
2. Has Add comment button (note the button will encourage users to login as we want more user interaction)
3. Has Navigation to easily allow user to login or access admin options or switch to characters page
![Blog](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/blog_post.png)

- CHARACTER PAGE
Here you can view the character's uploaded by the SuperUser. When not registered you can read about the chararcters, when 
logged in you can edit the character and if you are a SuperUser you can delete characters. 
![Character page](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/character_page.png)

- ADD CHARACTER
1. Accessed by Admin(superuser) level only URL in navigation for superusers only
2. Form Validation to not allow blank entires
3. Template level check that user is super user to keep this functionality really restricted
![Nav for character](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/add_character_nav.png)
![Add character](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/add_character_page.png)

- EDIT CHARACTER
1. Accessed by registerd user level only URL by button on bottom of character Detail Page
![Edit character](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/edit_character.png)

- DELETE CHARACTER
1. Accessed by Super User level only URL by button on bottom of character Detail Page
2. Template level check that user is super user to keep this functionality really restricted
![Delete character](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/delete_character.png)

- ADD COMMENT PAGE
1. Has unauthenticated version where user is encouraged to login
2. Has authenticated version where user has entry form
3. Has validation such that a blank entries are not allowed
4. Has name field so users can still be anonymous 
![Add comment](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/add_comment.png)

- LOGIN
Users who have already registered can login to the page and can leave comments and edit characters. 
![Login](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/signin.png)

- REGISTER
Users can sign up for an account if they do not already have one. 
![Sign up](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/signup.png)

- LOGOUT
Users who are logged in can easily log out. 
![Sign out](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/signout.png)


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

### Local 

- Step 1: Go the git hub repo: https://github.com/KateEllen/Simpsons-fan-page

- Step 2: Press the green Gitpod button. 

- Step 3: If needed, Upgrade pip locally with: pip3 install --upgrade pip

- Step 4: Create a new .env file by typing: touch env.py and put the below values into the file. 
  - os.environ["SECRET_KEY"] = "YOUR_VALUE"
  - os.environ["CLOUDINARY_URL"] = "YOUR_VALUE" 

- Step 5: Install all requirements by typing: pip3 install -r requirements.txt into your terminal. 

- Step 6: Create the superuser so you can have access to the django admin, follow the steps necessary to set up the username, email and password by running the following management command in your terminal: python manage.py createsuperuser

- Step 7: Start your server by running the following management command in your terminal: python3 manage.py runserver

![gitpod](https://github.com/KateEllen/Simpsons-fan-page/blob/main/static/media/gitpod.png)
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

## Credits

### Media Credits
- Blog post images and images for characters were found on : https://frinkiac.com/
- Colour palette was creadted by using : https://htmlcolors.com/create-palette
- Donut and Kang images were found here : https://www.pngegg.com/

### Content Credits
- Most of my content for the blog posts and character information were found at : https://simpsons.fandom.com/wiki/Simpsons_Wiki

### Code Credits 
- I learned how to make the spinning donut here : https://flaviocopes.com/css-animations/
- Overall concept was developed by using Code Institute tutorials and other tutorials by: https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw. I adapted my comment section from Codemy.com tutorials. 
 

## Acknowledgments
- I had help from Niall Maher and Carolina Cobo with the theme of the page.
- I also had help from my wonderful mentor Malia, who always steers me in the right direction. 
