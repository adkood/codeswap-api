FROM python:3.8
COPY requirements.txt /code/
CMD ["python", "manage.py", "runserver"]
