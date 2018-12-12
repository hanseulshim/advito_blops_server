# Advito Blops Server

This is a serverless GraphQL web service utilizing the serverless framework to deploy
to AWS Lambda.

## Software Dependencies for Developers
1. **Homebrew** (If on Mac): https://brew.sh/

2. **Python3.6**: https://www.python.org/downloads/release/python-366/

Python3 can be used using the *python3* command.
Invoking pip is done via:
```bash
python3 -m pip install <some_lib>
```
You can also create a virtual environment via:
```bash
python3 -m venv <path/to/local_python>
```
This should also install pip.

3. **NodeJS**:
```bash
brew install node
```
This should also install npm (Node Package Manager)

4. **Serverless**:
```
npm install -g serverless
```
5. **AWS CLI**:

```bash
python3 -m pip install awscli
```

## Setting Up AWS Account
1. Create IAM user with programmatic access and permission to use lambda

2. Download credentials.csv and run:
```bash
aws configure
```
Copy the values prompted in credentials.csv
When prompted for *region*, select *us-east-2* which is based in Ohio.
When prompted for *output*, select *text*.
After that is done, you'll be able to access aws lambda from the cli.
These credentials will be stored in ~/.aws/credentials under the *default* profile.
Other configurations will be stored in ~/.aws/config

3. Test CLI:
Run:
```bash
aws lambda list-functions
```
You should get a list of functions that have been deployed.

## Deploying application
When deploying the application, you are deploying lambda functions for a particular *stage*.
Currently, the only stage is *dev*, though in the future, there will be a *prod*.
The stage that is used when deploying does two things:
1. Alters the full name of the lambda. For instance, if the name of a particular lambda is *hello_world* and the stage is set to *dev* when deployed,
it will be deployed as <service_name>-dev-hello_world.
If *prod* is set, it will be deployed as <service_name>-prod-hello_world.
