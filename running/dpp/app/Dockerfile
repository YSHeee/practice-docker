# syntax=docker/dockerfile:1.4

# FROM python:3
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/


FROM python:3.7-alpine 
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./manage.py /app/manage.py
COPY ./example /app/example
ENTRYPOINT ["python"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
# EXPOSE 8000
# WORKDIR /app 
# COPY requirements.txt /app
# RUN pip3 install -r requirements.txt --no-cache-dir
# COPY . /app 
# ENTRYPOINT ["python3"] 
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# FROM builder as dev-envs
# RUN <<EOF
# apk update
# apk add git
# EOF

# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF
# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]