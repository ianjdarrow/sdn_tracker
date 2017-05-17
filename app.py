#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_cors import CORS
from util.parse_csv import read_sdn_list, time_util
from util.tag_list import tags

app = Flask(__name__)
CORS(app)

l = read_sdn_list()
last_pull = time_util()

@app.route('/list')
def sdn_list():
	global l, last_pull
	delta = time_util() - last_pull
	if delta > 60 * 10:
		print("Refreshing list as of ", time_util())
		l = read_sdn_list()
		last_pull = time_util()
	else:
		print("Serving cached list from ", last_pull, "-", 10*60 - delta, " seconds remaining")
	return jsonify(l)

@app.route('/tags')
def get_tags():
	return jsonify(tags)

if __name__ == '__main__':
	print("Spinning up API server")
	app.run(host='0.0.0.0', debug=True)