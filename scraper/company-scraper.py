import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDyAYrCZ19Y_9nfTmCTirbYlVk7-Xqysyg')
# # Geocoding an address
# geocode_result = gmaps.places('general assembly company startup')
# print(geocode_result)
companies_list = [line.rstrip() for line in open("companies.txt", "r")]
company_results = []

for company in companies_list[0:2]:
  place = gmaps.places(company + 'comapny startup')
  if not place['results']:
    place = gmaps.places(company)
  location = place['results'][0]['geometry']['location']
  co = {
    'name': company,
    'address': place['results'][0]['formatted_address'],
    'lat': location['lat'],
    'long': location['lng']
  }
  company_results.append(co)

print(company_results)

