#!/usr/bin/python3
'''
    creste Flask app; app_views
'''
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route("/status")
def status():
    '''
        return JSON of OK status
    '''
    return jsonify({'status': 'OK'})


@app_views.route("/stats")
def storage_counts():
    '''
        return counts of all classes in storage
    '''
    cls_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(cls_counts)

