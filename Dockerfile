FROM python

WORKDIR /app

COPY . /app

CMD ["python","-u","Task1.py"]
