FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY holded_test/ .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]