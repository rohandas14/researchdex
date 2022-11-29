from pydoc_data.topics import topics
from google.cloud import datastore

class TopicsDS:
    def __init__(self):
        self.client = datastore.Client()
        self.kind = "Topics"
        
    def insert(self, key, name, list):
        task = datastore.Entity(self.client.key(self.kind, key))
        task.update(
        {
            "name": name,
            "list": list,
        }
        )

    def fetch(self, key):
        task = self.client.get(key)

        return task

    def delete(self, key):
        self.client.delete(key)

class UserDS:
    def __init__(self):
        self.client = datastore.Client()
        self.kind = "Users"
        
    def insert(self, key, id, preference_list, timestamp):
        task = datastore.Entity(self.client.key(self.kind, key))
        task.update(
        {
            "id": id,
            "preferences": preference_list,
            "timestamp": timestamp,
        }
        )

    def fetch(self, key):
        task = self.client.get(key)

        return task

    def delete(self, key):
        self.client.delete(key)

class ResultsDS:
    def __init__(self):
        self.client = datastore.Client()
        self.kind = "Results"
        
    def insert(self, key, title, link, tags_list, timestamp):
        task = datastore.Entity(self.client.key(self.kind, key))
        task.update(
        {
            "title": title,
            "link": link,
            "tags": tags_list,
            "timestamp": timestamp,
        }
        )

    def fetch(self, key):
        task = self.client.get(key)

        return task

    def delete(self, key):
        self.client.delete(key)

if __name__ == "__main__":

    datastore_client = datastore.Client()
    topic = TopicsDS()
    list = ["AB", "CD"]
    topic.insert("AI", list)
