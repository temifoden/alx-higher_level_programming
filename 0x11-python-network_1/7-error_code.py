#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the HTTP status code is >= 400, prints "Error code: <status_code>"

Usage:
    ./7-error_code.py <URL>
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Display the response body
        print(response.text)

        # Check if the status code is >= 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")

    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
