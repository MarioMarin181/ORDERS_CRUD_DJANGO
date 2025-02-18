import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()

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

    if method == "GET":
        response = requests.get(
            API_URL + endpoint,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            params=data,
            headers=headers
        )
    elif method == "POST":
        response = requests.post(
            API_URL + endpoint,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    elif method == "PUT":
        response = requests.put(
            API_URL + endpoint,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    elif method == "DELETE":
        response = requests.delete(
            API_URL + endpoint,
            auth=(CLIENT_KEY, CLIENT_SECRET),
            data=json.dumps(data),
            headers=headers
        )
    else:
        raise ValueError("Invalid method provided.")

    return response.json()
