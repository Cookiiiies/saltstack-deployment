#!/usr/bin/env bash

if [ ! -x "$(command -v gcloud)" ]; then
     $(
        cd ${HOME} && \
        wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && \
        unzip google-cloud-sdk.zip && \
        rm google-cloud-sdk.zip && \
        google-cloud-sdk/install.sh --path-update=true
     )

fi


if [ ! -x "$(command -v kubectl)" ]; then
     $(
        mkdir -p ${HOME}/kubectl && \
        cd ${HOME}/kubectl && \
        curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl && \
        chmod +x ${HOME}/kubectl/kubectl &&
        source ${HOME}/.bashrc
     )
fi