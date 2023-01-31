# 5.24GB
ARG CONDA_ENV=docker_p
ARG CONDA_DIR=/opt/conda
ARG APP_DIR=/code

FROM nvidia/cuda:11.3.0-cudnn8-devel-ubuntu20.04 AS builder

ARG CONDA_ENV
ARG CONDA_DIR

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHON_VERSION=3.8 \
    PATH=$CONDA_DIR/bin:$PATH 

SHELL ["/bin/bash", "-c"]

COPY ./requirements.txt /requirements.txt

RUN export BUILD_TARGET_ARCH=$(uname -m) && \
    echo "$BUILD_TARGET_ARCH" && \
    apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends wget unzip bzip2 build-essential ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    if [ ${BUILD_TARGET_ARCH} == "x86_64" ]; then \
        export CONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh; \
    elif [ ${BUILD_TARGET_ARCH} == "arm64" ]; then \
        export CONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-arm64.sh; \
    else echo "Unsupported Flatform"; \
    fi && \ 
    wget -q $CONDA_URL -O /root/miniconda.sh && \
    /bin/bash /root/miniconda.sh -b -p /opt/conda && \
    rm /root/miniconda.sh &&  \
    /opt/conda/condabin/conda clean -y -av && \
    /opt/conda/condabin/conda update -y conda && \
    if [ $BUILD_TARGET_ARCH == "x86_64" ]; then \
        /opt/conda/condabin/conda install -y pytorch==1.11.0 cudatoolkit=11.3 -c pytorch; \
    elif [ $BUILD_TARGET_ARCH == "arm64" ]; then \
        /opt/conda/condabin/conda install pytorch==1.12.1 cpuonly -c pytorch; \
    fi && \
    conda install -c conda-forge uvicorn &&\
    conda install -c conda-forge fastapi &&\
    /opt/conda/condabin/conda clean -y -av 


FROM nvidia/cuda:11.3.0-base-ubuntu20.04 AS base

ARG CONDA_ENV
ARG CONDA_DIR

ENV PATH=$CONDA_DIR/bin:$PATH 
ENV PATH=/opt/conda/envs/$CONDA_ENV/bin:$PATH

RUN echo -e ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    rm -vrf /var/lib/apt/lists/* /var/cache/apt/archives/* /tmp/* /root/.cache/* 

COPY --from=builder /opt /opt


FROM base AS source
ARG APP_DIR

WORKDIR /${APP_DIR}
COPY ./app /${APP_DIR}/app

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "13583"]
