FROM python:3.8.3-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Based on https://alembic.sqlalchemy.org/en/latest/front.html#installation and
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
COPY config/requirements.txt /tmp
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

CMD ["python", "-m", "main", "/app"]
