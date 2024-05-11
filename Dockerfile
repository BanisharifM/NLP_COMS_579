# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Accept OPENAI_API_KEY as a build argument
ARG OPENAI_API_KEY

# Set the OPENAI_API_KEY as an environment variable
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# EXPOSE the port where Streamlit will run
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
