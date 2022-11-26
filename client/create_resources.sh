#!/bin/sh

#Create required pubsub resources
gcloud deployment-manager deployments create pub-sub-deployment --config ./templates/pubsub.yaml