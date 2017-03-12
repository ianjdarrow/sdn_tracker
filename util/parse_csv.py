#!/usr/bin/env python3

import csv, requests
url = 'https://www.treasury.gov/ofac/downloads/sdn.csv'

def read_sdn_list():

# download FINCEN SDN list and turn it into a Python list
  with requests.Session() as s:
    download = s.get(url)
    decoded = download.content.decode('utf-8')
    cr = csv.reader(decoded.splitlines())
    sdn_list = list(cr)

# fix various formatting eccentricities 
    del(sdn_list[-1])
    for row in sdn_list:
      if row[1][0] == "'":
        row[1] = row[1][1:]

# split list into individuals and entities; take relevant data; alphabetize
    individuals = [
                  { 'id':       int(row[0].strip()), 
                    'name':     row[1].upper().strip(), 
                    'details':  (row[11].strip() if row[11].strip() != '-0-' else 'None')
                  } for row in sdn_list if row[2] == 'individual']

    entities = [
                  { 'id':       int(row[0]), 
                    'name':     row[1].upper()
                  } for row in sdn_list if row[2] != 'individual']

    individuals = sorted(individuals, key=lambda x:x['name'])
    entities = sorted(entities, key=lambda x:x['name'])

    return {'individuals': individuals, 'entities': entities}

if __name__ == '__main__':
  print(read_sdn_list())