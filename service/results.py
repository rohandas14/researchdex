import json
import requests
import time
from client.datastore_client import UserDS, ResultsDS

def aggregate_results(app, data):
    try:
        user_client = UserDS()
        data = json.loads(data)
        try:
            user_record = user_client.fetch(data['user_id'])
        except Exception as err:
            app.log.error(err)
            user_record = None

        preferences = data['preferences']
        if len(preferences) < 0:
            preferences = user_record['preferences']
        
        results = fetch_results(preferences)
        response_text = compose_results(results)
        
        if user_record is not None:
            user_client.insert(data['user_id'], data['preferences'], int(time.time()))
    except Exception as err:
        app.log.error(err)
        response_text = {
            "text": "There was an error while trying to update your preferences. Please try again."
        }

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(data['response_url'], json.dumps(response_text), headers)    
    except Exception as err:
        app.log.error(err)

def fetch_results(preferences):
    pass

def compose_results(results):
    pass