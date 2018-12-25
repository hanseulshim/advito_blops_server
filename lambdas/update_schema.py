#!/usr/bin/env python3
import yaml
import os

# Opens environment file
with open('env.yml') as env_file:

    # Parses environment file
    env_dict = yaml.load(env_file)
    dev_dict = env_dict['dev']
    connection = dev_dict['DB_CONNECTION']

    # Runs command to generate schema
    os.system("sqlacodegen '{}' --outfile advito/model/table.py".format(connection))
