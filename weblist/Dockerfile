FROM python:alpine

WORKDIR /code
COPY requirements.txt /code
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP list.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 8001
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 8001

CMD ["flask", "run"]
