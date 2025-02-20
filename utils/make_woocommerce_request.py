import requests
import json
import os

from dotenv import load_dotenv
from django.conf import settings

dotenv_path = os.path.join(settings.BASE_DIR, ".env")
load_dotenv(dotenv_path)

API_URL = os.getenv("WOOCOMMERCE_API_ROUTE")
CLIENT_KEY = os.getenv("WOOCOMMERCE_CLIENT_KEY")
CLIENT_SECRET = os.getenv("WOCOMMERCE_SECRET_KEY")

def make_woocommerce_request(endpoint, method, data=None):
    """Makes a request to the WooCommerce API.

    Args:
        endpoint (str): The endpoint to make the request to.
        method (str): The HTTP method to use.
        data (dict, optional): The data to send with the request. Defaults to None.

    Returns:
        dict: The response from the API.
    """
    headers = {
        'Content-Type': 'application/json'
    }

    url = f"{API_URL}{endpoint}"

    if method == "GET":
        response = requests.get(
            url,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            params=data,
            headers=headers
        )
    elif method == "POST":
        response = requests.post(
            url,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    elif method == "PUT":
        response = requests.put(
            url,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    elif method == "PATCH":
        response = requests.patch(
            url,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    elif method == "DELETE":
        response = requests.delete(
            url,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    else:
        raise ValueError("Invalid method provided.")

    return response.json()
