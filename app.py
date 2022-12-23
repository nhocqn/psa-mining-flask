import pymongo
from json2html import *

from flask import Flask, request, jsonify
from urllib.parse import urlparse
import requests
import json
import re
import os
import threading, queue, time

db = pymongo.MongoClient(
    "mongodb+srv://doadmin:476Aa13F80pyQV5s@adlib-024293e9.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=adlib")[
    "admin"]

q = queue.Queue()
task_status = []

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    posts = db.posts.find().sort("_id", -1)

    content = ""

    for post in posts:
        content +="<p>" + json2html.convert(json=post) + "</p>"
        content +='<p><img src="' + str(post['image_url']) + '" width="500px" ></p>'
    return content


# 'Out for Delivery', 'Take Off', 'Order Created', 'Arrived Destination', 'delivered', 'Order Shipped', 'Processing', 'Delivered'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
