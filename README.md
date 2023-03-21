# Web Service

<br>
<br>

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white) !![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

---

Web API to store projects that a company made. The API was made with  [Django](https://docs.djangoproject.com/en/4.1/) and [Django Rest Framework](https://www.django-rest-framework.org/)

---


## :palm_tree: Features

| Technology | Description |
| --- | --- | ---| --- |
| Django | Python framework for web applications |
| Django Rest Framework | Django package that allow django to turn his models into restfull API's endpoints |


---

## :star2: Installation

<b>Step 1 : Install python</b>

https://www.python.org/downloads/

<b>Step 2 : After the installation of python you may the PIP package manager installed, so you will need to install a Virutal environment to run the project</b>

```bash
py -m pip install --user virtualenv
```

<b>Step 3 : Clone the repository</b>

```bash
git clone https://github.com/Endy02/webservice.git
```

<b>Step 4 : Go in the project folder and create a new virtual environment</b>

```bash
cd webservice
```

```bash
py -m pip install --user virtualenv
```

> if the 'py' doesn't work, try this :
>
> ```bash
> python3 -m pip install --user virtualenv
> ```
> This will create a new virtual environment in the root directory

<b>Step 5 : Install all package that the project need</b>

```bash
pip install -r requirements.txt
```

<b>Step 6 : Run the migrations and fixtures to create the project database and dummy data</b>

```bash
py manage.py migrate && py manage.py loaddata fixtures/*.json
```
> This wil create the database schema and insert dummy data in it

<b>Step 7 : Run the server and publish the API</b>

```bash
py manage.py runserver
```

The server will run after all this steps, you will that you can access it by the localhost url:

http://localhost:8000
or
http://127.0.0.0:8000

---

## :bookmark_tabs: Usage

Open a new terminal and go in the project directory to run the script that use the api started earlier :

```bash
cd webservice
```

```bash
py main.py
```
This script that test the API endpoints will show informations in the terminal.

---

## :pencil: License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


