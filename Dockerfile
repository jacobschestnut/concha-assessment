FROM python:3.9

WORKDIR /concha-assessment

COPY ./src ./src

ENV PYTHONUNBUFFERED=1

CMD ["python", "./src/request_handler.py"]