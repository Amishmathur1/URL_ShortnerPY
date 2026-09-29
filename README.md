# URL_ShortnerPY

Building a URL Shortner in Python
Requirements:- 
    - A simple UI Page which has a text input field and a submit button 
    - An output field which displays the shortened URL

Functional Requirements:-
    - Accept the URL input from the user - DONE
    - Generate a unique shortened URL from the original URL - DONE
    - Store the shortened URL in a database - DONE
    - Provide the shortened URL to the user
    - Redirect the user to the original URL when they click on the shortened URL
    - Return an Error if the shortened URL is not found in the database
    - Provide the user to delete the shortened URL from the database

Non-Functional Requirements:-
    - The URL generated should be unique and should not conflict with the existing URL's in the database
    - Appropriate HTTP status should be returned for each request
    - URL's must be validated first before shortening
    - Database operations should be seperate form the shortning logic

Database Table Schema:-
    A Single Table with the following columns:-
        - id: Primary Key
        - original_url: The original URL
        - short_code: The shortened URL
        - created_at: Timestamp of when the URL was shortened

Defining The Endpoints:-
    - POST /shorten: Accepts the original URL and returns the shortened URL
    - GET /<short_url>: Redirects the user to the original URL
    - DELETE /<short_url>: Deletes the shortened URL from the database

Files Needed:-
    - app.py - The main application file with the FastAPI app definition
    - database.py - The Database connection and setting up the table scheme using PostGre SQL for this includes the funtions of models.py also
    - short_url.py - The main logic for shrotening the URL and storing it into the database
    - Frontend Section with a basic template created using HTML and CSS
    - requirements.txt - The list of dependencies required to run the application