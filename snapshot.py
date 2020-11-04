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

#return snapshot url
import requests
import json
import time
from config import settings

def snapshot():
 camlist = settings.camlist
 snap_url=[]

 for sn in camlist:
  meraki_snapshot_url='https://api.meraki.com/api/v0/networks/' + settings.network_id + '/cameras/' + sn + '/snapshot'

  meraki_headers = {'X-Cisco-Meraki-API-Key': settings.apikey}

  meraki_snapshot_response = requests.post(meraki_snapshot_url, headers=meraki_headers)
  meraki_snapshot_response_json=json.loads(meraki_snapshot_response.text)

  snapshot_url=meraki_snapshot_response_json['url']
  snap_url.append(snapshot_url)
 return snap_url

if __name__ == "__main__":
    snap = snapshot()
    print(snap)
