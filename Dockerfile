# Use the official Python image as the base image
FROM python:3.12.0b4-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirement file to the working directory
COPY requirements.txt .

# Install the required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variables for the flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which Flask app will run
EXPOSE 5000

# Start the Flask app when the container is run
CMD [ "flask", "run" ]

