#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id variable from the header of a response
to a given URL
Usage:
    ./5-hbtn_header.py <URL>
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()     # Check for HTTP errors

        # Check if the X-Reques-Id is present in the response
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)
        else:
            print("X-Request-Id not found in the headers")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exceptoon: {err}")
