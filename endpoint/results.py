import json
from client.pubsub_client import PubSub

PROJECT_ID = "researchdex"
SEARCH_TOPIC_NAME = "search-queue"

def queue_search_job(request):
    if "user_id" in request.form and "text" in request.form and "response_url" in request.form:
        preferences = request.form['text'].split(",")
        preferences = [preference.strip() for preference in preferences]
        pub_msg = {
            'user_id': request.form['user_id'],
            'preferences': preferences,
            'response_url': request.form['response_url']
        }
    pubsub_client = PubSub(PROJECT_ID, SEARCH_TOPIC_NAME)    
    future = pubsub_client.publish(json.dumps(pub_msg).encode("utf-8"))    
    success_msg = "Thank you for your request for the latest papers. We are working on it."
    return success_msg