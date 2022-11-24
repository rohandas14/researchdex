from goblet import Goblet, jsonify
import logging
from service.discovery import discovery
from service.result_aggregator import result_aggregator

app = Goblet(function_name="researchdex")
app.log.setLevel(logging.INFO)  # configure goblet logger level

app.combine(discovery)
app.combine(result_aggregator)

@app.http()
def main(request):
    return jsonify(request.json)

