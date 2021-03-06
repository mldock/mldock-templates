FROM python:3.8-slim-buster

LABEL maintainer="SheldonGrant <sheldz.shakes.williams@gmail.com>"
SHELL ["/bin/bash", "-c"]

ARG container_platform="generic"

LABEL MLDOCK__IS_MLDOCK_CONTAINER="true"
LABEL MLDOCK__CONTAINER_PLATFORM="$container_platform"

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         ca-certificates \
         g++ \
         git \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y python3-dev build-essential && \
    apt-get install -y wget && \
    rm -rf /var/lib/apt/lists/*

# PYTHONUNBUFFERED keeps Python from buffering the standard
# output stream, which means that logs can be delivered to the user quickly. 
# PYTHONDONTWRITEBYTECODE keeps Python from writing the .pyc files which are unnecessary in this case. 

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

ARG requirements_file_path
ARG module_path
ARG target_dir_name

WORKDIR /opt/program/

# Here we get all python packages.
RUN pip install fastapi uvicorn[standard] mldock

COPY ${module_path}/assets.py /opt/program/${target_dir_name}/assets.py
COPY ${module_path}/container/lifecycle.py /opt/program/${target_dir_name}/container/lifecycle.py
COPY ${module_path}/container/executor.sh /opt/program/${target_dir_name}/container/executor.sh
COPY ${module_path}/container/prediction /opt/program/${target_dir_name}/container/prediction
COPY ${module_path}/container/training /opt/program/${target_dir_name}/container/training

ENTRYPOINT ["src/container/executor.sh"]
