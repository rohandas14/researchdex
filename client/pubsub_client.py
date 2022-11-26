from google.cloud import pubsub_v1

class PubSub:
    def __init__(self, project_id, topic_id):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_id)
        
    def publish(self, data_string):
        self.publisher.publish(self.topic_path, data_string)