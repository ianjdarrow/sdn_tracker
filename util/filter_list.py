#!/usr/bin/env python3

from fuzzywuzzy import fuzz, process
from util.parse_csv import read_sdn_list
import time

LEV_CUTOFF = 75

def filter_list(items, search):
	start_time = time.time()
	individuals = []
	for item in items['individuals']:
		score = fuzz.token_set_ratio(search, item['lastName'])
		if score > LEV_CUTOFF:
			item['score'] = score
			individuals.append(item)

	individuals = sorted(individuals, key=lambda i: i['score'], reverse=True)
	# for item in individuals:
	# 	print(item[0]['lastName'] + '\t' + str(item[1]))

	entities = []
	for item in items['entities']:
		score = fuzz.token_set_ratio(search, item['name'])
		if score > LEV_CUTOFF:
			item['score'] = score
			entities.append(item)

	entities = sorted(entities, key=lambda i: i['score'], reverse=True)

	print("Search for %s completed in %ss" % (search, '{0:.03f}'.format(time.time() - start_time)))
	return {'individuals': individuals, 'entities': entities}

# names = read_sdn_list()
# filter_list(names, 'BROTHERHOOD')