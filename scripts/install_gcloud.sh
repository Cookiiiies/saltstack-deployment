#!/usr/bin/env bash

if [ ! -d ${HOME}/google-cloud-sdk ]; then
     wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
     google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --additional-components kubectl
     gcloud components install kubectl
fi