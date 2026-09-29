## WorkFlow Model of this Project


Progression Chart
    - Create a Database to Store the url, short_code, id, and timestamp - DONE
    - Create the GET /shorten endpoint which takes the URL input - DONE
    - Validate the HTTP URL using Pydantic HttpUrl module - DONE
    - Store the user provided URL into the PostGreSQL - DONE
    - Extract the Auto-Incrementing ID value and Generate a Base62 Encoded Code for it - DONE
    - Create the new URL with the new Encoded Value as the Endpoint
    - Redirect the new URL to the original URL fetching from the Database
    - Create a Simple Frontend HTML + CSS Page for the following 