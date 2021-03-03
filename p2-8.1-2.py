import requests
import json

def get():
    pass #TODO
    resp = requests.get('http://httpbin.org/status/204')
    return resp.status_code

def post():
    pass #TODO
    resp = requests.post('http://httpbin.org/post', data = {'y' : 2, 'x' : 1})
    return resp
