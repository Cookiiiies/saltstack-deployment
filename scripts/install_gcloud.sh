#!/usr/bin/env bash

if [ ! -d ${HOME}/google-cloud-sdk ]; then
     wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
     google-cloud-sdk/install.sh --usage-reporting=true --path-update=true
fi

if [ ! -d ${HOME}/kubectl ]; then
     $( mkdir -p ${HOME}/kubectl && cd ${HOME}/kubectl && curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl )
     chmod +x ${HOME}/kubectl/kubectl
fi