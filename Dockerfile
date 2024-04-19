# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at
COPY . /

# Create virtual environment and install dependencies
RUN python -m venv /openai-env && \
    /openai-env/bin/pip install --upgrade pip && \
    /openai-env/bin/pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World
ENV PATH="/openai-env/bin:$PATH"


# Run app.py when the container launches
# CMD python -W ignore upload.py --pdf_file=${PDF_FILE}
CMD python -W ignore query.py