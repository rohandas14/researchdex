import logging
import time
import json

from client.resp.apis.arxiv_api import Arxiv
from client.datastore_client import TopicsDS, ResultsDS
from client.pubsub_client import PubSub

PROJECT_ID = "researchdex"
TOPIC_QUEUE_NAME = "topic-queue"

RESULT_TITLE_KEY = 'title'
RESULT_LINK_KEY = 'link'
RESULT_SOURCE_KEY = 'source'
RESULT_TIMESTAMP_KEY = 'timestamp'

SOURCE_VAL_ARXIV = 'arxiv'

def discovery(app):
    try:
        logging.info("running discovery service")

        topic_ds_client = TopicsDS()
        # Get the topics to fetch the results for
        all_topics_result = topic_ds_client.get_all()

        app.log.info("Fetching the topics for discovery.")

        topics_to_discover = []
        for result in all_topics_result:
            topics_to_discover+=result['list']

        app.log.info("Fetch for topics completed for discovery.")

        pubsub_client = PubSub(PROJECT_ID, TOPIC_QUEUE_NAME)
        for topic in topics_to_discover:
            topic_msg = {
                'topic': topic
            }
            future = pubsub_client.publish(json.dumps(topic_msg).encode("utf-8"))
            app.log.info(f"Topic: {topic} queued in for discovery!")
        app.log.info("all topics queued in for discovery.")
        return "all topics queued in for discovery."
    except Exception as err:
        app.log.error(err)
        raise f"Error running discovery service: {err}"

def discovery_per_topic(topic, app):
    try:
        arxiv_client = Arxiv()
        result_ds_client = ResultsDS()
        # get the results from arxiv
        arxiv_result = arxiv_client.arxiv(topic, max_pages=1)
        # arxiv_result = arxiv_result.head(2) #TODO
        topic_results = []
        for index, row in arxiv_result.iterrows():
            result = {
                RESULT_TITLE_KEY: row['title'],
                RESULT_LINK_KEY: row['link'],
                RESULT_SOURCE_KEY: SOURCE_VAL_ARXIV,
                RESULT_TIMESTAMP_KEY: int(time.time()),
            }
            topic_results.append(result)

        old_result = result_ds_client.fetch(topic)

        if not old_result == None:
            result_ds_client.insert(
                topic,
                old_result['result_list'] + topic_results
            )
        else:
            result_ds_client.insert(
                topic,
                topic_results
            )
        app.log.info(f"discovery service completed running for topic: {topic}")

    except Exception as err:
        app.log.error(err)
        raise f"Error running discovery service for topic {topic} : {err}"