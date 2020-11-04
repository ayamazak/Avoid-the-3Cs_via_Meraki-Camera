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
import json
from snapshot import snapshot
from config import settings
from collections import Counter
import time

def detectface(url):
    face_api_url = 'https://cisco.cognitiveservices.azure.com/face/v1.0/detect'
    headers = {'Ocp-Apim-Subscription-Key': settings.subscription_key}
    params = {
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age',
        #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    time.sleep(5)
    response = requests.post(face_api_url, params=params, headers=headers, json={"url": url})
    list = []
    for i in response.json():
        list.append(i['faceAttributes']['age'])
    return list

if __name__ == '__main__':
    img_url = snapshot()
    ages_list = detectface(img_url[0])
    print('The Age of people = ', ages_list)
