import json
import requests
import traceback
from client.datastore_client import UserDS

def update_preferences(app, data):
    try:
        ds_client = UserDS()
        data = json.loads(data)
        try:
            user_record = ds_client.fetch(data['user_id'])
        except:
            app.log.error(traceback.print_exc())
            user_record = None
        if user_record is not None:
            user_prefs = set(user_record['preferences'])
            for pref in data['preferences']:
                user_prefs.add(pref)
            ds_client.insert(data['user_id'], list(user_prefs), user_record['search_timestamp'])
        else:
            user_prefs = set(data['preferences'])
            ds_client.insert(data['user_id'], list(user_prefs), 0)
            
        response_text = {
            "text": "Your preferences have been updated."
        }
    except:
        app.log.error(traceback.print_exc())
        response_text = {
            "text": "There was an error while trying to update your preferences. Please try again."
        }
        
    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(data['response_url'], json.dumps(response_text), headers)    
    except:
        app.log.error(traceback.print_exc())