from setuptools import setup, find_packages

setup(
    name='config_module',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml'
    ],
    tests_require=[
        'pytest'
    ],
    description='A module to handle reading and writing configuration files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ehteshamul Haque',
    author_email='ehtesham.act@gmail.com',
    url='https://github.com/Ehtesham-repo/Sacumen',
)
