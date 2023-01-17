FROM python:3.8.16-slim
# FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV NUM="2000"

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--host", "0.0.0.0", "--port", "13583"]