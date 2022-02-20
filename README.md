# Milestone Project 4

## Purpose 

The purpose of this site is to complete the fourth Milestone Project for the Code Institute's Full Stack Developer course and can can be found [here](https://cob-milestonepj-4.herokuapp.com/).

## Cookbook Website

![Cookbook overview](static/assets/img/cookbook_app.png)

Fionn O'Brien (FOB) requested an app store to sell his beats. FOB requires a responsive website that allows users to listen to his beats and buy them for their own musical purposes. Once the user buys a beat(s) they will receive it as a download link in the sale confirmation email. The app allows users to create a profile where they can view their order history. An administation superuser will allow FOB to manage the site on his own with the capacity to add, delete and edit beats to the store.

## User Experience (UX)

### User stories

#### First Time User Goals

*   As a First Time user, I want to view clear and concise content on mobile, tablet and desktop.
*   As a First Time user, I want to learn and understand what the site offers.
*   As a First Time user, I want to easily navigate to the store.
*   As a First Time user, I want to easily search through the beat genres.
*   As a First Time user, I want to search the store with key words.
*   As a First Time user, I want to create an account.
*   As a First Time user, I want to listen to different beats.
*   As a First Time user, I want to add beat to my bag.
*   As a First Time user, I want to easily adjust my bag by removing beats if I require.
*   As a First Time user, I want to buy a buy using a credit card.
*   As a First Time user, I want to receive the beat(s) I bought in an email.
*   As a First Time user, I want to seemlessly navigate through all pages of the site.
*   As a First Time user, I want to easily connect with FOBs social platforms.
*   As a First Time user, I want to log out of my account.
*   As a First Time user, I want to buy a beat(s) without having to create an account.

#### Returning User Goals

*   As a Returning user, I want to view my order history.
*   As a Returning user, I want to update my user information.
*   As a Returning user, I want to sort through the beat by genre A-Z or price (high-low).
*   As a Returning user, I want to search for specific type of beat using the search tool.
*   As a Returning user, I want to navigate back to the beat store after adding a beat to my bag.
*   As a Returning user, I want to be able to generate a new password if I forgot my original one.

#### Frequent User Goals

The frequent user wants the following:

*   As a Frequent user, I want to look through the store for new beats or genres.

#### Admin User Goals

The admin user wants the following:

*   As an admin user, I want to manage (add, edit and delete) the beats on site.
*   As an admin user, view entire order history from all users.
*   As an admin user, I want to view and manage user accounts that signed up to the site.
*   As an admin user, I want to view all purchases via Stripe.

### Design

#### Colour Scheme

The main colours used are #292025 (dark purple), white, and #0dcaf0 (light blue). These colors were based around the FOB logo and the image used on the index page.

#### Font

The **Cairo** font is used through the whole app.

#### Imagery

Images and audio files were provided by and owned by my brother Fionn O'Brien (FOB) and he gave permission to use the files for this project.

#### Wireframes

For complete wireframes see this [PDF](static/assets/img/wireframes/wireframes_milestone_3.pdf).


### Limitations

There were no limitations.

## Features 

The features throughout the site are mininal text, larger text and clear buttons for clear navigation throughout the app. Use of Bootstrap buttons helped this.

### Existing Features

*   Navigation bar

    *   Featured on every page, but depending on the user can differ in the following two scenarios:
        1.  An everyday user - the nav bar contains links to the home, all beats, genres (dropdown to every genre link), profile (dropdown to login or register - this changes to my profile and logout options when the user has logged in), and the beat bag.
        1.  The only difference for an admin user is that a Beat Management option displays in the profile dropdown when they are logged in.
        
    *   The FOB Beat logo provides the user with a link back to the home page. 
    *   The navigation options becomes contained in a responsive Bootstrap burger icon for tablet and mobile devices that provides the nav options in a dropdown form.

*   Footer

    *   Featured identically on every page and contains Font Awesome icons used to provide external links to FOBs social platforms. Each external link has the attribute of target="_blank" which opens the link in a new tab, keeping the user on the site and allowing for seemless UX.

