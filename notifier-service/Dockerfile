FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY notifier-service/requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY /scripts/install-wait-for-it.sh .
RUN /bin/sh install-wait-for-it.sh

COPY . /code

ENV PYTHONPATH "${PYTHONPATH}:/code"

EXPOSE 8080

CMD ["python", "notifier-service/run.py"]
