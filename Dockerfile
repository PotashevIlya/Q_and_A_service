FROM python:3.12-slim

WORKDIR /Q_and_A_service

COPY ./requirements.txt /Q_and_A_service/requirements.txt

RUN pip install --no-cache-dir -r /Q_and_A_service/requirements.txt

COPY . /Q_and_A_service/

CMD ["sh", "run.sh"]