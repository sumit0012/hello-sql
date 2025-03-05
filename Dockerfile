# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to be accessible from outside the container
EXPOSE 8080

# Set environment variables (can be overridden at runtime)
ENV DB_HOST=mysql.hwsql.svc.cluster.local
ENV DB_ROOT_USER=root
ENV DB_ROOT_PASSWORD=sam123
ENV DB_NAME=hello_sql
ENV NEW_USER=sumit
ENV NEW_PASSWORD=sumit123

# Run the application when the container starts
CMD ["python", "app.py"]
