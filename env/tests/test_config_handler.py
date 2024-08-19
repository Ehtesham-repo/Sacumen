import pytest
import os
import json
from config_module.config_handler import ConfigHandler

@pytest.fixture
def config_handler():
    """Fixture to provide a ConfigHandler instance for tests."""
    return ConfigHandler()

def test_read_yaml(config_handler):
    """Test reading and flattening a YAML file."""
    yaml_content = """
    server:
      host: localhost
      port: 8080
    """
    with open('test.yaml', 'w') as f:
        f.write(yaml_content)

    data = config_handler.read_yaml('test.yaml')
    expected = {
        'server_host': 'localhost',
        'server_port': 8080
    }
    assert data == expected

def test_read_ini(config_handler):
    """Test reading and flattening an INI file."""
    ini_content = """
    [server]
    host = localhost
    port = 8080
    """
    with open('test.cfg', 'w') as f:
        f.write(ini_content)

    data = config_handler.read_ini('test.cfg')
    expected = {
        'server_host': 'localhost',
        'server_port': '8080'
    }
    assert data == expected

def test_write_to_env(config_handler):
    """Test writing data to a .env file."""
    data = {
        'TEST_KEY': 'test_value'
    }
    config_handler.write_to_env(data, '.env')
    with open('.env', 'r') as f:
        content = f.read()
    assert 'TEST_KEY=test_value' in content

def test_write_to_json(config_handler):
    """Test writing data to a JSON file."""
    data = {
        'key': 'value'
    }
    config_handler.write_to_json(data, 'test.json')
    with open('test.json', 'r') as f:
        content = json.load(f)
    assert content == data

def test_set_env_variables(config_handler):
    """Test setting environment variables."""
    data = {
        'ENV_VAR': 'value'
    }
    config_handler.set_env_variables(data)
    assert os.environ['ENV_VAR'] == 'value'

def teardown_module(module):
    """Cleanup after tests."""
    if os.path.exists('test.yaml'):
        os.remove('test.yaml')
    if os.path.exists('test.cfg'):
        os.remove('test.cfg')
    if os.path.exists('.env'):
        os.remove('.env')
    if os.path.exists('test.json'):
        os.remove('test.json')
    if 'ENV_VAR' in os.environ:
        del os.environ['ENV_VAR']
