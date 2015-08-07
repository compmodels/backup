FROM python:2.7

RUN apt-get update && apt-get install -y python-netifaces duplicity gcc python-dev
RUN pip2.7 install pyrax python-keystoneclient

RUN mkdir /srv/backup
WORKDIR /srv/backup
ADD backup.py /srv/backup/backup.py

ENV PYTHONPATH /usr/local/lib/python2.7/site-packages
ENTRYPOINT ["python2.7", "backup.py"]