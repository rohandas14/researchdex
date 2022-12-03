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
        self.client.put(task)

    def fetch(self, key):
        task = self.client.get(self.client.key(self.kind, key))
        return task

    def delete(self, key):
        self.client.delete(self.client.key(self.kind, key))

class UserDS:
    def __init__(self):
        self.client = datastore.Client()
        self.kind = "Users"
        
    def insert(self, key, preference_list, timestamp):
        task = datastore.Entity(self.client.key(self.kind, key))
        task.update(
            {
                "preferences": preference_list,
                "search_timestamp": timestamp,
            }
        )
        self.client.put(task)

    def fetch(self, key):
        task = self.client.get(self.client.key(self.kind, key))
        return task

    def delete(self, key):
        self.client.delete(self.client.key(self.kind, key))

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
        self.client.put(task)

    def fetch(self, key):
        task = self.client.get(self.client.key(self.kind, key))
        return task

    def delete(self, key):
        self.client.delete(self.client.key(self.kind, key))
