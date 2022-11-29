
from google.cloud import datastore

def create_entity(datastore_client):

    # The Cloud Datastore key for the new entity
    task1 = datastore.Entity(datastore_client.key("Topics"))
    task1.update(
    {
        "name": "Natural Language Processing",
        "list": ["Question Answering", "Sentiment Analysis"],
    }
    )
    datastore_client.put(task1)
    print("created Topics")


    task2 = datastore.Entity(datastore_client.key("Users"))
    task2.update(
    {
        "id": 123,
        "preferences": ["Question Answering", "Sentiment Analysis"],
        "timestamp": "2013-05-14T00:01:00.234Z",
    }
    )

    # Saves the entity
    datastore_client.put(task2)
    print("created Users")

    task3 = datastore.Entity(datastore_client.key("Results"))
    task3.update(
    {
        "title": "abc",
        "link": "abc",
        "tags": ["Question Answering", "Sentiment Analysis"],
        "timestamp": "2013-05-14T00:01:00.234Z",
    }
    )

    # Saves the entity
    datastore_client.put(task3)
    print("created Results")

    # Use this to upsert multiple entities
    # datastore_client.put_multi([task1, task2, task3])

if __name__ == "__main__":

    datastore_client = datastore.Client()
    create_entity(datastore_client)
    print("Created Kinds - Topics, Users, Results")