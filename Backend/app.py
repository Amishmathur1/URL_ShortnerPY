from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, ValidationError
from Database.Database import add_url, add_short_code
from shorten_url import shortening_logic
import re

app = FastAPI()

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
        
        l = re.findall("https://.*/", str(url.homepage))
        new_url = l[0]+short_code
        
        return {
            'Message' : f'new_code {short_code}',
            'New_URL' : new_url
        }

    except ValidationError as e:
        return {e}
