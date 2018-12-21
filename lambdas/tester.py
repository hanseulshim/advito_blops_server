#!/usr/bin/env python3

########### Must simulate environment variables before importing handler module ################
def simulate_environment_variables():

    """
    Simulates environment variables from env.yml file
    """

    import os
    import yaml
    from pathlib import Path

    # Reads environment file
    env_path = Path('env.yml')
    with env_path.open('r') as env_file:
        env_dict = yaml.load(env_file)

    # Sets environment variables for dev environment
    dev_dict = env_dict['dev']
    for key, value in dev_dict.items():
        os.environ[key] = str(value)

simulate_environment_variables()


# Imports
import unittest
import os
from test.usertests import UserTests


# Starts all tests imported
if __name__ == '__main__':
    unittest.main()
