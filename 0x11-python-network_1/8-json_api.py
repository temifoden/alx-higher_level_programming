#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as
a parameter.Displays the id and name from the JSON response if valid and
not empty. Otherwise, prints appropriate error messages.

Usage:
    ./8-json_api.py [letter]
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        try:
            json_response = response.json()
            if json_response:
                print(f"[{json_response['id']}] {json_response['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
