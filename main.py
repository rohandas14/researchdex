from goblet import Goblet, jsonify, goblet_entrypoint
import logging
from service.discovery import discovery
from service.result_aggregator import aggregate_result

app = Goblet(function_name="researchdex")
app.log.setLevel(logging.INFO)  # configure goblet logger level
goblet_entrypoint(app)


SUB_TOPIC_NAME = 'request-queue'    # Name of pubsub trigger topic
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

