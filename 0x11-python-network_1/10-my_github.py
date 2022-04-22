#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""


import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    pssw = argv[2]
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(user, pssw))
    print(req.json().get("id"))
