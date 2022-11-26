from goblet import Goblet, jsonify, goblet_entrypoint, Response
import logging
from service.discovery import discovery
from service.result_aggregator import aggregate_result

app = Goblet(function_name="researchdex", local='test')
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

# @app.topic(SUB_TOPIC_NAME)
# def result_aggregator(data):
#     aggregate_result(data)
#     app.log.info("running result aggregator with data: {}".format(data))
#     return 'result aggregator run completed!'

@app.route('/slash/prefs', methods=["POST"])
def update_preferences():
    r = app.current_request
    if "text" in r.form and "response_url" in r.form:
        user_id = r.form['user_id']
        preferences = r.form['text'].split(",")
        preferences = [preference.strip() for preference in preferences]
        response_url = r.form['response_url']
    success_msg = "Your preferences were updated successfully."
    #return Response({"success": "ok"}, headers={"Content-Type": "application/json"}, status_code=200)
    return success_msg