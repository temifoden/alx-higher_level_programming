#!/usr/bin/python3
"""
Fetches the GitHub user ID using Basic Authentication with personal
access token.

Usage:
    ./10-my_github.py <username> <token>
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data['id'])
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print(None)
