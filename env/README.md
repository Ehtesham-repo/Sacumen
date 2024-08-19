Overview
The config_handler module is a Python package designed to handle configuration files. It supports reading configuration files in .yaml, .cfg, and .conf formats and can generate a flat dictionary from these files. The module can write configurations to .env and .json files and set configurations as environment variables.
Features
Read Configuration Files: Supports .yaml, .cfg, and .conf formats.
Generate Flat Dictionary: Converts configuration data into a flat dictionary.
Write Configurations:
.env files
.json files
Set Environment Variables: Directly set configurations as environment variables.
Installation
Clone the Repository:
Create a Virtual Environment: python -m venv env
Activate the Virtual Environment:
On Windows: . \env\Scripts\activate
Install Dependencies: pip install -r requirements.txt

Reading Configuration Files: 
To read and convert a configuration file into a flat dictionary:
from config_module.config_handler import ConfigHandler
config_handler = ConfigHandler()
config_dict = config_handler.read_yaml('path/to/your/config.yaml')
print(config_dict)







Writing to .env File: 

config_dict = {
    'KEY': 'value'
}
config_handler.write_to_env(config_dict, '.env')


Writing to .json File:
config_dict = {
    'key': 'value'
}
config_handler.write_to_json(config_dict, 'config.json')


Setting Environment Variables:

config_dict = {
    'ENV_VAR': 'value'
}
config_handler.set_env_variables(config_dict)


Testing
To run tests for this module:
Ensure the virtual environment is activated.
Run the tests: pytest

