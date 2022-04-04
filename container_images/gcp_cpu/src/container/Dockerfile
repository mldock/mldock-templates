FROM mldockcloud/0.9.0-generic-py38-cpu:latest

ARG container_platform="gcp"
ARG requirements_file_path
ARG module_path
ARG target_dir_name

WORKDIR /root
# Installs google cloud sdk, this is mostly for using gsutil to export model.
RUN wget -nv https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz && \
    mkdir /root/tools && \
    tar xvzf google-cloud-sdk.tar.gz -C /root/tools && \
    rm google-cloud-sdk.tar.gz && \
    /root/tools/google-cloud-sdk/install.sh --usage-reporting=false \
        --path-update=false --bash-completion=false \
        --disable-installation-options && \
    rm -rf /root/.config/* && \
    ln -s /root/.config /config && \
    # Remove the backup directory that gcloud creates
    rm -rf /root/tools/google-cloud-sdk/.install/.backup

# Path configuration
ENV PATH $PATH:/root/tools/google-cloud-sdk/bin
# Make sure gsutil will use the default service account
RUN echo '[GoogleCompute]\nservice_account = default' > /etc/boto.cfg

WORKDIR /opt/program/

# Here we get all python packages.
RUN pip install mldock[gcp]
