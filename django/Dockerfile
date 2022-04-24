FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Set apps home directory.
ENV APP_DIR /code
RUN mkdir ${APP_DIR}

# Define current working directory.
WORKDIR ${APP_DIR}

ENV DOCKERIZE_VERSION v0.6.1
RUN apt-get update && apt-get install -y wget && apt-get install -y git\
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# ファイルをコンテナにコピー
COPY ./django ${APP_DIR}/
COPY ./.env ${APP_DIR}/
 
# Pythonのモジュールをインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

