FROM python:3.8

COPY /auto_flink .

CMD ["python", "./auto_flink/__main__.py"]