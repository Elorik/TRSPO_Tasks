# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /server
WORKDIR /server

# Copy the current directory contents into the container at /server
COPY . /server

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run server.py when the container launches
CMD ["python", "server.py"]
