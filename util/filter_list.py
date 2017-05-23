#!/usr/bin/env python3

from fuzzywuzzy import fuzz, process
from util.parse_csv import read_sdn_list
import time

LEV_CUTOFF = 78

def filter_list(items, search):
	start_time = time.time()
	individuals = []
	for item in items['individuals']:
		if fuzz.partial_ratio(search, item['lastName']) > LEV_CUTOFF:
			individuals.append(item)

	entities = []
	for item in items['entities']:
		if fuzz.partial_ratio(search, item['name']) > LEV_CUTOFF:
			entities.append(item)

	print("Search for %s completed in %ss" % (search, time.time() - start_time))
	return {'individuals': individuals, 'entities': entities}