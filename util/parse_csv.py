#!/usr/bin/env python3

import csv, sys, os
list_loc = os.path.abspath('./util/sdn.csv')

def read_sdn_list():
  with open(list_loc, 'rt') as list:
    list_reader = csv.reader(list)
    sdn_list = []
    for row in list_reader:
      sdn_list.append(row)
    del(sdn_list[-1])
    for row in sdn_list:
      if row[1][0] == "'":
        row[1] = row[1][1:]

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