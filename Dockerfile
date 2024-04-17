FROM python:3.8.5

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

CMD ["python","-u","Task1.py"]
