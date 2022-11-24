#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.cloud import datastore

def create_entity():
    # Imports the Google Cloud client library

    # Instantiates a client
    datastore_client = datastore.Client()

    # The Cloud Datastore key for the new entity
    task1 = datastore.Entity(datastore_client.key("Task", 1))
    task1.update(
    {
        "category": "Sample1",
        "done": False,
        "priority": 4,
        "description": "Sample1",
    }
    )
    datastore_client.put(task1)


    task2 = datastore.Entity(datastore_client.key("Task", 2))
    task2.update(
    {
        "category": "Sample2",
        "done": False,
        "priority": 4,
        "description": "Sample2",
    }
    )

    # Saves the entity
    datastore_client.put(task2)

    # Use this to upsert multiple entities
    datastore_client.put_multi([task1, task2])