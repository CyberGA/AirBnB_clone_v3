#!/usr/bin/python3
"""index file for json"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """method to get the status of API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def use_count():
    """use the newly added count() method from storage"""
    count = storage.count()
    return jsonify({"count": count})
