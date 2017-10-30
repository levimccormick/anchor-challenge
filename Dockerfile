# Test the lambda code
FROM python:3.6-alpine3.6

COPY code/requirements.pip /opt/app/
RUN pip install -r /opt/app/requirements.pip
COPY tests/* /tests/
CMD python /code/process.py
