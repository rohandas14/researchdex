from google.cloud import datastore

class TopicsDS:
    def __init__(self):
        self.client = datastore.Client()
        self.kind = "Topics"
        
    def insert(self, key, list):
        task = datastore.Entity(self.client.key(self.kind, key))
        task.update(
            {
                "list": list,
            }
        )
        self.client.put(task)

    def fetch(self, key):
        task = self.client.get(self.client.key(self.kind, key))
        return task

    def delete(self, key):
        self.client.delete(self.client.key(self.kind, key))

    def get_all(self):
        return self.client.query(kind=self.kind).fetch()

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
        
    def insert(self, key, result_list):
        task = datastore.Entity(self.client.key(self.kind, key))
        task.update(
            {
                "result_list": result_list,
            }
        )
        self.client.put(task)

    def fetch(self, key):
        task = self.client.get(self.client.key(self.kind, key))
        return task

    def delete(self, key):
        self.client.delete(self.client.key(self.kind, key))
