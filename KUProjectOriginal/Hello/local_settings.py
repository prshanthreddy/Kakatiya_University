import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES={
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':os.path(BASE_DIR,'db.sqlite3'),
    }
}