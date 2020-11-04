# coding: utf-8
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

from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps, Map
#from dynaconf import FlaskDynaconf
from detect import personcount
from snapshot import snapshot
from ms_fan import fan
import teams
import face
import requests
import json
import time
from collections import Counter
from config import settings

app = Flask(__name__, template_folder="templates")
#FlaskDynaconf(app)

GoogleMaps(
    app,
    key = settings.maps_key
)

@app.route("/")
def fullmap():
    img_url = snapshot()
    num_of_person = personcount()

    if num_of_person[0] < 10:
        icon_i = 'static/images/p1.png'
        discount_i = '<a href=http://127.0.0.1:5000/coupon>You can get a discount coupon now!!!</a>'
    else:
        icon_i = 'static/images/p2.png'
        discount_i = 'Come here now!'

    if num_of_person[1] < 10:
        icon_s = 'static/images/p1.png'
        discount_s = '<a href=http://127.0.0.1:5000/coupon>You can get a discount coupon now!!!</a>'
    else:
        icon_s = 'static/images/p2.png'
        discount_s = 'Come here now!'

    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:60%;"
            "width:90%;"
            "top:10;"
            "left:60;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=35.6295,
        lng=139.7942,
        markers=[
            {
                "icon": icon_i,
                "title": str(num_of_person[0]) + ' people here',
                "lat": 35.6293,
                "lng": 139.7942,
                "infobox": (
                    '\"<h1>Italian Restaurant <p> (' + str(num_of_person[0]) + ' people here!)</p></h1>\"'
                    '\"<h2>' + discount_i + '</h2>\"'
                    '\"<img src=\"' + img_url[0] + '\" width=\"50%\" height=\"50%\">\"'
                ),
            },
            {
                "icon": icon_s,
                "title": str(num_of_person[1]) + ' people here',
                "lat": 35.6294,
                "lng": 139.7942,
                "infobox": (
                    '\"<h1>Sushi Tokyo <p> (' + str(num_of_person[1]) + ' people here!)</p></h1>\"'
                    '\"<h2>' + discount_s + '</h2>\"'
                    '\"<img src=\"' + img_url[1] + '\" width=\"50%\" height=\"50%\">\"'
                ),
            },
        ],
        # maptype = "HYBRID",
        zoom="20"
    )
    return render_template(
        "map.html",
        fullmap=fullmap,
    )

@app.route('/coupon')
def coupon():
 return render_template("shotcoupon.html")

@app.route('/fan')
def shot():
 num_of_person = personcount()
 i=num_of_person[0]
 if i >= 10:
   fanstatus=1
   fan(True)
   time.sleep(20)
   return render_template("fan.html", count=i,fanstatus=fanstatus)
 else:
   fan(False)

   fanstatus=0
   return render_template("fan.html",count=i,fanstatus=fanstatus)

@app.route('/signage')
def signage():
    num_of_person = personcount()
    people = num_of_person[0]
    print('The number of people =', people)
    if people > 10:
        img_url = snapshot()
        ages_list = face.detectface(img_url[0])
        print('The age of people =', ages_list)
        age_c = Counter(ages_list)
        age_str = [str(int(i / 10)) for i in age_c]
        age_d = Counter(age_str)
        age = int(age_d.most_common()[0][0])
        msg = ''
        if age < 1:
            msg = teams.message()
    else:
        msg = ''
        age = 10

    return render_template("signage.html", msg=msg, people=people, age=age)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
