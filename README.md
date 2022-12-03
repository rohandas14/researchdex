# Reearch Dex

## Quickstart

1. Create and activate a virtual environment in python3.7
```commandline
$ python3 --version
Python 3.7.3
$ python3 -m venv venv37
$ . venv37/bin/activate
```
2. Install requirement:
```commandline
python3 -m pip install -r requirements.txt
```
3.1. Install [gcloud cli](https://cloud.google.com/sdk/docs/install) for authentication.

3.2. [NOT Required, already set up]
```commandline
gcloud services enable cloudfunctions.googleapis.com
gcloud services enable apigateway.googleapis.com
gcloud services enable servicemanagement.googleapis.com
gcloud services enable cloudscheduler.googleapis.com
gcloud services enable pubsub.googleapis.com        
gcloud services enable logging.googleapis.com
gcloud services enable deploymentmanager.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```
4. Run google cloud authentication and set configurations:
project_id: researchdex, 
region: us-central1
```commandline
gcloud auth application-default login
```
5. To test endpoints locally run `goblet local`
To deploy cloudfunctions and other gcp resources defined in `main.py` run `goblet deploy -l us-central1`

To check out goblet documentation go to [docs](https://goblet.github.io/goblet/docs/build/html/index.html)
