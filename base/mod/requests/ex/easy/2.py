#!/usr/bin/env python3


import requests, json


#use post  

url = "https://httpbin.org/post"
data_playload = {"name": "devops"}

try:
    response = requests.post(url, data=data_playload)

#check response status
    response.raise_for_status()

#parsing to python dic

    response_data = response.json()

#get info from 'form'

    form_data = response_data.get('form')

    print(form_data)

except requests.exceptions.RequestException as e:
    print(f"You have an error {e}")
