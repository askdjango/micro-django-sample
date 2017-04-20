FROM python:3.6

WORKDIR /app/askdjango
COPY . /app

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip3 install -r /app/requirements.txt

USER uwsgi
EXPOSE 8080

CMD ["/bin/sh", "run.py"]

