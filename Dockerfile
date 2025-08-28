FROM python:3.10.18

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver" ]
