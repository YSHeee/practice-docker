FROM python:3.8.16-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV NUM="2000"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "13583"]
