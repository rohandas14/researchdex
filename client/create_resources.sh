#!/bin/sh

#Create required pubsub resources
gcloud deployment-manager deployments create pub-sub-deployment --config client/templates/pubsub.yaml