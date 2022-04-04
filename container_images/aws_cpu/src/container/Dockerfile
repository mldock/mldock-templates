FROM mldockcloud/0.9.0-generic-py38-cpu:latest

ARG container_platform="aws"

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         curl \
         unzip \
    && rm -rf /var/lib/apt/lists/*

# Installs google cloud sdk, this is mostly for using gsutil to export model.
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

# Here we get all python packages.
RUN pip install mldock[aws]
