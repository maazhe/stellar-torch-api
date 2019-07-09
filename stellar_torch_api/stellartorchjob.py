#!/usr/bin/python3
# coding: utf8

import threading
import time
import config

def get_stellar_data():
    results = [
        [52.370216, 4.895168],
        [45.523064, -122.676483],
        [38.627003, -90.199402],
        [14.616199, 121.059319],
        [34.152588, 77.577049],
        [30.332184, -81.655647],
        [47.606209, -122.332069],
        [47.603230, -122.330280],
        [33.608768, -117.873360],
        ]
    # Background job here
    # Requests, scrap, crawl...
       
    config.LATLNGS = results
    

def run_job():
    
    # run first time
    get_stellar_data()
    
    # 6000 seconds / 100 minutes
    WAIT_TIME = 6000
    
    ticker = threading.Event()
    while not ticker.wait(WAIT_TIME):
        get_stellar_data()
