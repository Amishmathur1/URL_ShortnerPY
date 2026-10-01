from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, HttpUrl, ValidationError
from Database.Database import add_url, add_short_code, check_code
from shorten_url import shortening_logic
from fastapi.responses import RedirectResponse
import re
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(redirect_slashes=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:5500", "https://urlshortnerfront.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WebModel (BaseModel):
    homepage : HttpUrl


@app.post('/shorten')
def get_url(url: WebModel):
    '''
        Function To get the URL Enterted by the User
        Which needs to be shortened.
            - Validating the HTTP Url link using Pydantic Library (HttpUrl)
            - Calling External Fucntions from DataBase.py and shorten_url.py for the necessary logic and functions
    '''
    try:
        base_id = add_url (str(url.homepage))
        short_code = shortening_logic(base_id)
        add_short_code (short_code, base_id)

        new_url = 'https://url-shortnerpy.onrender.com/' + short_code
        return {
            'new_url' : new_url
        }

    except ValidationError as e:
        return {e}

@app.get('/{short_code}', response_class = RedirectResponse)
def redirect_url (short_code: str):
    '''
        Function to implement the redirect url logic
        - Checks the endpoint/short_code of the URL store that into a var
        - Using a helper function validate the short_code is valid and return the original URL from the database
    '''

    try:
        original_url = check_code (short_code)
        url_link = original_url[0]
        return RedirectResponse(url=url_link, status_code=status.HTTP_302_FOUND)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Short code not found or error occurred: {str(e)}"
        )
