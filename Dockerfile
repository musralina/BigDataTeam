FROM python:3.9

WORKDIR /src/bigdatateam/

COPY /src/bigdatateam/code.py .

ENTRYPOINT ["python3", "code.py"]

CMD ["10", "42"]
