FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY /scripts/install-wait-for-it.sh .
RUN /bin/sh install-wait-for-it.sh

COPY . /code

ENV PYTHONPATH "${PYTHONPATH}:/code"

EXPOSE 8000

CMD bash -c "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload"
