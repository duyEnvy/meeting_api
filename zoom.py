import jwt
import requests
import json
from time import time


# Enter your API key and your API secret
API_KEY = ''
API_SEC = ''

# create a function to generate a token
# using the pyjwt library


def generateToken():
    token = jwt.encode(

        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},

        # Secret used to generate token signature
        API_SEC,

        # Specify the hashing alg
        algorithm='HS256'
    )
    return token


# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
                  "type": 2,
                  "start_time": "2023-02-12T11: 43: 00",
                  "duration": "60",
                  "timezone": "Asia/Ho_Chi_Minh",
                  "agenda": "test",
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "true",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud",
                               'waiting_room': 'false'
                               }
                  }

# send a request with headers including
# a token and meeting details


def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))

    print("\n creating zoom meeting ... \n")
    # print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]

    print(
        f'\n here is your zoom meeting link {join_URL} and your \
		password: "{meetingPassword}"\n')


# run the create meeting function
createMeeting()
