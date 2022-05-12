FROM jupyter/scipy-notebook

USER root

RUN apt-get update && apt-get install -y curl

RUN python -m pip install --upgrade pip \
    && python -m pip install chia-dev-tools

ENV CHIA_ROOT="/home/jovyan/.chia/testnet"