*   Home page

    *   The striking background image creates an inticing effect for the user.
    *   The big header text explains what the site is - a beat store
    *   The user has two immediate options - to use the search tool and search for a beat using key words or click the SHOP NOW button which navigates the user to beat store. 
    *   This is good UX as the user within the 1st 10 seconds of arriving know that this is a store and has two options to go straight to where they can explore.
    *   A short About section at the bottom gives further explanation to twhat the store is and how the user might use a beat for themselves. And a SHOP NOW button is provided at the bottom.

*   All Beats/Genres Page

    *   All beats (and info) are structured in card form. Each card has an image, audio player (to play the beat), the beat name, the price, and a genre button.
    *   There are navigation options within the card: the image and the beat name are links to the beat detail page. The genre button navigated the user to the beats of that specific genre.
    *   Within the audio player the user can play, pause, skip to a specific part of beat, mute the volume, and alter the speed of the beat.
    *   The user can sort the beats in the following ways: Price (high to low, or low to high), Name (A-Z, Z-A), and Genre (A-Z, Z-A). The sorting dropdown options are at the top right of the page and to the left a beat count is provide to tell the user how many beats there are based on the genre selected.
    *   A jump back to the top of the page button is provided in the bottom right of the page for good UX.
    *   Bootstrap responsive displays the beats columns of 4 on 1 row (4 x 1) for large screen, 3 x 1 for medium screens, 2 x 1 on smaller tablets, 1 x 1 on mobile.
    *   When the user selects a specific genre, the only difference is that the genre button appears underneat the main page header.
    *   For admin users - edit and delete options display underneath the genre button.

*   Beat Detail page

    *   Page header is the name of the beat
    *   The page provides the image, audio, price, description and genre button (if clicked navigates the user to that genres beat list).
    *   Two large button ot the bottom of the page to Add the beat to their bag or naviagte back to the beat store.
    *   Responsive - two columns on all device except mobile. Mobile displays a single column.
    *   For admin users - edit and delete options display underneath the genre button.

*   Beat Bag

    *   This page provides the user with all the beats they have added to the bag, the price, and an option to remove the item from the bag.
    *   The page also provides the total cost and options to proceed to checkout or go back for more beats.
    *   For desktop, the beats info appear in a table with the info spread across the row and the check out (and total) appears at the bottom of the page.
    *   For tablet, the total and checkout options appear at the top of the page. The beat imag, price and remove option appear on the left column and the right column on the same row displays the beat name and audio.
    *   For mobile, the tablet view is condensed into one single column.
    *   A jump back to the top of the page button is provided in the bottom right of the page for good UX.

*   Checkout page

    *   This page provides order summary (beat image, name, price, subtotal and total costs), user details name and email for where the order will be sent, the payment by debit or credit card option (processed by strip in the backend), and the option to complete the purchase.
    *   For desktop, the apge has 2 main columns. The left, contains the user details input options, a radio button option to save the user detals (if the user is not registered or not looged in - the option appears as Create an account or sign in to save details), the card payment input option, and the complete purchase option. The right, contains the order summary and total cost.
    *   For tablet and mobile, all features are consensed into 1 column with the order history push to the on top of the user details, etc.

*   Checkout success page

    *   This page provides a thank you message to the user and confirms an email has been sent to the email address provided.
    *   This page provides an order history tabe - order number, date, beats purchased and total cost, and an button aoption back to the beat store.

*   Register Page

    *   This provides the user the option to create a FOB Beat account.
    *   The user can use the form to input their email, username, and password. The user clicks the sign up button and they are directed to the verify email section.
    *   An email is sent to the given email and the user clicks the link to in the email to verify the email and a FOB Beat account is created.
    *   On the register page, the user has to option to navigate to the sign in (medium sized text below the sign up button) page if they already have an account and have mistakenly navigated to the register page.

*   Login Page

    *   The user can use the form to input their email or username, and password. The user clicks the **sign in** button and they are directed to the verify email section.
    *   Before selecting **sign in** the user can select the radio button to remember the users login deails.
    *   The user clicks the **sign in** button and they are directed back to the home page where they start to explore.
    *   There is medium size text under the page header asking the user if they are new to the site and provides a link to the register page in case the user has mistakenly navigated to the log in page.
    
