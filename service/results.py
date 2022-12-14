import json
import random
import requests
import time
import traceback
from client.datastore_client import UserDS, ResultsDS

def aggregate_results(app, data):
    try:
        user_client = UserDS()
        custom_query = True
        data = json.loads(data)
        try:
            user_record = user_client.fetch(data['user_id'])
        except:
            app.log.error(traceback.print_exc())
            user_record = None

        preferences = data['preferences']
        if len(preferences) == 0:
            preferences = user_record['preferences']
            custom_query = False
        if len(preferences) == 1 and preferences[0] == '-f':
            preferences = user_record['preferences']
            custom_query = True
        last_searched = user_record['search_timestamp']
        results = fetch_results(app, preferences, last_searched, custom_query)
        if len(results) > 0:
            response_text = compose_results(results)
        else:
            response_text = {
                "text": "No new results found for your area(s) of interest."
            }
        
        if user_record is not None and not custom_query:
            user_client.insert(data['user_id'], user_record['preferences'], int(time.time()))
    except:
        app.log.error(traceback.print_exc())
        response_text = {
            "text": "There was an error while trying to fetch the latest papers. Please try again."
        }

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(data['response_url'], json.dumps(response_text), headers)    
    except:
        app.log.error(traceback.print_exc())

def fetch_results(app, preferences, last_searched, custom_query):
    results_client = ResultsDS()
    aggregate_results = []
    for preference in preferences:
        itr = 0
        try:
            topic_results = results_client.fetch(preference)['result_list']
        except:
            app.log.error("No such entry in Results DB with: " + preference)
            continue
        for result in  topic_results:
            if custom_query:
                candidate = result
                candidate['topic'] = preference
                aggregate_results.append(candidate)
                itr += 1
            else:
                if result['timestamp'] > last_searched:
                    candidate = result
                    candidate['topic'] = preference
                    aggregate_results.append(candidate)
                    itr += 1
            if itr == 20:
                continue

    return aggregate_results

def compose_results(results):
    response_text = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here are some relevant papers in your area(s) of interest."
                }
            },
            {
                "type": "divider"
            }
        ]
    }

    divider_block = {
			"type": "divider"
		}

    sampled_results = random.sample(results, 10)

    for result in sampled_results:
        text = '*<{link}|{title}>*\n\n*TOPIC:* {topic}\n\n*SOURCE:* {source}'.format(
            link=result['link'], 
            title=result['title'], 
            topic=result['topic'], 
            source=result['source'].capitalize()
        )
        result_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": text
            }
		}
        response_text["blocks"].append(result_block)
        response_text["blocks"].append(divider_block)

    return response_text