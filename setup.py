from setuptools import setup

setup(
    name='silkaudio',
    packages=['silkaudio'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask_sqlalchemy', 'flask_migrate', 'psycopg2'
    ],
)