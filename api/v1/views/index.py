#!/usr/bin/python3
"""index file for json"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('app_views')
def status():
    """method to get the status of API"""
    return jsonify({"status": "OK"})
