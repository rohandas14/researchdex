#!/bin/sh

cd "${0%/*}"

#Create required pubsub resources
gcloud deployment-manager deployments create pub-sub-deployment --config ./pubsub/pubsub.yaml