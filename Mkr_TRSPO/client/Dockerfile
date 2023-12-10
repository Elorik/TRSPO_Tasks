# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /client
WORKDIR /client

# Copy the current directory contents into the container at /client
COPY . /client

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run client.py when the container launches
CMD ["python", "client.py"]
