import sys
import os
import requests
from dotenv import load_dotenv; load_dotenv()


TOKEN = os.environ.get('API_TOKEN')



def fetch_currency(currency):
    """
    this function gets currency as input, adds it to the connection string and makes the API request.
    """
    try:
        r = requests.get(f'https://v6.exchangerate-api.com/v6/{TOKEN}/latest/{currency}')
        
        if r.status_code >= 400:
            raise requests.exceptions.HTTPError

    except requests.exceptions.RequestException:
        sys.exit("An error occured, please check your API config or network settings and try again.")

    else:
        return r.json()

