FROM python:3.11-slim
COPY requirements.txt requirements.txt 
RUN pip3 install  -r requirements.txt
ADD code /code
WORKDIR /code
CMD bash

