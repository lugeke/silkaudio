FROM python:3.6.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=autoapp.py FLASK_DEBUG=1

CMD "/usr/local/bin/gunicorn -w 2 -b :8000 autoapp:app"
