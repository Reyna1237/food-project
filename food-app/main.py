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
    """This is ganna give the flavors and places to eat"""
    def __init__(self, name, flavors, places, portions):
        self.name = name
        self.flavors = flavors
        self.places = places
        self.portions = portions
    def post(self):
        print(self.name)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/second', SecondHandler)
], debug=True)
