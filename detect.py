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

# return number of person detected by meraki camera

import requests
import json
from config import settings

def personcount():
 camlist = settings.camlist
 num_of_person=[]

 for sn in camlist:
  meraki_headers = {'X-Cisco-Meraki-API-Key': settings.apikey}
  meraki_live_url = 'https://api.meraki.com/api/v0/devices/'+sn+'/camera/analytics/live'
  meraki_live_response = requests.get(meraki_live_url, headers=meraki_headers)
  meraki_live_response_json=json.loads(meraki_live_response.text)
  num_of_person_detected=meraki_live_response_json['zones']['0']['person']
  num_of_person.append(num_of_person_detected)
 return num_of_person

if __name__ == "__main__":
    detect_num = personcount()
    print(detect_num)
