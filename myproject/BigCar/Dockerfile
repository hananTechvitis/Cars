# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Collect static files directly into /static/
RUN python manage.py collectstatic --no-input --clear --directory /static/

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "BigCar.wsgi:application"]
