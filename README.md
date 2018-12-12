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
In order to deploy this service to AWS lambda, an IAM user with programmatic access must be created
and configured for your local machine.

1. Create IAM user with programmatic access and permission to use lambda

2. Download credentials.csv and run:
```bash
aws configure
```
This will prompt you for credentials.
Copy the values from credentials.csv.

When prompted for *region*, enter *us-east-2* which is based in Ohio.

When prompted for *output*, enter *text*.

These credentials will be stored in ~/.aws/credentials under the *default* profile.
Other configurations will be stored in ~/.aws/config
After that is done, you'll be able to access aws lambda from the command-line.

3. Test CLI:
```bash
aws lambda list-functions
```
You should get a list of functions that have been deployed.

## Setting Up Environment Variables
Under the directory *lambdas*, there is a file called env.example.yml.
Copy this to env.yml and open it in the text editor of your choice.
We'll be working under the *dev* section of the file.
Replace the example values to their actual values.
You'll need to reach out to a fellow employee to determine what these values are.

## Deploying application
When deploying the application, you are deploying lambda functions to AWS for a particular *stage*.
Currently, the only stage is *dev*, though in the future, there will be *prod* as well.
The stage that is used when deploying does two things:

1. Alters the full name of the lambda. For instance, if the name of a particular lambda is *hello_world* and the stage is set to *dev* when deployed,
it will be called as <service_name>-dev-hello_world.
If *prod* is set, it will be deployed as <service_name>-prod-hello_world.

2. Determines environment variables that are set in each lambda.
For instance, if *dev* is set, environment variables will be set to the values in *dev* from env.yml.
This is useful when since lambdas from different stages often reach out to different databases.
