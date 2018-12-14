import json
import urllib.parse
import base64
import secrets
import hashlib
import boto3
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, DateTime, func, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base


Base = automap_base()
engine = create_engine(os.environ['DB_CONNECTION'] % urllib.parse.quote_plus(os.environ['DB_PASSWORD']))
Base.prepare(engine, reflect=True)
advito_user = Base.classes.advito_user
client = Base.classes.client
advito_user_session = Base.classes.advito_user_session
session = Session(engine)


def saltHash(password, salt=None):

    """
    Both hashes and salts a password.
    If salt is not supplied, salt will be created randomly.
    Salt is a base64 encoded string of bytes.
    Password is a string.
    Returns a tuple of the password and the salt that was used.
    """

    # Creates password bytes and either uses or calculates salt bytes.
    password_bytes = password.encode(encoding='UTF-8')
    if (salt is None):
        salt_bytes = secrets.token_bytes(16)
    else:
        salt_bytes = base64.b64decode(salt.encode(encoding='UTF-8'))

    # Hashes and salts password
    algo = hashlib.sha256()
    algo.update(password_bytes)
    algo.update(salt_bytes)
    hashed_password_bytes = algo.digest()

    # Converts both combined password and salt to base64-encoded strings
    hashed_password = base64 \
        .b64encode(hashed_password_bytes) \
        .decode('UTF-8')
    salt = base64 \
        .b64encode(salt_bytes) \
        .decode('UTF-8')

    # Returns as tuple
    return (hashed_password, salt)


def create_user(event, context):

    """
    Reads a user from the event body and inserts it into the database.
    """

    # Reads user payload from body
    user_body = event['body']
    user_json = json.loads(user_body)

    # Salts and hashes password. Writes result back to json.
    salt_and_hash = saltHash(user_json['pwd'])
    user_json['pwd'] = salt_and_hash[0]
    user_json['user_salt'] = salt_and_hash[1]

    # Sets default values
    user_json['is_enabled'] = True
    user_json['must_change_pwd'] = False
    user_json['pwd_expiration'] = '01/01/2024'
    user_json['created'] = '01/01/1900'
    user_json['modified'] = '12/12/2018'

    # Converts to advito_user and saves it
    usr = advito_user(**user_json)
    session.add(usr)
    session.commit()


def _create_user_session(user):

    """
    Creates, inserts and returns a session for the user specified.
    """

    # Generates random boken
    session_token = secrets.token_bytes(32)
    session_token = base64.b64encode(session_token)

    # Creates user session object
    user_session = advito_user_session (
        advito_user_id = user.id,
        session_token = session_token,
        session_start = datetime.utcnow()
    )

    # Inserts session into the database
    session.add(user_session)
    session.commit()

    # Done
    return user_session



def login(event, context):

    """
    Reads user credentials, generates a token and stores it in the database.
    Returns token to user.
    """

    # Reads login payload from body
    login_body = event['body']
    login_json = json.loads(login_body)

    # Reads in user where username matches
    user = session \
        .query(advito_user) \
        .filter_by(username=login_json['username']) \
        .first()

    # Gets password and salt of existing user
    db_password = user.pwd
    db_salt = user.user_salt
    db_salt = base64.b64decode(db_salt)

    # Massages password given
    login_password = login_json['pwd']
    login_password = saltHash(login_password, db_salt)[0]


    # If passwords match, create session
    if login_password == db_password:

        # Creates random base64-encoded token
        session_token = secrets.token_bytes(32)
        session_token = base64.b64encode(session_token)

        # Gets existing user session
        user_session = session \
            .query(advito_user_session) \
            .filter_by(advito_user_id=user.id) \
            .first()

        # If session was not found, create it
        if user_session is None:
            user_session = _create_user_session(user)

        print('Session is...')
        print(user_session)

        # Creates session object
        user_session = advito_user_session (
            advito_user_id = user.id,
            session_token = session_token,
            session_start = datetime.utcnow()
        )

        # Stores in db
        session.add(user_session)
        session.commit()
        print("Committed?")

        response =  {
            "statusCode": 200,
            "body": {
                "message": "Success!"
            }
        }

    # Otherwise, let user know passwords did not match
    else:
        response = {
            "statusCode": 400,
            "body": {
                "message": "Invalid username or password"
            }
        }

    # Sends response
    return response





def hello(event, context):

    #saltHashTuple = saltHash('Password1', '')
    #saltHashPwd = saltHashTuple[0]
    #salt = saltHashTuple[1]
    #print('Hashed Password = ' + saltHashPwd)
    #print('salt = ' + salt)

    #usr = advito_user(id=2, client_id=1, username='joeuser', pwd=saltHashPwd, name_last='User', name_first='Joe',
    #  is_enabled=True, must_change_pwd=False, pwd_expiration='01/01/2024', email='joeuser@gmail.com',
    #  phone='123-4567', profile_picture_path='/', timezone_default='EST', language_default='English', user_salt=salt,
    #  created='01/01/1900', modified='12/12/2018')
    #session.add(usr)
    #session.commit()

    #salt = 'rB/YTF0DENZhZiPV9cpaeg=='
    username = event['username']
    password = event['password']

    user_is_enabled = False
    user_id = 0
    user_email = ''
    user_displayname = ''
    user_token = 'abc'
    salt = ''

    for row in session.query(advito_user).filter(advito_user.username==username):
      salt = row.user_salt
      user_is_enabled = row.is_enabled
      user_id = row.id
      user_email = row.email
      user_displayname = row.name_first + " " + row.name_last
      user_pwd = row.pwd

    print('salt = ' + salt)
    saltHashTuple = saltHash(password, salt)
    saltHashPwd = saltHashTuple[0]
    salt = saltHashTuple[1]
    print('Hashed Password = ' + saltHashPwd)
    print('user_pwd = ' + user_pwd)

    #for row in session.query(advito_user).filter(advito_user.username==username, advito_user.pwd==saltHashPwd):
    #  print(row.id, row.name_first, row.name_last, row.email,  row.is_enabled)
    #  user_is_enabled = row.is_enabled
    #  user_id = row.id
    #  user_email = row.email
    #  user_displayname = row.name_first + " " + row.name_last

    # Print the column names of each table.
    #for table in Base.metadata.sorted_tables:
    #  print(table.name)
    #  for column in table.columns:
    #    print(column)

    for row in session.query(advito_user_session).filter(advito_user_session.advito_user_id==user_id):
      print('session_token = ' + row.session_token)
      user_token = row.session_token

    response = {
        "statusCode": 200,
        "user_id": user_id,
        "displayname": user_displayname,
        "email": user_email,
        "session_token": user_token
    }

    return response
