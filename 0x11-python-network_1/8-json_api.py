#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a
parameter.
"""


from sys import argv
import requests

if __name__ == "__main__":

    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    values = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, values)

    try:
        js_ob = req.json()
        if js_ob:
            print("[{}] {}".format(js_ob.get("id"), js_ob.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
