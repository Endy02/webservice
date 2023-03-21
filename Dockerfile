FROM python:latest

EXPOSE 8000

ADD . /test_projects
WORKDIR /test_projects

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py loaddata fixtures/*.json

RUN ls -a

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver"]