*   Profile Page

    *   A header with short descriptive text informing the user about the options available on the page.
    *   For desktop and tablet, there are two cards on the same row with an image and a button each so the user can either go the recipes page or add recipes page. On mobile the cards will sit on top of each other in the same column.


*   My Profile Page

    *   This page provides a welcome message and instruction on how to use the profile page.
    *   The users order history is contained within a collapsable bootstrap accordian feature. When the user user slect the accordian their order history displays in table form - order number, date, items, and order total.
    *   Below the oreder history is the users main deails in a form - name and email. The user can update this information as they want and selcting the **update information** button will update and save the new information.

*   Beat Management Pages

    * 

*   Bootstrap Toast Messages

    *   A heading with relevant information for the user appears (with a hr underneath to give spacing) in the following user interactions with the app:
        *   If a user trying to register enters a username that already exists (top of registration page) - **Oops! This username already exists**
        *   If a user trying to register enters an email that already exists (top of registration page) - **Oops! This email already exists**
        *   If a user successfully registers an account (top of profile page) - **You have successfully registered! Happy cooking!**
        *   If a returning user successfully logs in (top of the profile page) - **Welcome, {username}**
        *   If a returning user enters an incorrect password (top of the log in page) - **Incorrect Username and/or Password**
        *   If a returning user enters an incorrect username (top of the log in page) - **Incorrect Username and/or Password**
            * The **Incorrect Username and/or Password** message was chosen for both password and username protection. This is user security protection. The hypothtetical hacker will not know what field they have entered incorrect details into.
        *   If a user has logged out (top of the log in page) - **You have been logged out**
        *   When a user has added a new recipe (top of Recipes page) - **Your recipe has been added**
        *   When a user has edited a recipe (top of Recipes page) - **Your recipe has been updated**
        *   When a user has deleted a recipe (top of Recipes page) - **Your recipe was deleted**
        *   When an admin user has added a new recipe category (top of Recipes page) - **New Category Added**
        *   When an admin user has edited a recipe category (top of Recipes page) - **Category Successfully Updated**
        *   When an admin user has deleted a recipe category (top of Recipes page) - **Category Deleted**
    *   If a user refreshes the page on which a flash message is displayed, the flash message with disappear. 

*   Error 404 and Error 500 pages

    *   These pages were created to inform the user the a certain page doesn't exist or that something went wrong. The page provides a link so the user can navigate back to the homepage seemlessly.


### Features Left to Implement

*   A visual popup describing that only one of each beat can added to the bag. This needs to be supported by backend code to prevent user from adding multiple counts of the one beat.


## Technologies Used

*   HTML - Used for the structure of the website.

*   CSS - Used to style the website.

*   Djang Framework - high-level Python web framework that provided user authentication, content administration, email functionality and all of the backend funcionality for FOB Beats.

*   JavaScript - used to provide interactive features throughout the site.

