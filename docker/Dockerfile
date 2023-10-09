FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN apt-get update && apt-get install libpq-dev gcc cron -y  \
    && pip install --upgrade pip && pip install -r requirements.txt \
    && echo '0 * * * * /usr/local/bin/python /usr/src/app/cli.py collect >> /var/log/cron.log 2>&1' > /etc/cron.d/weather_collector \
    && chmod 0644 /etc/cron.d/weather_collector && crontab /etc/cron.d/weather_collector