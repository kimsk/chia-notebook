FROM jupyter/scipy-notebook
LABEL Karlkim Suwanmongkol <karlkim@gmail.com>:

ENV JUPYTER_ENABLE_LAB=yes
ENV CHIA_ROOT="/home/jovyan/.chia/testnet"

USER root

RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y jq

RUN apt-get update \
    && apt-get install -y wget apt-transport-https software-properties-common \
    && wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb" \
    && dpkg -i packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y powershell

RUN python -m pip install --upgrade pip \
    && python -m pip install chia-dev-tools


RUN mkdir /chia-utils
COPY code/*.py /chia-utils