from goblet import Goblet, jsonify, goblet_entrypoint, Response
import json
import logging
from service.discovery import discovery
from service.result_aggregator import aggregate_result
from client.pubsub_client import PubSub

app = Goblet(function_name="researchdex")
app.log.setLevel(logging.INFO)  # configure goblet logger level
goblet_entrypoint(app)

PROJECT_ID = "researchdex"
SUB_TOPIC_NAME = "request-queue"    # Name of pubsub trigger topic
PREF_TOPIC_NAME = "preferences-queue"     # Name of preferences pubsub topic
#TODO: Update the schedule for run
DISCOVERY_RUN_SCHEDULE = "* 23 * * *" # Schedule of discovery run


@app.http()
def main(request):
    return jsonify(request.json)

# #TODO: update the route to schedule trigger after development and testing
# @app.route('/discovery')
# def run_discovery():
#     return discovery()

@app.topic(SUB_TOPIC_NAME)
def result_aggregator(data):
    aggregate_result(data)
    app.log.info("running result aggregator with data: {}".format(data))
    return 'result aggregator run completed!'

@app.route('/slash/prefs', methods=["POST"])
def update_preferences():
    r = app.current_request
    if "user_id" in r.form and "text" in r.form and "response_url" in r.form:
        preferences = r.form['text'].split(",")
        preferences = [preference.strip() for preference in preferences]
        pub_msg = {
            'user_id': r.form['user_id'],
            'preferences': preferences,
            'response_url': r.form['response_url']
        }
    pubsub_client = PubSub(PROJECT_ID, PREF_TOPIC_NAME)    
    future = pubsub_client.publish(json.dumps(pub_msg).encode("utf-8"))    
    success_msg = "Your request to update your preferences was received."
    return success_msg