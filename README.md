# Creating Api using Python and Django

To create this project I have used python version 3.8.2 ,django version 3.0 and djangorestframework. Here I'm Using python's default database sqlite3. To populate database I used admin-site.

## Description 

In the project I created three models Members, Emp and Active and relate them by Many-To-One model relationships,
and to serielize the data and create api I used django rest framework. I have used default SQLite3 database to store data and provided data using admin-site.


## Installation

First of all install the dependencies by running the following command on your terminal pip install -r requirements.txt on your terminal. 

```bash
pip install -r requirements.txt
```
or We can run following commands:

```bash
pip install django==3.0
pip install djangorestframework==3.11.0
```

## How to run

Create superuser by running this command:
```bash
python manage.py createsuperuser
```
and after that run makemigrations, migrate and runserver commands:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
and copy the link and paste to browser urlbox. and open admin-site using http://127.0.0.1:8000/admin.
and log in to admin-site using the username and password that you created using createsuperuser command.

here ,you can see 3 tables members, emp, and active. All the three models are relate to each other by Many-To-One model relationships, here you can add data simply by click on add button,
you can add true or false value in Members model.

you can add id, real_name and timezone in Emp model and also give relation to previous Members model.

you can add starting_time and end_time in Active model and also give relation to previous Emp model.

now go to the url: http://127.0.0.1:8000/members/ or open terminal and run the following command:
```bash
curl http://127.0.0.1:8000/members/
```
you will get the data in JSON format like this (example data):

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "ok": true,
        "members": [
            {
                "id": "101",
                "real_name": "prince",
                "tz": "asia/kolkata",
                "activity_status": [
                    {
                        "start_time": "2020-06-02T11:33:31Z",
                        "end_time": "2020-06-03T11:33:38Z"
                    },
                    {
                        "start_time": "2020-06-05T11:33:54Z",
                        "end_time": "2020-06-21T11:34:01Z"
                    },
                    {
                        "start_time": "2020-06-05T10:54:04Z",
                        "end_time": "2020-06-07T11:34:31Z"
                    }
                ]
            },
            {
                "id": "102",
                "real_name": "pranay",
                "tz": "newyork",
                "activity_status": [
                    {
                        "start_time": "2020-06-24T11:34:50Z",
                        "end_time": "2020-06-23T11:34:54Z"
                    },
                    {
                        "start_time": "2020-06-21T11:35:10Z",
                        "end_time": "2020-06-26T11:35:23Z"
                    },
                    {
                        "start_time": "2020-06-20T11:35:31Z",
                        "end_time": "2020-06-25T11:35:38Z"
                    }
                ]
            }
        ]
    }
]


