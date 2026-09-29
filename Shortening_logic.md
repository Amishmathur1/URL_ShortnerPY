## Shortening Logic

What we want:-
    - A shortner Code of the user given URL
    - It should be unique and not conflict with existing URLs in the database
    - After generating that Code we need to store it in the database along with the original URL

How to do it:-
    For generating the shortner Code, we will use base62 encoding since it guarantees uniqueness with no risk of hash collisions, and produces short, compact codes.
    
    Other Techniques which can be used are:- 
        - Using random.choises to generate a random string of characters
        - Using Hash-based techniques with collision techniques
        - using a Public shortner API

    We are Going with Base64 Encoding
    How do we achieve this Base62 encoding over the URL provided
    - Ok First take the URL that the user has provided us with and store it into our database 
    - Use the auto-generated ID number from the Database and perform Base62 Encoding on that number and generate a new code and save it in the database intself
    - Now use that changed code as the shortened URL endpoint and redirect that endpoint URL to the main original URL
