import os
from autoapp import app


# Postgres Initialization Files
docker_file = 'Dockerfile'
source_dir = os.path.abspath(os.curdir)
destination_dir = os.path.join(source_dir, '../postgresql')

# Before creating files, check that the destination directory exists
if not os.path.isdir(destination_dir):
    os.makedirs(destination_dir)

# Create the 'Dockerfile' for initializing the Postgres Docker image
with open(os.path.join(destination_dir, docker_file), 'w') as f:
    f.write('FROM postgres:10.1-alpine')
    f.write('\n')
    f.write('\n# Set environment variables')
    f.write('\nENV POSTGRES_USER {}'.format(app.config['POSTGRES_USER']))
    f.write('\nENV POSTGRES_PASSWORD {}'.format(app.config['POSTGRES_PASSWORD']))
    f.write('\nENV POSTGRES_DB {}'.format(app.config['POSTGRES_DB']))
    f.write('\n')
