#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import urllib2
import urllib
import jinja2
import os

template_dir=os.path.join(os.path.dirname(__file__))

jinja_environment = jinja2.Environment(
loader = jinja2.FileSystemLoader(template_dir)
)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

class SecondHandler(webapp2.RequestHandler):
#This is ganna give the flavors and places to eat"""
    def get(self):
        template = jinja_environment.get_template('templates/secondpd.html')
        username = self.request.get("username")
        userlocation = self.request.get("userlocation")
        user_info = {"username" : username, "userlocation":userlocation}
        self.response.write(template.render(user_info))

    def post(self):
        template = jinja_environment.get_template('templates/secondpd.html')
        name = self.request.get("username")
        location = self.request.get("userlocation")
        flavors = self.request.get("flavors")
        places = self.request.get("places")
        portions = self.request.get("portions")
        #self.response.write("Hello " + name + " you have chosen " + flavors + " and based on your location we have found this place near you, " + places + ", and the amount of your portion is " + portions + ".")
        self.response.write(template.render())

        self.response.write("Your name is: <strong> " + name + "</strong> Your location is: <strong> " + location + "</strong> <br>")
        self.response.write("Hello " + name + ", you have chosen " + flavors + " as the flavor you are craving and based on your location we have found a place that matches what you want, " + places + ", and the amount of your portion is " + portions + ".")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/second', SecondHandler)
], debug=True)
