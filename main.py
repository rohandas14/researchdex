import logging
import json
from goblet import Goblet, jsonify, goblet_entrypoint
from endpoint.preferences import queue_update_job
from endpoint.results import queue_search_job
from service.discovery import discovery
from service.discovery import discovery_per_topic
from service.preferences import update_preferences
from service.results import aggregate_results

app = Goblet(function_name="researchdex")
app.log.setLevel(logging.INFO)  # configure goblet logger level
goblet_entrypoint(app)

PROJECT_ID = "researchdex"
SEARCH_TOPIC_NAME = "search-queue"
PREFERENCES_TOPIC_NAME = "preferences-queue"
TOPIC_QUEUE_NAME = "topic-queue"


@app.http()
def main(request):
    return jsonify(request.json)


# TODO: update the route to schedule trigger after development and testing
@app.route('/discovery', deadline=90)
def run_discovery_job():
    discovery(app)
    return "Discovery run completed!"


@app.topic(TOPIC_QUEUE_NAME)
def run_discovery_per_topic(data):
    data = json.loads(data)
    topic = data['topic']
    discovery_per_topic(topic, app)


@app.route('/slash/search', methods=["POST"])
def search_endpoint():
    success_msg = queue_search_job(app.current_request)
    return success_msg


@app.route('/slash/prefs', methods=["POST"])
def update_preferences_endpoint():
    success_msg = queue_update_job(app.current_request)
    return success_msg


@app.topic(SEARCH_TOPIC_NAME)
def result_aggregator_worker(data):
    aggregate_results(app, data)


@app.topic(PREFERENCES_TOPIC_NAME)
def update_preferences_worker(data):
    update_preferences(app, data)
