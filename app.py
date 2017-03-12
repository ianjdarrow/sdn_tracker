#!/usr/bin/env python3

from flask import Flask, jsonify, render_template
from flask_cors import CORS
from util.parse_csv import read_sdn_list

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return "<h1>Index page</h1>"

@app.route('/individuals')
def individuals():
  l = read_sdn_list()
  return jsonify(l['individuals'])

@app.route('/entities')
def entities():
  l = read_sdn_list()
  return jsonify(l['entities'])

if __name__ == '__main__':
  app.run(debug=True)