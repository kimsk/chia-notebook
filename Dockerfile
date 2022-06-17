FROM jupyter/scipy-notebook
LABEL Karlkim Suwanmongkol <karlkim@gmail.com>:

ENV JUPYTER_ENABLE_LAB=yes

USER root

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y jq

# install PowerShell
RUN apt-get update && \
    apt-get install -y wget apt-transport-https software-properties-common && \
    wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb" && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y powershell

# Install dotnet-sdk
RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb

RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    apt-get update && \
    apt-get install -y dotnet-sdk-6.0

# Install Dotnet-Interactive Tool
RUN dotnet tool install Microsoft.dotnet-interactive --tool-path /usr/bin

# Install Dotnet-Interactive Kernels
RUN dotnet interactive jupyter install

RUN python -m pip install --upgrade pip && \
    python -m pip install chia-blockchain && \
    python -m pip install chia-dev-tools --no-deps && \
    python -m pip install pytest && \
    python -m pip install jupyterlab_sos

ENV CHIA_ROOT="/.chia"
RUN mkdir /chia-utils
COPY code/*.* /chia-utils
RUN chmod +x  /chia-utils/start-chia-notebook.ps1
RUN mkdir /.chia && \
    mkdir /.chia/config

CMD ["/chia-utils/start-chia-notebook.ps1"]