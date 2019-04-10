#!/usr/bin/env python
# -*- coding: utf-8 -*

from googleplaces import GooglePlaces, types
from geopy.geocoders import googlev3
from decimal import *
import os
import csv

class ExportRestaurant():

    query_result = None

    def __init__(self, apikey, place_name='Chetumal, Quintana Roo, Mexico', radius=20000):
        self.apikey = apikey
        self.place_name = place_name
        self.radius = radius

    def __str__(self):
        return 'ExportRestaurant Object'

    def getRestaurants(self):
        geolocator = googlev3.GoogleV3(self.apikey)
        # We obtain the coordinates of the given place
        location = geolocator.geocode(self.place_name)
        lat, lon = location.latitude, location.longitude

        google_places = GooglePlaces(self.apikey)
        # Api call and response and saved in query_result att
        self.query_result = google_places.nearby_search(
            location=self.place_name, lat_lng={'lat' : lat, 'lng': lon}
            ,radius=self.radius, types=[types.TYPE_RESTAURANT])
    
    def to_csv(self):
        if self.query_result:
            google_places = GooglePlaces(self.apikey)
            query = self.query_result
            csv_file = open('Restaurants.csv', encoding='utf-8', mode="w")
            writer = csv.writer(csv_file)

            #Writing the headers of the csv file
            header = ['name','lat','lng','number','inumber','website','map']
            writer.writerow(header)

            firsttime = True
            #list for writing every restaurant like a row in the csv file
            values = []
            #iteration per page
            while query.has_next_page_token or firsttime:
                
                if not(firsttime):
                    query = google_places.nearby_search(pagetoken=query.next_page_token)
                #iteration per place
                for place in query.places:
                    values.append(place.name)
                    values.append(float(place.geo_location['lat']))
                    values.append(float(place.geo_location['lng']))
                    #Api call for the details of every restaurant
                    #In that way we can obtain the phone number, website and maps
                    #of every single place of query_result
                    place.get_details()
                    values.append(place.local_phone_number)
                    values.append(place.international_phone_number)
                    values.append(place.website)
                    values.append(place.url)
                    
                    #writing new restaurant
                    writer.writerow(values)
                    values = []

                firsttime = False               
                
            st = os.stat('Restaurants.csv')
            os.chmod('Restaurants.csv', st.st_mode)
            csv_file.close()
        
        else:
            raise ValueError('query_result empty or None. Call the getRestaurants method before export')




        
        