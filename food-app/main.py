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
import logging

template_dir=os.path.join(os.path.dirname(__file__))

jinja_environment = jinja2.Environment(
loader = jinja2.FileSystemLoader(template_dir)
)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

    def post(self):


class SecondHandler(webapp2.RequestHandler):
#This is ganna give the flavors and places to eat"""
    def get(self):
        template = jinja_environment.get_template('templates/secondpd.html')
        username = self.request.get("username")
        usercolor = self.request.get("usercolor")
        user_info = {"username" : username, "usercolor":usercolor}
        self.response.write(template.render(user_info))

    def post(self):
        template = jinja_environment.get_template('templates/secondpd.html')
        name = self.request.get("username")
        color = self.request.get("usercolor")
        flavors_5 = self.request.get("flavors_5")
        flavors_4 = self.request.get("flavors_4")
        flavors_3 = self.request.get("flavors_3")
        flavors_2 = self.request.get("flavors_2")
        flavors = self.request.get("flavors")
        places = self.request.get("places")
        portions = self.request.get("portions")

        flavors_list = []
        if flavors !="":
            flavors_list.append(flavors)
        if flavors_2 !="":
            flavors_list.append(flavors_2)
        if flavors_3 !="":
            flavors_list.append(flavors_3)
        if flavors_4 !="":
            flavors_list.append(flavors_4)
        if flavors_5 !="":
            flavors_list.append(flavors_5)

        #for flavor in flavors_list:
        if len(flavors_list) == 0:
            flavors_string = "you didnt choose any flavors<br>"
        elif len(flavors_list) == 1:
            flavors_string = "You have chosen {0}.<br>".format(flavors_list[0])
        else:
            base_flavor_string = "You have chosen the following flavors: "
            flavors_string = ""
            for flavors in flavors_list:
                flavors_string += flavors + ", "
            flavors_string = base_flavor_string + flavors_string[0:-2] + ".<br>"
        #self.response.write("Hello " + name + " you have chosen " + flavors + " and based on your location we have found this place near you, " + places + ", and the amount of your portion is " + portions + ".")
        logging.info(flavors_list)
        self.response.write(template.render())
        self.response.write(flavors_string)
        self.response.write("Your name is: <strong> " + name + "</strong> Your favorite color is: <strong> " + color + "</strong> <br>")

        self.response.write("Hello " + name + ", based on your choice in flavors we have found a place that matches what you want, " + places + ", and the amount of your portion is " + portions + ".")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/second', SecondHandler)
], debug=True)
