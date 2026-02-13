# Barkley Group Project - Project 4

The link to live project can be found here - https://barkley-group-4246915066fd.herokuapp.com/

The link to github repository can be found here - https://github.com/declanwatts97/barkley_group_project

### Introduction

Welcome to Barkley Group! We are an accountancy practice located in the Team Valley, Gateshead. Explore our site for information about our services provided, create an account to become a client, or request a consultion with one of our advisors.

## Table of Contents


## User Experience

### User Requirements

The website has been created with the below goals in mind:



## User Stories
### Website Visitors



### Acceptance Criteria



### Goals of Site Developers



### Acceptance Criteria



## Structure

The site has 9 active pages:


### Navbar


### Footer



### Home Page


### Our Servies Page


### Request a Meeting Page



### Log In Page



### Sign Up Page



### My Account Page



### Checkout Page



### Sign Out Page



### Payment Success Page



## Design



### Entity Relationship Diagram



### Colour Scheme

 - The main colour scheme was dark green for the header and footer, and white for the background of the pages.
 - The button colours on this website are Green.
 - The heading colours on the our services page are the same dark green, showing they are individual services.
 - The rest of the headers are black, as they are utility headers.

### Font

- The font used in this project are just the standard global font for HTML pages.

## Imagery

All images used on this website were AI generated.

These were from both ChatGPT and Gemini. In the future this would look to be changed to properly designed images.

ChatGPT was used to create the business logo.

## Technologies Used

### Development Tools

- Github: For hosting code through repositories and deployment.
- Heroku: For hosting and deploying the final site.
- VS Code: Used for writing and testing local code prior to sending to github.
- HTML5: The standard language of a web page.
- Javascript - For creating the navbar.
- Python - Used through the Django framework for the models, views, url's of the site. The style guide used for writing the code in this project was PEP8.
- Django - the django framework was used for the building of this site.
- Taiwind: To create responsive design and also page styling through the use of classes.
- Favicon.io: For adding the favicon on the title bar of webpage.
- Gemini AI - for troubleshooting as well as producing images.
- ChatGPT - for creating the logo.
- PostgreSQL - for hosting the site database.

## Deployment

### Deployment to Heroku

This site has been deployed to Heroku. To view, please see below:

1. View the GitHub repository. This project is found at title (https://github.com/declanwatts97/barkley_group_project)
2. You can view the deployment on Heroku by visiting (https://barkley-group-4246915066fd.herokuapp.com/)

### Deployment Procedure

See below step by step instructions for how to deploy to Heroku:

First you need to clone this repositories URL, by copying the HTTPS. You can then open the terminal in your code editor and type git clone. Paste the previously copied URL and enter to create your local clone.

1. Create a new app on Heroku with a unique name.
2. Click on the settings tab and reveal the config vars. Add a key of DISABLE_COLLECTSTATIC and add a value of 1.
3. Install a production ready web server to the project with pip3 install gunicorn~=20.1.
4. Add your web server to requirements.txt with pip3 freeze --local > requirements.txt
5. Create a file named Procfile at the root directory of the project.
6. In the Procfile add web: gunicorn my_project.wsgi.
7. In your settings.py file add '.herokuapp.com' to your allowed hosts list.
8. Return to heroku and click on the deploy tab.
9. Connect and log in to github after clicking the connect to github box.
10. Scroll to the bottom of the page and manually deploy your site on the main branch.
11. Open the resources tab and choose an Eco Dyno.
12. Click open app to view your deployed project!

## Testing

### User Stories Testing



### Manual Testing



9. Dev Tools - I checked my code through the console on chrome dev tools. One area to improve in the future is the that tailwind CCS needs to amended to a post CSS plugin or use the tailwind CLI for production. This will be fixed in future updates.

### Testing Summary

As shown in the breakdown of testing above, the website meets all user and developer goals as well as being fully responsive. This is fully operational from a design and production viewpoint. Manual testing was the primary form of testing used in this project. Automated testing will be implemented in the future.

### Browser Compatibility

This website was tested on the below browsers to ensure compatibility:

- Safari
- Google Chrome
- Microsoft Edge
- Firefox

## Credits
### Content and Inspiration

- Images: images taken from Unsplash free as uploaded by other users.
- Content: content inspired by the current website this is based on.

### Acknowledgements 

- Tailwind: for most of the styling used on the website.
- Code Institute: for ideas, assistance and the LMS, which was referred back to while designing this project.
- Favicon.io - for the favicon used in browser title.
- Unsplash - for all images used on the webpage.
- Gemini AI - for the images, as well as occasional assistance troubleshooting.

## Contact Information
- For any queries or feedback, please contact declan.watts97@gmail.com

