#!/usr/bin/env python3

import csv, requests, time
from util.tag_list import tags
url = 'https://www.treasury.gov/ofac/downloads/sdn.csv'

def read_sdn_list():

# download FINCEN SDN list and turn it into a Python list
  print('Downloading current SDN list... ', end='')
  with requests.Session() as s:
    download = s.get(url)
    decoded = download.content.decode('utf-8')
    cr = csv.reader(decoded.splitlines())
    sdn_list = list(cr)
    print("complete.")

# fix various formatting eccentricities 
    del(sdn_list[-1])
    for row in sdn_list:
      if row[1][0] == "'":
        row[1] = row[1][1:]

# split list into individuals and entities; take relevant data; alphabetize
    print('Formatting data... ', end='')
    individuals = [
                  { 'id':            int(row[0].strip()), 
                    'firstName':     row[1].strip().split(', ')[1] if len(row[1].strip().split(', ')) > 1 else 'None',
                    'lastName':      row[1].upper().strip().split(', ')[0], 
                    'details':       (row[11].strip() if row[11].strip() != '-0-' else 'None')
                  } for row in sdn_list if row[2] == 'individual']

    entities = [
                  { 'id':       int(row[0]), 
                    'name':     row[1].upper().strip(),
                    'details':  row[3].strip().replace('[', '').replace(']', '').split(' ')
                  } for row in sdn_list if row[2] != 'individual']

    for entity in entities:
      for i, item in enumerate(entity['details']):
        try:
          entity['details'][i] = tags[item]
        except:
          pass

    print('complete.')

    individuals = sorted(individuals, key=lambda x:x['lastName'])
    entities = sorted(entities, key=lambda x:x['name'])

    return {'individuals': individuals, 'entities': entities}

def time_util():
  return int(time.mktime(time.gmtime()))

if __name__ == '__main__':
  print(read_sdn_list())