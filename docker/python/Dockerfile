ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}
SHELL ["/bin/bash", "-l", "-c"]

#####################################
# Set Timezone
#####################################
ARG TZ=UTC
ENV TZ ${TZ}
#RUN apt-get update && apt-get install -y curl wget gnupg2 systemd gettext-base vim
COPY ./docker/python/setup.sh /usr/local/bin/
RUN set -eu && chmod +x /usr/local/bin/setup.sh

RUN /usr/local/bin/python -m pip install --upgrade pip && /usr/local/bin/python -m pip install poetry
COPY ./poetry.lock ./poetry.toml ./pyproject.toml /var/app/

RUN cd /var/app/ && poetry install

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "-l", "-c", "setup.sh"]
