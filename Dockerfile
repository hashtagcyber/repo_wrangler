FROM python:3

COPY app /app

RUN python -m pip install -r /app/requirements.txt

ENTRYPOINT [ "/app/app.py" ]