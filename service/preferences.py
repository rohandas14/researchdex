import json
import requests
import traceback
from client.datastore_client import UserDS, TopicsDS
from client.pubsub_client import PubSub

PROJECT_ID = "researchdex"
TOPIC_QUEUE_NAME = "topic-queue"


def update_preferences(app, data):
    try:
        data = json.loads(data)
        users_ds_client = UserDS()
        pubsub_client = PubSub(PROJECT_ID, TOPIC_QUEUE_NAME)

        topic_ds_client = TopicsDS()
        all_topics_result = topic_ds_client.get_all()

        app.log.info("Fetching the topics for discovery.")

        topics_to_discover = []
        for result in all_topics_result:
            topics_to_discover += result['list']

        app.log.info("Fetch for topics completed for discovery.")

        try:
            user_record = users_ds_client.fetch(data['user_id'])
        except:
            app.log.error(traceback.print_exc())
            user_record = None
        if user_record is not None:
            user_prefs = set(user_record['preferences'])
            for pref in data['preferences']:
                if pref not in topics_to_discover:
                    misc_topics = topic_ds_client.fetch('misc')['list']
                    misc_topics.append(pref)
                    topic_ds_client.insert('misc', misc_topics)

                    topic_msg = {
                        'topic': pref
                    }
                    future = pubsub_client.publish(json.dumps(topic_msg).encode("utf-8"))
                user_prefs.add(pref)
            users_ds_client.insert(data['user_id'], list(user_prefs), user_record['search_timestamp'])
        else:
            user_prefs = set(data['preferences'])
            users_ds_client.insert(data['user_id'], list(user_prefs), 0)

        response_text = {
            "text": "Your preferences have been updated: " + ', '.join(user_prefs)
        }
    except:
        app.log.error(traceback.print_exc())
        response_text = {
            "text": "There was an error while trying to update your preferences. Please try again."
        }

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post(data['response_url'], json.dumps(response_text), headers)
    except Exception as err:
        app.log.error(traceback.print_exc())
