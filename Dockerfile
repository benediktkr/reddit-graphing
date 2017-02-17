FROM python:2.7
MAINTAINER Lehmann

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app
RUN chmod +x /app/main.py
RUN pip install -e .

ENTRYPOINT ["python", "main.py", "5"]
