import json
#import sqlalchemy
import urllib.parse
import base64
import secrets
import hashlib
import boto3
import os
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

def saltHash(password, salt):
  password_bytes = password.encode(encoding='UTF-8')
  if (salt == ''):
    salt_bytes = secrets.token_bytes(16)
  else:
    salt_bytes = base64.b64decode(salt.encode(encoding='UTF-8'))

  # Hashes salted password
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

  return (hashed_password, salt)


def hello(event, context):
    #print(event['key1'])
    print(os.environ['DB_CONNECTION'])

    #saltHashTuple = saltHash('Password1', '')
    #saltHashPwd = saltHashTuple[0]
    #salt = saltHashTuple[1]
    #print('Hashed Password = ' + saltHashPwd)
    #print('salt = ' + salt)

    #usr = advito_user(id=1, client_id=1, username='Chuck Norris', pwd=saltHashPwd, name_last='Norris', name_first='Chuck',
    #  is_enabled=True, must_change_pwd=False, pwd_expiration='01/01/2024', email='chucknorris@gmail.com',
    #  phone='123', profile_picture_path='/', timezone_default='EST', language_default='murican', user_salt=salt,
    #  created='01/01/1900', modified='12/12/2018')
    #session.add(usr)
    #session.commit()

    #salt = 'rB/YTF0DENZhZiPV9cpaeg=='
    username = event['username']
    password = event['password']

    for row in session.query(advito_user).filter(advito_user.username==username):
      salt = row.user_salt

    print('salt = ' + salt)
    saltHashTuple = saltHash(password, salt)
    saltHashPwd = saltHashTuple[0]
    salt = saltHashTuple[1]
    print('Hashed Password = ' + saltHashPwd)

    user_is_enabled = False
    user_id = 0
    user_email = ''
    user_displayname = ''
    user_token = 'abc'

    for row in session.query(advito_user).filter(advito_user.username==username, advito_user.pwd==saltHashPwd):
      print(row.id, row.name_first, row.name_last, row.email,  row.is_enabled)
      user_is_enabled = row.is_enabled
      user_id = row.id
      user_email = row.email
      user_displayname = row.name_first + " " + row.name_last

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
