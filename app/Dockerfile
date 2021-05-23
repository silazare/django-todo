FROM python:3.9-slim-buster

RUN set -ex && \
    mkdir /app && \
    apt-get update -qq && \
    apt-get install --no-install-recommends -qq -y git=1:2.20.1-2+deb10u3 && \
    pip3 install --no-cache-dir pipenv==11.9.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN set -ex && \
    adduser --no-create-home --disabled-password --gecos '' appuser && \
    mkdir /app

USER appuser

WORKDIR /app

RUN set -ex && \
    git clone https://github.com/shacker/gtd.git /app && \
    pipenv --python 3.9 && \
    pipenv install --dev && \
    pipenv install --keep-outdated Faker==8.2.0

COPY local.py project/.
COPY entrypoint.sh .

RUN set -ex && \
    chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
