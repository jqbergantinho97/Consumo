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


class MainHandler(webapp2.RequestHandler):
    def post(self):
        km = int(self.request.get("km", 1))
        tiempo = int(self.request.get("tiempo", 1))
        consumo = int(self.request.get("consumo", 1))

        if km <= 0:
            km = 1
        if tiempo <= 0:
            tiempo = 1
        if consumo <= 0:
            consumo = 1

        velocidad_media = self.calcular_velocidad(km, tiempo)
        consumo_total = self.calcular_consumo(tiempo, consumo)

        self.response.write("Velocidad media: " + str(velocidad_media))
        self.response.write("\n Consumo total: " + str(consumo_total))

    def calcular_velocidad(self, km, tiempo):
        return km/tiempo

    def calcular_consumo(self, tiempo, consumo):
        return tiempo * consumo

app = webapp2.WSGIApplication([
    ('/vehiculo', MainHandler)
], debug=True)
