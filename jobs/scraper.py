import googlemaps
import os


def scrape():
  module_dir = os.path.dirname(__file__)  # get current directory
  file_path = os.path.join(module_dir, 'data/companies.txt')
  location_path = os.path.join(module_dir, 'data/company_location.txt')
  output_path = os.path.join(module_dir, 'data/company_data_accurate.txt')
  not_found_path=os.path.join(module_dir, 'data/not_found.txt')
  not_found_location_path=os.path.join(module_dir, 'data/not_found_location.txt')
  company_data_file = open(output_path, 'a')
  not_found_file = open(not_found_path, 'a')
  not_found_location_file = open(not_found_location_path, 'a')
  gmaps = googlemaps.Client(key='AIzaSyDLRWu7jDRZF91arvnnUKsqboJhtRjgFwg')
  companies_list = [line.rstrip() for line in open(file_path, "r")]
  location_list = [line.rstrip() for line in open(location_path, "r")]
  for index, company in enumerate(companies_list):
    place = gmaps.places(company + location_list[index])
    if not place['results']:
      # If too specific and returns no results, just search name
      place = gmaps.places(company)
    if place['results']:
      print("SCRAPING: {company}".format(company=company))
      location = place['results'][0]['geometry']['location']
      address = place['results'][0]['formatted_address']
      lat = location['lat']
      long = location['lng']
      company_data_file.write("{company}|{address}|{lat}|{long}\n".format(
        company=company,
        address=address,
        lat=lat,
        long=long)
      )
    else:
      not_found_file.write("{company}\n".format(company=company))
      not_found_location_file.write("{location}\n".format(location=location_list[index]))
      print("DIDNT FIND: {company}".format(company=company))
  company_data_file.close()
  not_found_file.close()
  not_found_location_file.close()

def load_scraped_data():
  module_dir = os.path.dirname(__file__)  # get current directory
  company_data = os.path.join(module_dir, 'data/company_data_accurate.txt')
  company_info = [line.rstrip().split('|') for line in open(company_data, "r")]
  return company_info

load_scraped_data()
