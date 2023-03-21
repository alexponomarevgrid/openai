FROM python:slim

RUN mkdir /app
WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y stress

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY tgbot.py /app

EXPOSE 5001

ENTRYPOINT ["python", "-u"]

CMD ["/app/tgbot.py"]
