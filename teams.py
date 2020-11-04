"""This is a sample script for Avoid-the-3Cs_via_Meraki-Camera.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests
from config import settings

def message():
    req = 'https://webexapis.com/v1/messages?max=1&roomId=' + settings.room_id + '&mentionedPeople=' + settings.mentioned_id
    headers = {'Authorization': 'Bearer %s' % settings.token}
    response = requests.get(req, headers=headers)
    return response.json()['items'][0]['text']

if __name__ == '__main__':
    msg = message()
    print(msg)
