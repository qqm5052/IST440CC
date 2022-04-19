"""
Title: Log Class
Description: Used to log puzzle status
Course: Capstone Spring 2022 M5 Stack
Author(s): Qiu Qing Ma
Date: 3/28/22
Date Last Changed: 4/14/22
Version: 1.4
"""
import requests
import json

class Log:
    url = 'http://192.168.1.232:5000/status'    # need to change this host to whatever is running Eve

    def logstatus(teamname, puzzlename, message):
        if len(puzzlename.strip()) == 0:
            return False
        if len(message.strip()) == 0:
            return False

        statusdata = {
            "teamname": teamname,
            "puzzlename": puzzlename,
            "message": message,
        }
        jsondata = (json.dumps(statusdata))
        headers = {
            'Content-Type': 'application/json'
        }
        r = requests.post(url=Log.url, headers=headers, data=jsondata)
        return True

    # GET requests to get data from the status collection as json
    def getstatus_json():
        r = requests.get(url=Log.url)
        return (r.json())