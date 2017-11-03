FROM alpine:latest
RUN apk add --no-cache \
        uwsgi \
        uwsgi-python3 \
        python3
COPY reporting /app/reporting
COPY setup.py /app/setup.py
WORKDIR /app
RUN pip3 install --no-cache-dir -e /app
CMD uwsgi  --plugin python3  -b 32768 -s 0.0.0.0:9000  --wsgi-file /app/reporting/main/main.py  --callable create_app