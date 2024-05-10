FROM python:3

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /opt/code
WORKDIR /opt/code

# Copy requirements and install
COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

# Copy the rest of the application code
COPY . /opt/code