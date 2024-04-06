# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir llama-index-vector-stores-weaviate==0.1.4
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD python -W ignore upload.py --pdf_file=${PDF_FILE}
# CMD ["python", "src/openai-test.py"]