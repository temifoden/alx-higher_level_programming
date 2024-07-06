#!/usr/bin/python3
"""
Fetches the 10 most recent commits from a GIThub respository

Usage:
    ./100-github_commits.py <respository_name> <owner_name>
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    try:
        response = requests.get(url)
        response.raise_for_status()     # Check for HTTP errors

        commits = response.json()[:10] # Get the lastest 10 commits

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
