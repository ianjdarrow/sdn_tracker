#!/usr/bin/env python3

from sanic import Sanic, response
from sanic_cors import CORS, cross_origin
from util.parse_csv import read_sdn_list, time_util
from util.tag_list import tags
from util.filter_list import filter_list
from threading import Timer

app = Sanic(__name__)
CORS(app)

l = []

# 
def update_list():
	global l
	l = read_sdn_list()
	updater = Timer(10*60, update_list)
	updater.daemon = True
	updater.start()

@app.listener('before_server_start')
async def load_files(app, loop):
	update_list()

@app.route('/list/<search>')
async def sdn_list(request, search):
	result = filter_list(l, search.upper())
	return response.json(result)

@app.route('/tags')
async def get_tags():
	return response.json(tags)

if __name__ == '__main__':
	print("Spinning up API server")
	app.run(host='0.0.0.0', port=5000)