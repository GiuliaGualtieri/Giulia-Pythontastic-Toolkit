FROM python:3.10-slim

RUN apt-get update \
    && apt-get install build-essential git -y --no-install-recommends

ENV PYTHONUNBUFFERED=1

RUN python -m pip install pip --upgrade \
    && python -m pip install hatch

COPY . .

ENV PIP_USER false

RUN python -m hatch env create
