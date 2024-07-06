#!/usr/bin/python3
"""
Sends a POST reques to a given URL with an email as a parameter and displays
the responsee body

Usage:
    ./6-post_email.py <URL> <email>
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        data = {'email': email}

        response = requests.post(url, data=data)
        response.raise_for_status()     # check for http error
        print(response.text)
    except requests.ecceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
