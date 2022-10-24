FROM python:3.8

WORKDIR /python_app
COPY . /python_app

RUN pip install -r requirements.txt


CMD [ "python", "python_app/main.py" ]