*   [Heroku](https://id.heroku.com/login) -  used to deploy app

*   [AWS]() - Used the S3 bucket to host static and media files

*   [Bootstrap](https://getbootstrap.com/) - used throughout the site for layout, styling and components. 

*   [Google Fonts](https://fonts.google.com/) - provided the *Cairo* font used throughout the website.

*   [Font Awesome](https://fontawesome.com/) - provided the icons used through the site.

*   [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/) - used to inpect each page, debug, lighthouse test and test different CSS styles.

*   [GitHub](https://github.com/) - hosting site to store the websites source code and Git pages used to deploy the live site.

*   [Gitpod](https://gitpod.io/workspaces) - the version control to check status, add, commit and push code to GitHubs repository for storage.

*   [Microsoft PowerPoint](https://office.live.com/start/powerpoint.aspx) - used to create the wireframes.

*   [PX converter](https://nekocalc.com/px-to-rem-converter) - to covert px values to rem values.

*   [Stack Overflow](https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete) - used to help create the pop up confirmation alerts when the user deletes data or tries to log out.


## Testing

### Testing Strategy

1.  Complete tests for user goals.

1.  Run all HTML pages through the [W3C HTML Validator](https://validator.w3.org/).

1.  Run all CSS files through the [W3C CSS Validator](http://www.css-validator.org/).

1.  Run all .js files through the [JShint](https://jshint.com/) validator.

1.  Run all python files through [PEP8 online](http://pep8online.com/)

1.  Run a lighthouse test for performance.


### Test Results

#### Validation Results

##### HTML Files

1.  add_recipe.html

    *   **ERROR:** The first child option element of a select element with a required attribute, and without a multiple attribute, and without a size attribute whose value is greater than 1, must have either an empty value attribute, or must have no text content. Consider either adding a placeholder option label, or adding a size attribute with a value equal to the number of option elements.

        *   **Fix:** Added empty value attribute to the first child option element.

    *   **ERROR:** The aria-describedby attribute must point to an element in the same document. 

        *   **Fix:** Updated the aria-describedby attribute to recipe_name to match for element in the label.


1.  recipe_list.html

    *   **ERROR:** Duplicate ID accordionExample.
    *   **ERROR:** Duplicate ID headingOne.
    *   **ERROR:** Duplicate ID collapseOne.
    *   **ERROR:** Duplicate ID headingTwo.
    *   **ERROR:** Duplicate ID collapseTwo.

    These errors repeat depending on how many recipes are store in the data base. 
    
    **NOTE/FIX** The errors do not appear if you run the validation for 1 card that contain the accordians. The backend is creating more cards/recipes so is there for duplicating the IDs. 
    
    To fix the error an attempt was made to impliment a loop counter id to contatonate accordian variable to generate uniique IDs for each. Due to time constraints for this project resources could not be put into solving this. The user doesn't suffer greatly for this.

1.  add_recipe_type.html

    *   **ERROR:** The aria-describedby attribute must point to an element in the same document.

        *   **Fix:** Updated the aria-describedby attribute to recipe_type to match for element in the label.


##### Python (app.py) 

1.  Line 79	 col 5	continuation line with same indent as next logical line

    *   **Fix:** Indented lines 79-84 by one.

1.  Line 182 line too long (86 > 79 characters)

    *   **Fix:** Put half the line indented on the next line

Python errors fixed and is producing 0 errors.

##### CSS

The CSS validations produced 0 errors.

*   ![CSS Validation Result](static/assets/img/testing/CSS_validation_result.png)

##### JaveScript Files

JavaScript validations produced 0 errors.


#### User Goal Results

##### First Time users

*   As a First Time user, I want to view clear and concise content on mobile - Testing was performed to ensure there was no clusters of over information, well spaced and aesthically pleasing on tablet and mobile.

*   As a First Time user, I want to learn and understand what the site offers - Testing was performed to verify enough information is uploaded to tell the user about what the site offers.

*   As a First Time user, I want to find the registration page - Testing was performed to verify enough information is given to user about how to navigate to the regisration page.

*   As a First Time user, I want to easily register a Cookbook account - Testing was performed on the registration form to verify that a user can register an account on this app.

*   As a First Time user, I want to recieve an email that welcomes me and acknowledges that I have created an account - Testing was performed to verify that when a user create an account they recieve a personal email. (NOTE: Please see the EmailJS results in the Validation Results section above).

*   As a First Time user, I want to add a recipe - Testing was performed on the recipe form input fields and the add recipe buttons to ensure a user can create a recipe.

*   As a First Time user, I want to view the recipe on the recipes page - Testing was performed on the recipe cards and the accordian features within it to ensure the user can view their recipe.

*   As a First Time user, I want to view other user's recipes on the recipes page - Testing was performed on the recipe cards and the accordian features within them to ensure the user can view other user's recipes.

*   As a First Time user, I want to be able to edit my recipes - Testing was performed on the user recipe cards on the Recipes page to ensure the edit button navigates the user to the Edit Recipe page. Testing was performed on all inputs and buttons in the edit recipe form function correctly so that the user can successfully update their recipe.

*   As a First Time user, I want to be able to delete my recipes - Testing was performed on the user recipe cards on the Recipes page to ensure that when the Delete button is selected, a pop up appears to confirm that the user want to delete. If the user confirms deletion, testing was done to confirm that the recipe has been removed from the Recipes page.

*   As a First Time user, I want to seemlessly navigate through the 6 pages of the site - Testing was performed on all navigation links to ensure the user can seemlessly navigate throughout the site.

*   As a First Time user, I want to easily connect with Cookbook's social platforms - Testing was performed on the socail icon links in the footer to ensure that the user is navigated to the chosen social media platform and that the link opens in a new tab to keep the user in the app allowing for seemless UX.

*   As a First Time user, I want to log out of my account - Testing was performed on the Log Out link in the Navigation bar to enusre that the user can successfully log out, that when the link is selected a pop up appear asking the user to confirm that they want to logout (as to avoid an unwanted log out), and the upon a successful logout, the user is redirected back to the log in page.

##### Returning Users

*   As a Returning user, I want to easily use a recipe while cooking - Testing was performed on the accordian features in the recipe cards to ensure the cook using the app can easily open and close the ingredients and cooking instructions accordians individuallty, so the user doesn't have to scroll through all the ingredients to get to the cooking instructions or visa versa. 

*   As a Returning user, I want to easily add more recipes - Testing was performed to ensure a user can create and store as many recipes as they would like and that they all appear on the Recipes page.

*   As a Returning user, I want to categorize all my recipes - Testing was performed on the choose category dropdown in the Add and Edit recipe forms to ensure a user can create and store as many recipes under a variety of categories.

*   As a Returning user, I want to search for certain recipes on the recipes page - Testing was perfomred on the search bar and the search button to ensure the user can search the recipe list using keywords and that the user is informed if no matches are found for the users keywords.

*   As a Returning user, I want to navigate back to the recipe page after finding a recipe using the search tool - Testing was performed on the reset button of the search tool so a user can easily navigate back the recipe page after using the search tool.

##### Frequent Users

*   As a Frequent user, I want to add, edit and delete as many of my recipes as I want - Testing was performed on the database and its capacity to (1) Store multiple recipes (2) handle recipe that are constantly being edited, updated, and deleted, so that the user has confidence that their data wont be lost and the app can handle their demand for manipulating a recipe when that want.

*   As a Frequent user, I want to use this app as my only cooking tool - Testing cannot be performed on this parameter as this can be subjective and some users may prefer other simailar apps. If we had the capacity, we could use analytics to measure rates of returning users and provide surveys to ask how users rate the app, is there other apps that they like too, etc.

*   As a Frequent user, I want to search for new recipes other users have added over time - Continuous testing was performed on the search tool to ensure a user can easily search the recipe list using the search tool.

##### Admin User Goals

*   As an admin user, I want to manage (add, edit and delete) the recipe categories - Testing was perfomred on the manage category pages to ensure the admin user can easily and quickly manage the recipe categories to meet the demand of the regular users.


#### Lighthouse Test Results

See the following lighthouse test results:

![Lighthouse mobile results](static/assets/img/testing/Lighthouse_test_mobile.png) \
**Mobile test result**


![Lighthouse desktop results](static/assets/img/testing/Lighthouse_test_desktop.png) \
**Desktop test result**


These test results indicate that the site peforms very well overall. It also shows that the Performance could be improved a lot for mobile.

Due to the time constaints of this project it is not feasible to act further on this. In a normal working situation time would be taken to optimise performance.


## Deployment

### Project Creation

Created the project by:

1.  Navigating to my [user profile](https://github.com/cobobc).
2.  Selecting the **Respositories** tab.
3.  Selected the **New** button.
4.  Under Repository tempate, select the Code Institute template from the dropdown menu.
5.  Entered milestone_project_4 for the **Repository name**.
6.  Select **Create Repository**. 

### During the Project

The following commands were used throughout the project:

*   `git add .` - This command was used to add files to the staging area before commiting.
*   `git commit` - This command was used to to commit changes to the local repository.
*   `git push` - This command is used to push all commited changes to the GitHub repository.
*   `python3 manage.py runserver` - run the site locally
*   `python3 manage.py migrate` - migrate newly installed applications
*   `python3 manage.py loaddata` - load beat and genre data

### Deployment to Heroku

1.  Create application:

    1. Navigate to Heroku.com and login.
    1. Select the **new** button.
    1. Select **create new app**.
    1. Enter the app name.
    1. Select the region.
    1. In the resourced tab > Provision new Postgres, select **Provison** in the Postgres plan popup.

1. Connect Heroku to the terminal:

    1. In the gitpod terminal, install `dj-database-url`.
    1. In the gitpod terminal, install `psycopy2-binary`.
    1. In the gitpod terminal, run `freeze > requirements.txt`.

    1. In setting.py, import dj-database-url from the heroku app > settings > reveal configs.
    1. Save settings.py
    1. Run `python3 manage.py migrate`
    1. Run `python3 manage.py loaddata genres`
    1. Run `python3 manage.py loaddata beats`
    1. Sign in as superuser in the terminal.
    1. In the gitpod terminal, install `gunicorn`.
    1. Create Procfile to serve the app (fob-beats).

    1. In the gitpod terminal, run `heroku login -i`
    1. Run `heroku config:set DISABLE_COLLECTSTATIC app cob-milestonepj-4`

    1. Update ALLOWED HOST FIELD in settngs.py.
    1. Save settings.py

    1. In the terminal, run `git add .`
    1. Run `git commit`
    1. Run `git push`
    1. Run `git push heroku main` to deploy to heroku
    1. Run `heroku git:remote -a cob-milestonepj-4`
    1. Run `git push heroku main`


1.  Set up connection to Github Repository:

    1. Select the **Deploy tab > GitHub > Connect to GitHub**.
    1. Enter the repository name for the project and select **search**.
    1. When the repo has been found, select the **connect** button.

1.  Enable automatic deployment:

    1. Select the **Deploy** tab.
    1. In the Automatic deploys section, choose the branch you want to deploy.
    1. Select **Enable Automation Deploys**.


1. Connect Django to the S3 Bucket:

    1.  In the terminal, install `boto3` and `django-storages`
    1. Enter the AWS_ACCESS_KEY and SECRET_KEY into heroku configs and settings.py
    1.  Add USE_AWS value to True in Heroku
    1. Delete the DISABLE_COLLECTSTATIC value in heroku
    1. Create a custom_storages.py file for product images.

### Run Locally

**Note:** The project will not run locally with database connections unless the user sets up an env.py file configuring IP, PORT, MONGO_URI, MONGO_DBNAME and SECRET_KEY.

1.  Navigate to the GitHub [Repository](https://github.com/cobobc/cob_MilestonePJ_4.git).
1.  Select the Code drop down menu.
1.  Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1.  Open your developement editor of choice and open a terminal window in a directory of your choice.
1.  Use the 'git clone' command in terminal followed by the copied git URL.
1.  A clone of the project will be created locally on your machine.


## Credits

### Code

*   [W3Schools](https://www.w3schools.com/) helped throughout the project with general element and attribute uncertainties.

*   [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) - used this as the source code for the theme of the app. Includes JS for interactive nav bar use.

*   [Stack Overflow](https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete) - used to help create the pop up confirmation alerts when the user deletes data.

*   [gitconnected](https://levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317) - used to help with creating error 404 page for html and python.

*   [Handling Application Errors](https://flask.palletsprojects.com/en/2.0.x/errorhandling/) - used to help with creating error 500 page for html and python.

*   Tim Nelson a Tutor at Code Institute code in the Flash Framework and mini project lesson helped give my project a great base to work off.


### Content 

The contents of this app was all created by Ciaran O'Brien.

### Media 

Images and audio files were provided by my brother Fionn O'Brien (FOB) and he gave permission to use the files for this project.

### Acknowledgements

I'd like to thank my mentor Spencer Barriball for his guidance, efficiency and positivity throughout my project.

I'd like to thank mentor Daisy McGirr who kindly stepped in to take my final project review as Spencer was on holidays. I am so thankful for her help.

Thank you to Tim Nelson a Tutor at Code Institute whose teaching techniques helped me understand how to build a full stack site using Django. A lot of this project's code structing and testing was sourced from Tim's amazing Mini Project and Flash Framework lessons.

Thanks to various Slack users for helping with issues I had throughout the journey.

Thanks to tutors for stepping in when I was really stuck on a bug.

Thank you to my tester friends Fionn and Ollie who allowed me to contsantly test my email functionality with their email addresses.