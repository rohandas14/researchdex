from goblet import Goblet

result_aggregator = Goblet()

SUB_TOPIC_NAME = 'slack_request'

# #TODO: Uncomment when topic is created
# @result_aggregator.topic(SUB_TOPIC_NAME)
# def result_aggregator(data):
#     result_aggregator.log.info("running result aggregator with data: {}".format(data))
#     return 'result aggregator run completed!'