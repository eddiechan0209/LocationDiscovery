"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

def get_user_name():
    return auth.current_user.get('first_name') if auth.current_user else None

def get_user_last_name():
    return auth.current_user.get('first_name') if auth.current_user else None

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
# db.define_table(
#     'user_info',
#     # Field('user_id', 'reference auth_user'),
#     Field('FirstName'),
#     Field('LastName', default=get_user_last_name, requires=IS_NOT_EMPTY()),
#     Field('Username', requires=IS_NOT_EMPTY()),
#     Field('Email', default=get_user_email),
#     Field('Bio'),
# )

db.define_table(
    'post',
    Field('user_id', 'reference auth_user'),
    Field('post_title', requires=IS_NOT_EMPTY()),
    Field('post_description'),
    Field('latitude', requires=IS_FLOAT_IN_RANGE(-90, 90)),
    Field('longitude',  requires=IS_FLOAT_IN_RANGE(-180, 180)),
    )

db.define_table(
    'friends',
    Field('friender_id', 'reference auth_user'),
    Field('FriendAdded_id', 'reference auth_user')
)

# define another table for photos
# have a reference to post

db.define_table(
    'requests',
    Field('requester_id', 'reference auth_user'),
    Field('active', 'boolean'),
    Field('target_id', 'reference auth_user')
)

db.commit()
